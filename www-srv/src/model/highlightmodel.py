# coding=UTF8

"""

Highlight model

"""

from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
import datetime
from flask import session
import ipdb


class HighlightModel(PostgreSQLModel):
    """Highlight model."""

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


    def getActiveHighlight(self, lang):
        """Returns the list of active highlights, ordered."""
        # a =
        pass

    
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

        if pub:
            self.update("www.highlight",
                        {"published": False,
                         "publication_order": None},
                        {"id_highlight": id})
        else:
            self.update("www.highlight",
                        {"published": True,
                         "publication_order": None},
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
                     "image_name_en": data["new_image_name_en"],
                     "image_hash_en": data["new_image_hash_en"],
                     "image_name_es": data["new_image_name_es"],
                     "image_hash_es": data["new_image_hash_es"],
                     "last_edit_id_user": session["id_user"],
                     "last_edit_time": datetime.datetime.utcnow().isoformat(),
                     "published": data["published"]},
                    {"id_highlight": data["id_highlight"]})

        return data["id_highlight"]


    def getHighlight(self, id_highlight):
        """Gets highlight data."""
        q = "select * from www.highlight where id_highlight=%s"
        return(self.query(q, id_highlight).row())
