import sqlite3


class Sql:
    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def reg_user(self, user_id,login,passw):
        """Проверяем, есть ли учетка у юзера"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM login  WHERE (id,login,passw) = (?,?,?)", (user_id,login,passw),).fetchall()
            return bool(len(result))


    def add_reg_user(self, user_id,login,passw):
        """Проверяем, есть ли учетка у юзера"""
        with self.connection:
            return self.cursor.execute('INSERT INTO login (id,login,pass) VALUES(?,?,?)', (user_id,login,passw))
