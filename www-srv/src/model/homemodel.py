# coding=UTF8

"""

Home page model.

TODO: check all select * and state the fields.
TODO: review SQL parsing. Use bindings.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel


class HomeModel(PostgreSQLModel):
    """Home model."""
    def getLabels(self, lang):
        """Gets labels in one language."""
        sql = """
        select
          id_label_{} as id,
          label
        from
          www.label_{};
        """.format(lang, lang)

        return(self.query(sql).result())

    def newStuffSections(self, lang, section):
        """Access new for the home's new stuff control for Blog, Media, and Events."""
        a = """
        with a as(
        select
        a.id_new::integer as id,
        array[(b.name || ' ' || b.surname)]::varchar[] as wwwuser,
        new_time::timestamp as time,
        title_{} as title,
        description_{}::varchar as section,
        array_agg(d.id_label_{})::varchar[] as label
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
        limit 5
        ) 
        select
        row_number() over (order by time) as id,
        wwwuser,
        time,
        title,
        section,
        label
        from a
        where section='{}'
        order by time desc;
        """.format(lang,lang,lang,lang,lang,lang,lang,section)
    
        return(self.query(a).result())


    def newStuffDocuments(self, lang):
        """Gets new documents for the home's new stuff control for Documents."""
        a = """
        with a as(
        select
        a.id_document::integer as id,
        array[(b.name || ' ' || b.surname)]::varchar[] as wwwuser,
        last_edit_time::timestamp as time,
        title_{} as title,
        'Documents'::varchar as section,
        array_agg(d.id_label_{})::varchar[] as label
        from
        www.document a inner join www.wwwuser b
        on a.last_edit_id_user=b.id_wwwuser
        left join www.document_label_{} d 
        on a.id_document=d.id_document
        left join www.label_{} e
        on d.id_label_{}=e.id_label_{}
        group by id, b.name, b.surname, time, title, section
        limit 5
        ) 
        select
        row_number() over (order by time) as id,
        wwwuser,
        time,
        title,
        section,
        label
        from a
        order by time desc;
        """.format(lang,lang,lang,lang,lang,lang)

        return(self.query(a).result())


    def newStuffAll(self, lang):
        """Gets new stuff for all sections except Twitter."""
        sql = """
        with a as(
        select * from(
        select
        a.id_new::integer as id,
        array[(b.name || ' ' || b.surname)]::varchar[] as wwwuser,
        new_time::timestamp as time,
        title_{} as title,
        description_{}::varchar as section,
        array_agg(d.id_label_{})::varchar[] as label
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
        union
        select
        a.id_document::integer as id,
        array[(b.name || ' ' || b.surname)]::varchar[] as wwwuser,
        last_edit_time::timestamp as time,
        title_{} as title,
        'Documents'::varchar as section,
        array_agg(d.id_label_{})::varchar[] as label
        from
        www.document a inner join www.wwwuser b
        on a.last_edit_id_user=b.id_wwwuser
        left join www.document_label_{} d 
        on a.id_document=d.id_document
        left join www.label_{} e
        on d.id_label_{}=e.id_label_{}
        group by id, b.name, b.surname, time, title, section) ab
        order by time desc
        limit 5)
        select
        row_number() over (order by time) as id,
        wwwuser,
        time,
        title,
        section,
        label
        from a;""".format(lang,lang,lang,lang,lang,lang,lang,lang,lang,lang,lang,lang,lang)

        return(self.query(sql).result())
