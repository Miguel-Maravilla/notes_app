
import mysql.connector  


# CONNECT TO DATABASE  [".connect()" method is indside of "mysql.connector" library]

def conectar():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "notes_app_v2",
        port = 3306
    )

    # CREATE "CURSOR" TO MAKE QUERIES  (use the buffered=True parameter, to make many queries)
    cursor = database.cursor(buffered=True)

    return [database, cursor]