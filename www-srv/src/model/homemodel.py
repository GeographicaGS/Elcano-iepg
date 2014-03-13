# coding=UTF8

"""

Home page model.

TODO: check all select * and state the fields.
TODO: review SQL parsing. Use bindings.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel


class HomeModel(PostgreSQLModel):
    """Home model."""
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
