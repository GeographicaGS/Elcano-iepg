# coding=UTF8

"""

Document model

TODO: check all select * and state the fields.
TODO: check for SQL injection.

"""

from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
import datetime
from flask import session
from helpers import DataValidator


class DocumentModel(PostgreSQLModel):
    """Modelo de documento."""
    def getDocumentData(self, idDocument):
        """Gets the document full data."""
        doc = "select * from www.document where id_document=%s"
        return(self.query(doc, bindings=[idDocument]).row())


    # def getDocumentCatalogSize(self, search=None):
    #     """Gets the total size of a list of document for the frontend."""
    #     docs = """
    #     with count as(
    #     select distinct a.id_document
    #     from
    #       www.document a inner join
    #       www.document_label_en b on
    #       a.id_document=b.id_document inner join
    #       www.label_en c on
    #       b.id_label_en=c.id_label_en inner join
    #       www.document_label_es d on
    #       a.id_document=d.id_document inner join
    #       www.label_es e on
    #       d.id_label_es=e.id_label_es inner join
    #       www.author f on
    #       a.id_document=f.id_document"""

    #     if search:
    #         search = "%"+search+"%"
    #         docs+="""
    #           where
    #             a.title_en ilike %s or
    #             a.title_es ilike %s or
    #             a.theme_en ilike %s or
    #             a.theme_es ilike %s or
    #             a.description_en ilike %s or
    #             a.description_es ilike %s or
    #             c.label ilike %s or
    #             e.label ilike %s or
    #             f.name ilike %s or
    #             f.twitter_user ilike %s"""

    #     docs+="""
    #     )
    #     select count(id_document) as c
    #     from count;"""

    #     if search:
    #         return self.query(docs, bindings=[ \
    #                                            search, search, search, search, search, \
    #                                            search, search, search, search, search]).row()["c"]
    #     else:
    #         return self.query(docs).row()["c"]


    def searchInLabels(self, lang, search):
        """Returns ID of documents attached to a given label expressed in search."""
        dv = DataValidator()
        dv.checkLang(lang)

        sql = """
        select
        gs__uniquearray(array_agg(dl.id_document)::int[]) as id_document
        from
        www.document_label_{} dl inner join
        www.label_{} l on dl.id_label_{}=l.id_label_{}
        where
        """.format(lang,lang,lang,lang)

        bi = []
        for i in search.split(","):
            sql += "label ilike %s or "
            bi.append("%"+i+"%")

        sql = sql.rstrip(" or ")+";"
        return(self.query(sql, bindings=bi).row())


    def searchInAuthors(self, search):
        """Gets the list of documents ID on a search by author name and Twitter user."""
        sql = """
        select gs__uniquearray(array_agg(id_document)::int[]) as id_document
        from
        www.author
        where
        """
        if search is None:
            return None

        bi = []
        for i in search.split(","):
            sql += """
            (name ilike %s or
            twitter_user ilike %s) or
            """
            bi.extend(["%"+i+"%","%"+i+"%"])

        sql = sql.rstrip(" or\n")+";"
        out = self.query(sql, bindings=bi).row()

        if out:
            return(out)
        else:
            return None


    def filterByLabels(self, lang, labels):
        """Gets the list of documents ID whose labels ID includes the target one."""
        dv = DataValidator()
        dv.checkIntList(labels.split(","))
        
        sql = """
        with a as(
        select
        a.id_document as id,
        gs__uniquearray(array_agg(id_label_{})::int[]) as labels
        from
        www.document a inner join
        www.document_label_{} b on
        a.id_document=b.id_document
        group by
        id
        )
        select
        gs__uniquearray(array_agg(id)::int[]) as id_document
        from a
        where
        array[""".format(lang,lang)+labels+"""]::int[] <@ labels;"""

        return(self.query(sql).row())


    def searchInDocument(self, lang, search=None):
        """Gets the list of document ID, optionally with a search in title,
        theme or description."""
        dv = DataValidator()
        dv.checkLang(lang)

        sql = """
        select
          gs__uniquearray(array_agg(id_document)::int[]) as id_document
        from
          www.document
        """

        bi = []
        if search:
            sql += "where"
            for s in search.split(","):
                sql += """
                (title_{} ilike %s or
                theme_{} ilike %s or
                description_{} ilike %s) or
                """.format(lang,lang,lang)
                bi.extend(["%"+s+"%","%"+s+"%","%"+s+"%"])
        
            sql = sql.rstrip(" or\n")

        sql += ";"
        return(self.query(sql, bindings=bi).row())


    def getDocumentDetails(self, lang, idDocument):
        """Gets details of documents for the frontend document catalog by ID."""
        dv = DataValidator()
        dv.checkLang(lang)
        dv.checkNumber(idDocument)

        sql = """
        select
        id_document,
        title_{} as title,
        theme_{} as theme,
        description_{} as description,
        link_{} as link,
        last_edit_id_user,
        last_edit_time,
        published
        from
        www.document
        where
        id_document=%s;""".format(lang,lang,lang,lang)

        return(self.query(sql, bindings=[idDocument]).row())


    def createDocument(self, data):
        """Creates a new document."""
        a = self.insert("www.document", 
                        {"title_en": data["title_en"],
                         "title_es": data["title_es"],
                         "theme_en": data["theme_en"],
                         "theme_es": data["theme_es"],
                         "description_en": data["description_en"],
                         "description_es": data["description_es"],
                         "last_edit_time": datetime.datetime.utcnow().isoformat(),
                         "last_edit_id_user": session["id_user"],
                         "link_en": data["link_en"],
                         "link_es": data["link_es"],
                         "published": "False"},
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


    def deletePdf(self, id_document, hash):
        """Deletes a PDF."""
        q = 'delete from www.pdf where id_document=%s and hash=%s;'
        self.queryCommit(q, [id_document, hash])


    def __createPdf(self, lang, name, hash, id_document):
        """Creates a PDF document and attaches it to a document."""
        self.insert("www.pdf",
                    {"id_document": id_document,
                     "lang": lang,
                     "pdf_name": name,
                     "hash": hash})


    def editDocument(self, id_document, data, newPdfHashEn, newPdfHashEs):
        """Edits a document."""
        self.update("www.document", 
                    {"title_en": data["title_en"],
                     "title_es": data["title_es"],
                     "theme_en": data["theme_en"],
                     "theme_es": data["theme_es"],
                     "description_en": data["description_en"],
                     "description_es": data["description_es"],
                     "last_edit_time": datetime.datetime.now().isoformat(),
                     "last_edit_id_user": session["id_user"],
                     "last_edit_id_user": "1",
                     "link_en": data["link_en"],
                     "link_es": data["link_es"],
                     "published": data["published"]},
                    {"id_document": id_document})

        q = "delete from www.author where id_document=%s"
        self.queryCommit(q, [id_document])

        q = "delete from www.document_label_en where id_document=%s"
        self.queryCommit(q, [id_document])

        q = "delete from www.document_label_es where id_document=%s"
        self.queryCommit(q, [id_document])

        for label_en in data["labels_en"]:
            self.__attachLabel(label_en["id"], id_document, "en")

        for label_es in data["labels_es"]:
            self.__attachLabel(label_es["id"], id_document, "es")

        for author in data["authors"]:
            self.__createAuthor(author, id_document)

        for pdf in data["pdfs_es"]:
            if pdf["hash"] in newPdfHashEs:
                self.__createPdf("es", pdf["name"], pdf["hash"], id_document)

        for pdf in data["pdfs_en"]:
            if pdf["hash"] in newPdfHashEn:
                self.__createPdf("en", pdf["name"], pdf["hash"], id_document)

        return id_document


    def deleteDocument(self, id_document):
        """Deletes a document."""
        q = "delete from www.author where id_document=%s"
        self.queryCommit(q, [id_document])

        q = "delete from www.document_label_en where id_document=%s"
        self.queryCommit(q, [id_document])

        q = "delete from www.document_label_es where id_document=%s"
        self.queryCommit(q, [id_document])

        q = "delete from www.pdf where id_document=%s"
        self.queryCommit(q, [id_document])

        q = "delete from www.document where id_document=%s"
        self.queryCommit(q, [id_document])

        return id_document


    def getDocumentListSize(self, search=None):
        """Gets the total size of a list of document."""
        docs = """select count(*) as c from www.document """

        if search!=None:
            docs += """
            where title_en ilike '%{}%' or title_es ilike '%{}%' or 
            theme_en ilike '%{}%' or theme_es ilike '%{}%' or 
            description_en ilike '%{}%' or description_es ilike '%{}%'
            """.format(search, search, search, search, search, search)

        docs += ";"
        return self.query(docs).row()["c"]
               

    def getDocumentList(self, offset, listSize, search=None, orderByField="title", orderByOrder="asc"):
        """Gets list of documents."""
        docs = """
        select id_document as id, coalesce(title_es, title_en) as title, 
        title_en, title_es, theme_en, theme_es, description_en, description_es, 
        link_en, link_es, last_edit_time as time, published from www.document """
               
        if search:
            search = '%'+search+'%'
            docs += """
            where title_en ilike %s or title_es ilike %s or 
            theme_en ilike %s or theme_es ilike %s or 
            description_en ilike %s or description_es ilike %s
            """

        docs += """
        order by {} {} offset %s limit %s;
        """.format(orderByField, orderByOrder)

        print docs

        if search:
            return self.query(docs, bindings=[ \
                                               search, search, search, search, search, search, \
                                               int(offset)*listSize, \
                                               listSize]).result()
        else:
            return self.query(docs, bindings=[int(offset)*listSize, listSize]).result()


    def getDocumentAuthors(self, id_document):
        """Gets the list of authors of a document."""
        q = "select * from www.author where id_document=%s;"
        return self.query(q, [id_document]).result()

    
    def getPdfData(self, idPdf):
        """Gets data of a PDF."""
        sql = "select * from www.pdf where id_pdf=%s;"
        return(self.query(sql, bindings=[idPdf]).row())


    def getDocumentPdf(self, idDocument, lang=None):
        """Gets the list of PDF of a document, optionally for a given language."""
        dv = DataValidator()

        if lang:
            dv.checkLang(lang)
        dv.checkNumber(idDocument)

        q = "select id_pdf as id, id_document, lang, pdf_name as name, hash from www.pdf where id_document=%s"
        bindings = [idDocument]

        if lang:
            q += " and lang=%s;"
            bindings.append(lang)
        else:
            q += ";"

        return self.query(q, bindings).result()


    def __attachLabel(self, id_label, id_document, language):
        self.insert("www.document_label_"+language,
                    {"id_document": id_document,
                     "id_label_"+language: id_label})


    def __createAuthor(self, data, id_document):
        if "twitter_user" in data:
            self.insert("www.author",
                        {"id_document": id_document,
                         "twitter_user": data["twitter_user"]})
        else:
            self.insert("www.author",
                        {"id_document": id_document,
                         "name": data["name"],
                         "position_en": data["position_en"],
                         "position_es": data["position_es"]})


    def getDocumentBackend(self, id_document):
        """Get Document for the backend."""
        q = "SELECT * FROM www.document WHERE id_document=%s"
        return self.query(q,[id_document]).row()


    def getDocumentLabels(self, idDocument, lang):
        """Get document labels."""
        dv = DataValidator()
        dv.checkLang(lang)
        dv.checkNumber(idDocument)

        q = "SELECT dl.id_label_{} as id_label, l.label FROM www.document_label_{} dl "\
            " INNER JOIN  www.label_{} l ON dl.id_label_{}=l.id_label_{} "\
            " WHERE id_document=%s".format(lang,lang,lang,lang,lang)
        return self.query(q,[idDocument]).result()


    def togglePublish(self, id_document):
        """Toggles the publish status of id_document."""
        try:
            q = """
            select published from www.document
            where id_document=%s;"""

            status = self.query(q, bindings=[id_document]).row()["published"]
        
            self.update("www.document",
                        {"published": not status},
                        {"id_document": id_document})
            return not status
        except:
            return None
