# coding=UTF8

"""

Document model

TODO: check all select * and state the fields.

"""

from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
import datetime
from flask import session


class DocumentModel(PostgreSQLModel):
    """Modelo de documento."""

    def getDocumentFrontend(self, idDocument, lang):
        """Gets the document details for the frontend."""
        doc = """
        with label_en as(
            select
                a.id_document as id_document,
                array_agg(b.label) as labels
            from
                www.document_label_en a
                inner join www.label_en b
                on a.id_label_en=b.id_label_en
            group by id_document),
        label_es as(
            select
                a.id_document as id_document,
                array_agg(b.label) as labels
            from
                www.document_label_es a
                inner join www.label_es b
                on a.id_label_es=b.id_label_es
            group by id_document),
        authors as(
            select
                id_document as id_document,
                array_agg(coalesce(twitter_user, name)) as author
            from www.author
            group by id_document),
        docs as(
            select
                a.id_document,"""

        if lang=="en":
            doc += "coalesce(title_en, title_es) as title,"
        else:
            doc += "coalesce(title_es, title_en) as title,"

        if lang=="en":
            doc += "coalesce(theme_en, theme_es) as theme,"
        else:
            doc += "coalesce(theme_es, theme_en) as theme,"

        if lang=="en":
            doc += "coalesce(description_en, description_es) as description,"
        else:
            doc += "coalesce(description_es, description_en) as description,"

        doc += """
                a.last_edit_time as time
            from www.document a
        )
        select
            a.id_document as id,
            a.title as title,
            a.theme as theme,
            a.description as description,
            a.time as time,
            b.labels as labels,
            d.author as authors
        from
            docs a inner join """

        if lang=="en":
            doc += "label_en b on"
        else:
            doc += "label_es b on"

        doc += """
            a.id_document=b.id_document inner join
            authors d on
            a.id_document=d.id_document
        where
            a.id_document=%s"""

        return(self.query(doc, bindings=[idDocument]).row())


    def getDocumentCatalogSize(self, search=None):
        """Gets the total size of a list of document for the frontend."""
        docs = """
        with count as(
        select distinct a.id_document
        from
          www.document a inner join
          www.document_label_en b on
          a.id_document=b.id_document inner join
          www.label_en c on
          b.id_label_en=c.id_label_en inner join
          www.document_label_es d on
          a.id_document=d.id_document inner join
          www.label_es e on
          d.id_label_es=e.id_label_es inner join
          www.author f on
          a.id_document=f.id_document"""

        if search:
            search = "%"+search+"%"
            docs+="""
              where
                a.title_en ilike %s or
                a.title_es ilike %s or
                a.theme_en ilike %s or
                a.theme_es ilike %s or
                a.description_en ilike %s or
                a.description_es ilike %s or
                c.label ilike %s or
                e.label ilike %s or
                f.name ilike %s or
                f.twitter_user ilike %s"""

        docs+="""
        )
        select count(id_document) as c
        from count;"""

        if search:
            return self.query(docs, bindings=[ \
                                               search, search, search, search, search, \
                                               search, search, search, search, search]).row()["c"]
        else:
            return self.query(docs).row()["c"]
               

    def getDocumentCatalog(self, offset, listSize, lang, search=None):
        """Gets list of documents for the frontend document catalog."""
        a = """
        with label_en as(
          select
            a.id_document as id_document,
            array_agg(b.label) as labels
          from
            www.document_label_en a
            inner join www.label_en b
            on a.id_label_en=b.id_label_en
          group by id_document),
        label_es as(
          select
            a.id_document as id_document,
            array_agg(b.label) as labels
          from
            www.document_label_es a
            inner join www.label_es b
            on a.id_label_es=b.id_label_es
          group by id_document),
        authors as(
          select
            id_document as id_document,
            array_agg(coalesce(twitter_user, name)) as author
          from www.author
          group by id_document),
        docs as(
          select
            a.id_document,"""

        if lang=="es":
            a+="""
            coalesce(title_es, title_en) as title, 
            coalesce(theme_es, theme_en) as theme, """
        else:
            a+="""
            coalesce(title_en, title_es) as title, 
            coalesce(theme_en, theme_es) as theme, """

        a+="""
            a.last_edit_time as time
          from www.document a
        ),
        selection as (
          select distinct a.id_document
          from
            www.document a inner join
            www.document_label_en b on
            a.id_document=b.id_document inner join
            www.label_en c on
            b.id_label_en=c.id_label_en inner join
            www.document_label_es d on
            a.id_document=d.id_document inner join
            www.label_es e on
            d.id_label_es=e.id_label_es inner join
            www.author f on
            a.id_document=f.id_document"""

        if search:
            search = "%"+search+"%"
            a+="""
              where
                a.title_en ilike %s or
                a.title_es ilike %s or
                a.theme_en ilike %s or
                a.theme_es ilike %s or
                a.description_en ilike %s or
                a.description_es ilike %s or
                c.label ilike %s or
                e.label ilike %s or
                f.name ilike %s or
                f.twitter_user ilike %s"""

        a+="""
        )
        select
          a.id_document as id,
          a.title as title,
          a.theme as theme,  
          a.time as time,
          b.labels as labels,
          d.author as authors
        from
          docs a inner join 
          label_{} b on
          a.id_document=b.id_document inner join
          authors d on
          a.id_document=d.id_document
        where
          a.id_document in (select * from selection)
        offset %s limit %s;""".format(lang)

        if search:
            return self.query(a, bindings=[ \
                                            search, search, search, search, search, \
                                            search, search, search, search, search, \
                                            offset*listSize, listSize]).result()
        else:
            return self.query(a, bindings=[offset*listSize, listSize]).result()


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
        q = "select id_author, twitter_user from www.author where id_document=%s;"
        return self.query(q, [id_document]).result()


    def getDocumentPdf(self, id_document, lang=None):
        """Gets the list of PDF of a document, optionally for a given language."""
        q = "select id_pdf, pdf_name as name, hash from www.pdf where id_document=%s"
        bindings = [id_document]

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


    def getDocumentBackend(self,id_document):
        """Get Document for the frontend."""
        q = "SELECT * FROM www.document WHERE id_document=%s"
        return self.query(q,[id_document]).row()


    def getDocumentLabels(self, id_document, lang):
        """Get document labels."""
        if lang == "es":
            q = "SELECT dl.id_label_es as id_label,l.label FROM www.document_label_es dl "\
                    " INNER JOIN  www.label_es l ON dl.id_label_es=l.id_label_es "\
                    " WHERE id_document=%s"
        else:
           q = "SELECT dl.id_label_en as id_label,l.label FROM www.document_label_en dl"\
                    " INNER JOIN www.label_en l ON dl.id_label_en=l.id_label_en "\
                    " WHERE id_document=%s"

        return self.query(q,[id_document]).result()
