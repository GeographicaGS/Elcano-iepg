# coding=UTF8

"""

Highlight model

"""

from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
import datetime
from flask import session
from helpers import DataValidator


class HighlightModel(PostgreSQLModel):
    """Highlight model."""
    def getHighlightCatalogBackend(self, published, page=None, listSize=None, search=None):
        """Gets the highlight catalog, active or inactive"""
        sql = """
        select count(id_highlight) as c
        from www.highlight
        """

        if published:
            sql += """
            where published
            """
        else:
            sql += """
            where not published
            """

        if search:
            search = '%'+search+'%'
            sql += """
            and (
            title_en ilike %s or
            title_es ilike %s or
            text_en ilike %s or
            text_es ilike %s or
            image_name_en ilike %s or
            image_name_es ilike %s or
            credit_img_en ilike %s or
            credit_img_es ilike %s)"""

        sql += ";"

        if search:
            count = self.query(sql, bindings=[search,search,search,search,search,search,search,search]).row()["c"]
        else:
            count = self.query(sql).row()["c"]

        sql = """
        select
          id_highlight,
          coalesce(title_es,title_en) as title,
          coalesce(text_es, text_en) as text,
          title_en,
          title_es,
          text_en,
          text_es,
          image_hash_en,
          image_hash_es,
          last_edit_time,
          link_en,
          link_es
        from
          www.highlight
        """

        if published:
            sql += """
            where published
            """
        else:
            sql += """
            where not published
            """

        if search:
            search = '%'+search+'%'
            sql += """
            and (
            title_en ilike %s or
            title_es ilike %s or
            text_en ilike %s or
            text_es ilike %s or
            image_name_en ilike %s or
            image_name_es ilike %s or
            credit_img_en ilike %s or
            credit_img_es ilike %s)"""

        sql += """
        order by last_edit_time desc
        """

        if page and listSize:
            sql += """
            offset %s limit %s
            """

        sql += ";"

        if search:
            if page and listSize:
                results = self.query(sql, bindings=[search,search,search, \
                                                    search,search,search,search, \
                                                    search,(int(page)*listSize),listSize]).result()
            else:
                results = self.query(sql, bindings=[search,search,search, \
                                                    search,search,search,search, \
                                                    search]).result()
        else:
            if page and listSize:
                results = self.query(sql, bindings=[(int(page)*listSize),listSize]).result()
            else:
                results = self.query(sql).result()

        return(count, results)


    def setHighlightOrder(self, order):
        """Set order among the published highlights."""
        try:
            for index,value in enumerate(order):
                self.update("www.highlight",
                            {"publication_order": index},
                            {"id_highlight": value})
            return True
        except:
            return False


    def togglePublishHighlight(self, id):
        """Toggles the published status a highlight."""
        a = """
        select
          published
        from
          www.highlight
        where
          id_highlight=%s;"""
        pub = self.query(a, bindings=[id]).row()["published"]

        a = """
        select
        max(publication_order)
        from
        www.highlight;
        """
        max = self.query(a).row()["max"]
        max = int(max+1) if max!=None else 0
        if pub:
            self.update("www.highlight",
                        {"published": False,
                         "publication_order": None},
                        {"id_highlight": id})
        else:
            self.update("www.highlight",
                        {"published": True,
                         "publication_order": max},
                        {"id_highlight": id})
        return(not pub)


    def createHighlight(self, data):
        """Creates a new highlight."""
        a = self.insert("www.highlight",
                        {"title_en": data["title_en"],
                         "title_es": data["title_es"],
                         "text_en": data["text_en"],
                         "text_es": data["text_es"],
                         "image_name_en": data["image_name_en"],
                         "image_hash_en": data["image_hash_en"],
                         "image_name_es": data["image_name_es"],
                         "image_hash_es": data["image_hash_es"],
                         "credit_img_en": data["credit_img_en"],
                         "credit_img_es": data["credit_img_es"],
                         "link_en": data["link_en"],
                         "link_es": data["link_es"],
                         "last_edit_id_user": session["id_user"],
                         "last_edit_time": datetime.datetime.utcnow().isoformat(),
                         "published": "False",
                         "publication_order": None},
                        returnID="id_highlight")

        return a


    def editHighlight(self, data):
        """Edits a highlight."""
        self.update("www.highlight",
                    {"title_en": data["title_en"],
                     "title_es": data["title_es"],
                     "text_en": data["text_en"],
                     "text_es": data["text_es"],
                     "credit_img_en": data["credit_img_en"],
                     "credit_img_es": data["credit_img_es"],
                     "link_en": data["link_en"],
                     "link_es": data["link_es"],
                     "image_name_en": data["image_name_en"],
                     "image_hash_en": data["image_hash_en"],
                     "image_name_es": data["image_name_es"],
                     "image_hash_es": data["image_hash_es"],
                     "last_edit_id_user": session["id_user"],
                     "last_edit_time": datetime.datetime.utcnow().isoformat()},
                    {"id_highlight": data["id_highlight"]})

        return data["id_highlight"]


    def getHighlight(self, id_highlight):
        """Gets highlight full data."""
        q = "select * from www.highlight where id_highlight=%s"
        return(self.query(q, bindings=[id_highlight]).row())


    def getSliderFrontend(self, lang):
        """Get the slider's data in language lang for the home, active and ordered.
        """
        dv = DataValidator()
        dv.checkLang(lang)
        sql = """
        select
        id_highlight,
        title_{} as title,
        text_{} as text,
        image_hash_{} as image_file,
        credit_img_{} as credit_img,
        link_{} as link,
        published,
        publication_order
        from
        www.highlight
        where
        published and publication_order is not null
        order by
        publication_order;
        """.format(lang,lang,lang,lang,lang)

        return(self.query(sql).result())


    def deleteHighlight(self, idHighlight):
        """Deletes a highlight by ID."""
        sql = "delete from www.highlight where id_highlight=%s"

        self.queryCommit(sql, bindings=[idHighlight])
        return(True)
