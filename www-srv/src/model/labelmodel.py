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


    def insertLabel(self, label, lang):
        """Inserts a label."""
        dv = DataValidator()
        dv.checkLang(lang)
        sql = "select id_label_{} as id from www.label_{} where label=%s;".format(lang, lang)
        id = self.query(sql, bindings=[label]).row()
        if id:
            return(id["id"])
        else:
            return(self.insert("www.label_{}".format(lang), {"label": label}, "id_label_{}".format(lang)))
