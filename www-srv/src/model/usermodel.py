# coding=UTF8

"""

User model.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel


class UserModel(PostgreSQLModel):
    
    def getUserLogin(self,idUser=None,email=None):
        sql = "SELECT id_wwwuser,email,name,surname,password,username,language \
                    FROM www.wwwuser WHERE admin AND status=1 AND "
        if idUser:
            sql = sql + " id_user=%s"
            binding = idUser
        elif email:
            sql = sql + " email=%s"
            binding = email
        else:
            raise Exception("Bad parameters")
            return None
        
        return self.query(sql,[binding]).row()


    def newUser(self, data):
        """Creates a new user."""
        try:
            a = self.insert("www.wwwuser",
                            {"name": data["name"],
                             "surname": data["surname"],
                             "password": data["password"],
                             "email": data["email"],
                             "admin": data["admin"],
                             "username": data["username"],
                             "language": data["language"],
                             "status": data["status"]},
                            returnID="id_wwwuser")

            a = {"id": a}
        except:
            a = {"error": "Duplicated email"}

        return a