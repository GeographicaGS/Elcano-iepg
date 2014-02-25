'''
Created on 15/01/2014

@author: alasarr
'''

from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
import base

class UserModel(PostgreSQLModel):
    
    def getUserLogin(self,idUser=None,email=None):
        sql = "SELECT id_user,email,name,surname,password,username,language \
                    FROM www.user WHERE admin AND status=1 AND "
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

        return a
