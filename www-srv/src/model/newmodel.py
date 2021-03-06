# coding=UTF8

"""

New model

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
from flask import session
from helpers import DataValidator
import datetime

class NewModel(PostgreSQLModel):
    """New's model."""
    def filterByLabels(self, lang, labels):
        """Gets the list of news ID whose labels ID includes the target one."""
        DataValidator().checkLang(lang)
        DataValidator().checkIntList(labels.split(","))

        sql = """
        with a as(
        select
        a.id_new as id,
        gs__uniquearray(array_agg(id_label_{})::int[]) as labels
        from
        www.new a inner join
        www.new_label_{} b on
        a.id_new=b.id_new
        where published
        group by
        id
        )
        select
        gs__uniquearray(array_agg(id)::int[]) as id
        from a
        where
        array[""".format(lang,lang)+labels+"""]::int[] <@ labels;"""

        m = self.query(sql).row()["id"]
        return(set(m) if m!=None else set([]))


    def getNewsSections(self, lang):
        """Returns the sections of news in lang."""
        DataValidator().checkLang(lang)
        sql = """
        select
        id_news_section as id,
        description_{}
        from
        www.news_section;
        """.format(lang)
        return(self.query(sql).result())


    def createNew(self, title_en, title_es, text_en, text_es, url_en, url_es, news_section, \
                  labels_en, labels_es, time):
        """Create new."""
        id = self.insert("www.new",
                         {"title_en": title_en,
                          "title_es": title_es,
                          "text_en": text_en,
                          "text_es": text_es,
                          "url_en": url_en,
                          "url_es": url_es,
                          "id_wwwuser": session["id_user"],
                          "new_time": datetime.datetime.utcnow().isoformat(),
                          "id_news_section": news_section,
                          "published": False,
                          "publishing_date": time},
                         returnID="id_new")

        if labels_en:
            for label in labels_en:
                self.__attachLabel(label, id, "en")
        if labels_es:
            for label in labels_es:
                self.__attachLabel(label, id, "es")
        
        return(id)


    def editNew(self, id_new, title_en, title_es, text_en, text_es, url_en, url_es, news_section, \
                  labels_en, labels_es, time):
        """Edits new."""
        self.update("www.new",
                    {"title_en": title_en,
                     "title_es": title_es,
                     "text_en": text_en,
                     "text_es": text_es,
                     "url_en": url_en,
                     "url_es": url_es,
                     "id_wwwuser": session["id_user"],
                     "new_time": datetime.datetime.utcnow().isoformat(),
                     "id_news_section": news_section,
                     "publishing_date": time},
                    {"id_new": id_new})

        self.__detachLabels(id_new, "en")
        self.__detachLabels(id_new, "es")

        if labels_en:
            for label in labels_en:
                self.__attachLabel(label["id"], id_new, "en")
        if labels_es:
            for label in labels_es:
                self.__attachLabel(label["id"], id_new, "es")
        
        return(id_new)


    def deleteNew(self, id_new):
        """Deletes a new."""
        self.__detachLabels(id_new, "en")
        self.__detachLabels(id_new, "es")

        sql = "delete from www.new where id_new=%s;"
        self.queryCommit(sql, bindings=[id_new])
        return(id_new)


    def togglePublish(self, id_new):
        """Toggles published status of a new."""
        try:
            q = """
            select published from www.new
            where id_new=%s;"""
            status = self.query(q, bindings=[id_new]).row()["published"]
        
            self.update("www.new",
                        {"published": not status},
                        {"id_new": id_new})
            return not status
        except:
            return None

    
    def searchNewsByFeatures(self, search, published):
        """Returns a set with the ID of news that satisfies the search
        criteria on text, and title."""
        DataValidator().checkBoolean(published)
        sql = """
        with a as(
        select
        id_new,
        published,
        publishing_date
        from
        www.new
        where
        """
        if published:
            sql+="""
            published and
            """
        bi = []
        for s in search.split(","):
            sql += """
            (title_en ilike %s or
            text_en ilike %s or 
            title_es ilike %s or
            text_es ilike %s) and
            """
            bi.extend(["%"+s+"%", "%"+s+"%", "%"+s+"%", "%"+s+"%"])

        sql = sql.rstrip(" and\n")+")"
        sql += """
        select
        array_agg(id_new) as ids
        from
        a;"""

        m = self.query(sql, bi).row()["ids"]
        if m:
            return(set(m))
        else:
            return(set([]))


    def searchNewsByLabel(self, search, published):
        """Returns a set with the ID of news that satisfies the search criteria on labels."""
        sql = """
        with a as(
        select
        a.id_new as id_new,
        a.published as published,
        a.publishing_date as publishing_date,
        d.label as label_en,
        e.label as label_es
        from
        www.new a inner join 
        www.new_label_en b on
        a.id_new=b.id_new inner join
        www.new_label_es c on
        a.id_new=c.id_new inner join
        www.label_en d on
        b.id_label_en=d.id_label_en inner join
        www.label_es e on
        c.id_label_es=e.id_label_es
        """
        if published:
            sql+="""
            where published)
            """
        else:
            sql+=")"

        sql+="""
        select
        array_agg(id_new) as ids
        from a
        where
        """
        bi = []
        for s in search.split(","):
            sql += """
            label_en ilike %s or
            label_es ilike %s or
            """
            bi.extend(["%"+s+"%","%"+s+"%"])

        sql = sql.rstrip(" or\n")+";"
        m = self.query(sql, bi).row()["ids"]
        if m:
            return(set(m))
        else:
            return(set([]))


    def getNewDetails(self, idNew):
        """Returns details of a new by ID."""
        sql = """
        select
        id_new as id,
        a.id_wwwuser,
        c.name as username,
        c.surname as usersurname,
        c.email as useremail,
        c.username as userusername,
        new_time,
        title_en,
        title_es,
        text_en,
        text_es,
        url_en,
        url_es,
        a.id_news_section,
        b.description_en as section_en,
        b.description_es as section_es,
        published,
        publishing_date
        from
        www.new a inner join
        www.news_section b on 
        a.id_news_section=b.id_news_section inner join 
        www.wwwuser c on
        a.id_wwwuser=c.id_wwwuser
        where id_new=%s;
        """
        return(self.query(sql, [idNew]).row())


    def getLabelsForNew(self, idNew, lang):
        """Returns the labels for new idNew and language lang."""
        DataValidator().checkLang(lang)
        sql = """
        select
        b.id_label_{} as id,
        b.label
        from
        www.new_label_{} a inner join
        www.label_{} b on
        a.id_label_{}=b.id_label_{}
        where id_new=%s;
        """.format(lang,lang,lang,lang,lang)
        return(self.query(sql, [idNew]).result())


    def __attachLabel(self, id_label, id_new, lang):
        """Attach a label to a new."""
        sql = self.insert("www.new_label_{}".format(lang),
                        {"id_new": id_new,
                         "id_label_{}".format(lang): id_label})


    def __detachLabels(self, id_new, lang):
        """Detaches all labels from a new."""
        sql = "delete from www.new_label_{} where id_new=%s;".format(lang)
        self.queryCommit(sql, bindings=[id_new])
