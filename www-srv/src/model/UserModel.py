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
    
   
    
    