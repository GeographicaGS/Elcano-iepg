"""

Modelo de documento.

"""

from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel

class DocumentModel(PostgreSQLModel):
    """Modelo de documento."""

    def createDocument(self, data):
        print(data)

