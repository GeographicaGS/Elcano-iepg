# coding=UTF8

"""

Home page model.

TODO: check all select * and state the fields.
TODO: review SQL parsing. Use bindings.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
from helpers import DataValidator
from datetime import datetime
from psycopg2 import IntegrityError


class HomeModel(PostgreSQLModel):
    """Home model."""
    def newEmail(self, email):
        """Inserts a new email into the mailing list."""
        try:
            out = self.insert("www.email_list",
                              {"email": email,
                               "time": datetime.utcnow().isoformat()},
                              returnID="email")
        
            return(out)
        except IntegrityError as e:
            return({"error": "duplicated email"})
        

    def newStuffSections(self, lang, section):
        """Access new for the home's new stuff control for Blog, Media, and Events."""
        dv = DataValidator()
        dv.checkLang(lang)
        dv.checkNewsSection(section)

        a = """
        with a as(
        select
        a.id_new::integer as id,
        (b.name || ' ' || b.surname)::varchar as wwwuser,
        publishing_date::date as time,
        title_{} as title,
        a.id_news_section as id_section,
        description_{}::varchar as section,
        a.url_{} as link,
        array_agg(d.id_label_{})::varchar[] as labels
        from
        www.new a inner join www.wwwuser b
        on a.id_wwwuser=b.id_wwwuser
        inner join www.news_section c
        on a.id_news_section=c.id_news_section
        left join www.new_label_{} d 
        on a.id_new=d.id_new
        left join www.label_{} e
        on d.id_label_{}=e.id_label_{}
        where a.published
        group by id, b.name, b.surname, time, title, id_section, section
        ) 
        select
        id as id_item,
        wwwuser,
        time,
        title,
        link,
        section,
        labels
        from a
        where id_section={}
        order by time desc
        limit 5;
        """.format(lang,lang,lang,lang,lang,lang,lang,lang,section)
        return(self.query(a).result())


    def newStuffDocuments(self, lang):
        """Gets new documents for the home's new stuff control for Documents."""
        dv = DataValidator()
        dv.checkLang(lang)

        a = """
        with a as(
        select
        a.id_document::integer as id,
        (b.name || ' ' || b.surname)::varchar as wwwuser,
        null as link,
        publishing_date::date as time,
        title_{} as title,
        '{}'::varchar as section,
        array_agg(d.id_label_{})::varchar[] as labels
        from
        www.document a inner join www.wwwuser b
        on a.last_edit_id_user=b.id_wwwuser
        left join www.document_label_{} d 
        on a.id_document=d.id_document
        left join www.label_{} e
        on d.id_label_{}=e.id_label_{}
        where a.published
        group by id, b.name, b.surname, time, title, section
        ) 
        select
        id as id_item,
        wwwuser,
        time,
        title,
        link,
        section,
        labels
        from a
        order by time desc
        limit 5;
        """.format(lang,
                   "Documents" if lang=='en' else "Documentos",
                   lang,lang,lang,lang,lang)

        return(self.query(a).result())


    def newStuffAll(self, lang):
        """Gets new stuff for all sections except Twitter."""
        dv = DataValidator()
        dv.checkLang(lang)

        sql = """
        with a as(
        select * from(
        select
        a.id_new::integer as id,
        (b.name || ' ' || b.surname)::varchar as wwwuser,
        publishing_date::date as time,
        a.url_{} as link,
        title_{} as title,
        description_{}::varchar as section,
        array_agg(d.id_label_{})::varchar[] as labels
        from
        www.new a inner join www.wwwuser b
        on a.id_wwwuser=b.id_wwwuser
        inner join www.news_section c
        on a.id_news_section=c.id_news_section
        left join www.new_label_{} d 
        on a.id_new=d.id_new
        left join www.label_{} e
        on d.id_label_{}=e.id_label_{}
        where a.published
        group by id, b.name, b.surname, time, title, section
        union
        select
        a.id_document::integer as id,
        (b.name || ' ' || b.surname) as wwwuser,
        publishing_date::date as time,
        null as link,
        title_{} as title,
        '{}'::varchar as section,
        array_agg(d.id_label_{})::varchar[] as labels
        from
        www.document a inner join www.wwwuser b
        on a.last_edit_id_user=b.id_wwwuser
        left join www.document_label_{} d 
        on a.id_document=d.id_document
        left join www.label_{} e
        on d.id_label_{}=e.id_label_{}
        where a.published
        group by id, b.name, b.surname, time, title, section) ab
        order by time desc)
        select
        id as id_item,
        wwwuser,
        time,
        title,
        link,
        section,
        labels
        from a
        limit 5;""".format(lang,lang,lang,lang,lang,lang,lang,lang,lang,
                           "Documents" if lang=='en' else "Documentos",
                           lang,lang,lang,lang,lang)

        return(self.query(sql).result())


    def countryList(self, lang):
        """Gets the list of IEPG countries alphabetically ordered."""
        dv = DataValidator()
        dv.checkLang(lang)

        sql = """
        select distinct
        a.short_name_{}1 as country_name
        from
        iepg_data.master_country a inner join
        iepg_data.iepg_final_data b on
        a.id_master_country=b.id_master_country
        where
        a.id_master_country<>'eu900'
        order by
        a.short_name_{}1;""".format(lang,lang)

        return(self.query(sql).result())

