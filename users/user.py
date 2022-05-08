

from calendar import different_locale
from unittest import result
import users.conection as conection
import datetime
import hashlib



connect = conection.conectar()
database = connect[0]
cursor = connect[1]

class User:

    def __init__(self, name, last_name, email, password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password

    def to_register(self): # (registrar)

        cifrado = hashlib.sha256() # encrypt password
        cifrado.update(self.password.encode('utf8'))

        fecha = datetime.datetime.now()
        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.last_name, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, user) # query and "data for the query"
            database.commit()
            result =  [cursor.rowcount, self] # "Return the amount of records that have been modifeid" and "return the own object (self) and all its data"
        except:
            result = [0, self]
        
        return result

        
    def to_identify(self): #(identificar)
        sql = "SELECT * FROM users WHERE email = %s AND password = %s" # query to verify if user exists in db

        cifrado = hashlib.sha256() # encrypt password
        cifrado.update(self.password.encode('utf8'))

        user = (self.email, cifrado.hexdigest()) # data for query

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result


