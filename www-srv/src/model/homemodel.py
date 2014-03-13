# coding=UTF8

"""

Home page model.

TODO: check all select * and state the fields.
TODO: review SQL parsing. Use bindings.

"""

from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
import datetime


class HomeModel(PostgreSQLModel):
    """Home model."""

    def getDocument(self, idDocument, lang):
        """Gets the document details."""
        doc = """
        with label_en as(
          select
            a.id_document as id_document,
            array_agg(b.label) as labels
          from
            www.document_label_en a
            inner join www.label_en b
            on a.id_label_en=b.id_label_en
          group by id_document),
        label_es as(
          select
            a.id_document as id_document,
            array_agg(b.label) as labels
          from
            www.document_label_es a
            inner join www.label_es b
            on a.id_label_es=b.id_label_es
          group by id_document),
        authors as(
          select
            id_document as id_document,
            array_agg(coalesce(twitter_user, name)) as author
          from www.author
          group by id_document),
        docs as(
          select
            a.id_document,
            title_{} as title,
            theme_{} as theme,
            description_{} as description,
            a.last_edit_time as time
          from www.document a
        )
        select
          a.id_document as id,
          a.title as title,
          a.theme as theme,
          a.description as description,
          a.time as time,
          b.labels as labels,
          d.author as authors
        from
          docs a inner join 
          label_{} b on
          a.id_document=b.id_document inner join
          authors d on
          a.id_document=d.id_document
        where
          a.id_document=%s""".format(lang, lang, lang, lang)

        return(self.query(doc, bindings=[idDocument]).result())

    def getDocumentPdf(self, idDocument):
        """Gets the PDF for a given idDocument."""
        pdf = """
        select
          lang,
          pdf_name,
          hash
        from
          www.pdf
        where id_document=%s;"""

        return(self.query(pdf, bindings=[idDocument]).result())


    def getDocumentCatalogSize(self, search=None):
        """Gets the total size of a list of document."""
        docs = """
        with count as(
        select distinct a.id_document
        from
          www.document a inner join
          www.document_label_en b on
          a.id_document=b.id_document inner join
          www.label_en c on
          b.id_label_en=c.id_label_en inner join
          www.document_label_es d on
          a.id_document=d.id_document inner join
          www.label_es e on
          d.id_label_es=e.id_label_es inner join
          www.author f on
          a.id_document=f.id_document"""

        if search!=None:
            docs+="""
              where
                a.title_en ilike '%{}%' or
                a.title_es ilike '%{}%' or
                a.theme_en ilike '%{}%' or
                a.theme_es ilike '%{}%' or
                a.description_en ilike '%{}%' or
                a.description_es ilike '%{}%' or
                c.label ilike '%{}%' or
                e.label ilike '%{}%' or
                f.name ilike '%{}%' or
                f.twitter_user ilike '%{}%'""". \
            format(search,search,search,search,search,search,search,search,search,search)

        docs+="""
        )
        select count(id_document) as c
        from count;"""

        return self.query(docs).row()["c"]
               

    def getDocumentCatalog(self, offset, listSize, lang, search=None):
        """Gets list of documents."""
        a = """
        with label_en as(
          select
            a.id_document as id_document,
            array_agg(b.label) as labels
          from
            www.document_label_en a
            inner join www.label_en b
            on a.id_label_en=b.id_label_en
          group by id_document),
        label_es as(
          select
            a.id_document as id_document,
            array_agg(b.label) as labels
          from
            www.document_label_es a
            inner join www.label_es b
            on a.id_label_es=b.id_label_es
          group by id_document),
        authors as(
          select
            id_document as id_document,
            array_agg(coalesce(twitter_user, name)) as author
          from www.author
          group by id_document),
        docs as(
          select
            a.id_document,"""

        if lang=="es":
            a+="""
            coalesce(title_es, title_en) as title, 
            coalesce(theme_es, theme_en) as theme, """
        else:
            a+="""
            coalesce(title_en, title_es) as title, 
            coalesce(theme_en, theme_es) as theme, """

        a+="""
            a.last_edit_time as time
          from www.document a
        ),
        selection as (
          select distinct a.id_document
          from
            www.document a inner join
            www.document_label_en b on
            a.id_document=b.id_document inner join
            www.label_en c on
            b.id_label_en=c.id_label_en inner join
            www.document_label_es d on
            a.id_document=d.id_document inner join
            www.label_es e on
            d.id_label_es=e.id_label_es inner join
            www.author f on
            a.id_document=f.id_document"""

        if search!=None:
            a+="""
              where
                a.title_en ilike '%{}%' or
                a.title_es ilike '%{}%' or
                a.theme_en ilike '%{}%' or
                a.theme_es ilike '%{}%' or
                a.description_en ilike '%{}%' or
                a.description_es ilike '%{}%' or
                c.label ilike '%{}%' or
                e.label ilike '%{}%' or
                f.name ilike '%{}%' or
                f.twitter_user ilike '%{}%'""". \
            format(search,search,search,search,search,search,search,search,search,search)

        a+="""
        )
        select
          a.id_document as id,
          a.title as title,
          a.theme as theme,  
          a.time as time,
          b.labels as labels,
          d.author as authors
        from
          docs a inner join 
          label_{} b on
          a.id_document=b.id_document inner join
          authors d on
          a.id_document=d.id_document
        where
          a.id_document in (select * from selection);""".format(lang)

        return self.query(a).result()


    def countries(self, lang, year):
        """Returns the list of geopolitical blocks and its countries for a language and a year."""
        a = """
        select
          a.id_country,
          b.full_name_{} as country_name,
          f.full_name_{} as block_name
        from
          iepg_data.iepg_final_data a 
          inner join iepg_data.master_country b
          on a.id_country=b.id_master_country
          inner join iepg_data.country_relation c
          on a.id_country=c.id_child
          inner join iepg_data.master_country d
          on c.id_parent=d.id_master_country
          inner join iepg_data.country_relation e
          on d.id_master_country=e.id_child
          inner join iepg_data.master_country f
          on e.id_parent=f.id_master_country
        where
          date_part('year', a.date_in+(365/2))={}
        order by f.full_name_{}, b.full_name_{};""".format(lang,lang,year,lang,lang)

        return(self.query(a).result())

    def years(self):
        """Returns the years of IEPG data stored in the database."""
        a = """
        select distinct date_part('year', (date_in+(365/2)))::varchar as year 
        from iepg_data.iepg_final_data order by year desc;"""

        return(self.query(a).result())


    def newStuff(self, lang, section=None):
        """Access news for the home's new stuff control."""
        if section in ["Blog", "Media", "Events"]:
            a = """
            with a as(
              select
                a.id_new::integer as id,
                array[(b.name || ' ' || b.surname)]::varchar[] as wwwuser,
                new_time::timestamp as time,
                title_{}::varchar as title,
                description_{}::varchar as section,
                array_agg(label)::varchar[] as label
              from
                www.new a inner join www.wwwuser b
                on a.id_wwwuser=b.id_wwwuser
                inner join www.news_section c
                on a.id_news_section=c.id_news_section
                left join www.new_label_{} d 
                on a.id_new=d.id_new
                left join www.label_{} e
                on d.id_label_{}=e.id_label_{}
              group by id, b.name, b.surname, time, title, section
            ) 
            select
              id as id_new_stuff,
              gs__uniquearray(wwwuser) as wwwuser,
              time,
              title,
              section,
              gs__uniquearray(label) as label
            from a
              where section='{}'
            order by time desc
            limit 5;
            """.format(lang,lang,lang,lang,lang,lang,section)
        elif section=="Documents":
            a = """
            with a as(
              select
                a.id_document::integer as id,
                array_agg(case when (b.name is null)
                  then b.twitter_user
                  else b.name
                  end)::varchar[] as wwwuser,
                last_edit_time::timestamp as time,
                title_{}::varchar as title,
                'Document'::varchar as section,
                array_agg(d.label)::varchar[] as label
              from
                www.document a inner join www.author b
                on a.id_document=b.id_document
                left join www.document_label_{} c
                on a.id_document=c.id_document
                left join www.label_{} d
                on c.id_label_{}=d.id_label_{}
              group by id, title, section
            ) 
            select
              id as id_new_stuff,
              gs__uniquearray(wwwuser) as wwwuser,
              time,
              title,
              section,
              gs__uniquearray(label) as label
            from a
            order by time desc
            limit 5;
            """.format(lang,lang,lang,lang,lang)
        else:
            a = """
            with a as(
              select
                a.id_new::integer as id,
                array[(b.name || ' ' || b.surname)]::varchar[] as wwwuser,
                new_time::timestamp as time,
                title_en::varchar as title,
                description_en::varchar as section,
                array_agg(label)::varchar[] as label
              from
                www.new a inner join www.wwwuser b
                on a.id_wwwuser=b.id_wwwuser
                inner join www.news_section c
                on a.id_news_section=c.id_news_section
                left join www.new_label_en d 
                on a.id_new=d.id_new
                left join www.label_en e
                on d.id_label_en=e.id_label_en
              group by id, b.name, b.surname, time, title, section
              union
              select
                a.id_document::integer as id,
                array_agg(case when (b.name is null)
                  then b.twitter_user
                  else b.name
                  end)::varchar[] as wwwuser,
                last_edit_time::timestamp as time,
                title_en::varchar as title,
                'Document'::varchar as section,
                array_agg(d.label)::varchar[] as label
              from
                www.document a inner join www.author b
                on a.id_document=b.id_document
                left join www.document_label_en c
                on a.id_document=c.id_document
                left join www.label_en d
                on c.id_label_en=d.id_label_en
              group by id, title, section
            ) 
            select
              id as id_new_stuff,
              gs__uniquearray(wwwuser) as wwwuser,
              time,
              title,
              section,
              gs__uniquearray(label) as label
            from a
            order by time desc
            limit 5;
            """.format(lang,lang,lang,lang,lang,lang,lang,lang,lang,lang,lang)

        return(self.query(a).result())
