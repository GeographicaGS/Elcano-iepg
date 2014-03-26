# coding=UTF8

"""
Label model.
"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
from helpers import DataValidator
from psycopg2 import IntegrityError


class LabelModel(PostgreSQLModel):
    """Model for labels."""
    def getLabels(self, lang):
        """Returns labels in the given language."""
        dv = DataValidator()
        dv.checkLang(lang)
        q = "select id_label_{} as id, label from www.label_{};".format(lang, lang)
        return self.query(q).result()


    def insertLabel(self, label, lang="es"):
        """Inserts a label."""
        dv = DataValidator()
        dv.checkLang(lang)
        try:
            return self.insert("www.label_{}".format(lang), {"label": label}, "id_label_{}".format(lang))
        except IntegrityError as e:
            return({"error": "Duplicated label"})

