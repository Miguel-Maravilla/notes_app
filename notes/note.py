from users import conection as connection


connect = connection.conectar()
database = connect[0]
cursor = connect[1]


class Note:

    def __init__(self, user_id, title, description):
        self.user_id = user_id
        self.title = title
        self.description = description
    
    def to_save(self):
        sql = "INSERT INTO notes VALUES (null, %s, %s, %s, NOW())" # NOW() is a MySQL function
        note = (self.user_id, self.title, self.description)

        cursor.execute(sql, note)
        database.commit()

        return [cursor.rowcount, self] # rowcount = cantidad de filas afectadas, self = el objeto en sí


    def to_list(self):
        sql = f"SELECT * FROM notes WHERE user_id = {self.user_id}"
        cursor.execute(sql)
        result = cursor.fetchall() # fetchall() allows you to recover all result set, instead of fetchone()

        return result


    def to_delete(self):
        sql = f"DELETE FROM notes WHERE user_id = {self.user_id} AND title LIKE '%{self.title}%'"
        
        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]

