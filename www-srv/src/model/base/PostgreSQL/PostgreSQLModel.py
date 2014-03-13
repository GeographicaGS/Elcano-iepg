'''
Created on 15/01/2014

@author: alasarr
'''

import psycopg2
from config import PostgreSQLConfig
import psycopg2.extras

class Result():
    def __init__(self,cur):
        self.cur = cur
    
    def result(self):
        return self.cur.fetchall()
    
    def row(self):
        return self.cur.fetchone()
        

class PostgreSQLModel():
    def __init__(self):
        self.conn = psycopg2.connect(host=PostgreSQLConfig['host'],dbname=PostgreSQLConfig['db'],port=PostgreSQLConfig['port'],user=PostgreSQLConfig['user'],password=PostgreSQLConfig['passwd'])
        
    def query(self,sql,bindings=None):
        cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(sql,bindings)
        return Result(cur)
    
    def queryCommit(self,sql,bindings=None):
        cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(sql,bindings)
        self.conn.commit()
    
    def insert(self,table,data,returnID=None):
        cur = self.conn.cursor()
        returnIDSQL = "RETURNING " + returnID  if returnID else ""
        sql = "INSERT INTO %s (%s) VALUES (%s) %s" % (table,",".join(data.keys()),",".join(["%s" for e in data.keys()]),returnIDSQL)     
        
        cur.execute(sql,data.values())
        self.conn.commit()
        if returnID:
            return cur.fetchone()[0]
        else:
            return None
        
    def update(self,table,data,where):
        setSQLString = ""
        for key in data:
            setSQLString += str(key) + "=%s," 
            
        setSQLString = setSQLString[:-1]
        
        whereSQLString = " true "
        for key in where:
            whereSQLString += " AND " + str(key) + "=%s " 
            
        cur = self.conn.cursor()        
        sql = "UPDATE %s SET %s WHERE %s" % (table,setSQLString,whereSQLString)     
        
        cur.execute(sql,data.values()+where.values())
        self.conn.commit()        
    
    def insertBatch(self,table,data):
        for d in data:
            self.insert(table, d)
        
