"""

Document model

"""

from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
import datetime
from flask import session


class DocumentModel(PostgreSQLModel):
    """Modelo de documento."""

    def createDocument(self, data):
        """Creates a new document."""
        a = self.insert("www.document", 
                        {"title_en": data["title_en"],
                         "title_es": data["title_es"],
                         "theme_en": data["theme_en"],
                         "theme_es": data["theme_es"],
                         "description_en": data["description_en"],
                         "description_es": data["description_es"],
                         "last_edit_time": datetime.datetime.now().isoformat(),
                         # "last_edit_id_user": session["id_user"]},
                         "last_edit_id_user": "1",
                         "link_en": data["link_en"],
                         "link_es": data["link_es"]},
                        returnID="id_document")

        for label_en in data["labels_en"]:
            self.__attachLabel(label_en["id"], a, "en")

        for label_es in data["labels_es"]:
            self.__attachLabel(label_es["id"], a, "es")

        for author in data["authors"]:
            self.__createAuthor(author, a)

        for pdf in data["pdfs_es"]:
            self.__createPdf("es", pdf["name"], pdf["hash"], a)

        for pdf in data["pdfs_en"]:
            self.__createPdf("en", pdf["name"], pdf["hash"], a)

        return a


    def __createPdf(self, lang, name, hash, id_document):
        """Creates a PDF document and attaches it to a document."""
        self.insert("www.pdf",
                    {"id_document": id_document,
                     "lang": lang,
                     "pdf_name": name,
                     "hash": hash})


    def editDocument(self, data):
        """Edits a document."""
        self.update("www.document", 
                    {"title_en": data["title_en"],
                     "title_es": data["title_es"],
                     "theme_en": data["theme_en"],
                     "theme_es": data["theme_es"],
                     "description_en": data["description_en"],
                     "description_es": data["description_es"],
                     "last_edit_time": datetime.datetime.now().isoformat(),
                     # "last_edit_id_user": session["id_user"]},
                     "last_edit_id_user": "1",
                     "link_en": data["link_en"],
                     "link_es": data["link_es"]},
                    {"id_document": data["id_document"]})

        q = "delete from www.author where id_document=%s"
        self.query(q, data["id_document"])

        q = "delete from www.document_label_en where id_document=%s"
        self.query(q, data["id_document"])

        q = "delete from www.document_label_es where id_document=%s"
        self.query(q, data["id_document"])

        q = "delete from www.pdf where id_document=%s"
        self.query(q, data["id_document"])

        for label_en in data["labels_en"]:
            self.__attachLabel(label_en["id"], data["id_document"], "en")

        for label_es in data["labels_es"]:
            self.__attachLabel(label_es["id"], data["id_document"], "es")

        for author in data["authors"]:
            self.__createAuthor(author, data["id_document"])

        for pdf in data["pdfs_es"]:
            self.__createPdf("es", pdf["name"], pdf["hash"], data["id_document"])

        for pdf in data["pdfs_en"]:
            self.__createPdf("en", pdf["name"], pdf["hash"], data["id_document"])

        return data["id_document"]


    def deleteDocument(self, data):
        """Deletes a document."""
        q = "delete from www.author where id_document=%s"
        self.queryCommit(q, data["id_document"])

        q = "delete from www.document_label_en where id_document=%s"
        self.queryCommit(q, data["id_document"])

        q = "delete from www.document_label_es where id_document=%s"
        self.queryCommit(q, data["id_document"])

        q = "delete from www.pdf where id_document=%s"
        self.queryCommit(q, data["id_document"])

        q = "delete from www.document where id_document=%s"
        self.queryCommit(q, data["id_document"])

        return data["id_document"]


    def getDocumentList(self, data, listSize):
        """Gets list of documents."""
        q = "select id_document as id, coalesce(title_es, title_en) as title, "+ \
            "last_edit_time as time, "+ \
            "published from www.document "+ \
            "order by "+data["orderbyfield"]+" "+data["orderbyorder"]+" "+ \
            "offset "+str(int(data["offset"])*listSize)+" "+ \
            "limit "+str(listSize)+";"

        print(q)

        # print(self.query(q).result)
#            print(r)           


        return q
        


    def __attachLabel(self, id_label, id_document, language):
        self.insert("www.document_label_"+language,
                    {"id_document": id_document,
                     "id_label_"+language: id_label})


    def __createAuthor(self, data, id_document):
        self.insert("www.author",
                    {"id_document": id_document,
                     "twitter_user": data})
