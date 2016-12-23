# -*- coding: utf-8 -*-
import sqlite3

class Connection:
    def __init__(self):
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = sqlite3.connect('my.sqlite')

    def disconnect(self):
        if self._connection:
            self._connection.close()


class UserModel:
    def __init__(self, db_connection, id, name, email, phone):
        self.db_connection = db_connection.connection
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO UserModel (id, name, email, phone) VALUES ('%s', '%s', '%s', '%s');"%(self.id, self.name, self.email, self.phone))
        self.db_connection.commit()
        c.close()


con = Connection()

with con:
    usermodel = UserModel(con, '2', 'Igor Nasedkin', 'ignased@yandex.ru', '84956780987')
    usermodel.save()