#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import threading
from jsonium.core.document import Document

class Table:

    _name = None
    _database = None

    __mutex = None

    def __init__(self, name, db_object):
        self.__mutex = threading.Lock()
        self.name = name
        self.database = db_object
        self.database.driver.create_table(self.database, self)
        self.last_id = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name must be an instance of str')
        self._name = name

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, database):
        self._database = database

    @property
    def last_id(self):
        return self.database.driver.get_table_last_id(
            self.database,
            self,
        )

    @last_id.setter
    def last_id(self, last_id):
        if not isinstance(last_id, int):
            raise TypeError('last_id must be an instance of int')
        self.__mutex.acquire()
        self.database.driver.set_table_last_id(
            self.database,
            self,
            last_id,
        )
        self.__mutex.release()


    def __repr__(self):
        return '<jsonium.core.Table name="{name}">'.format(
            name=self.name,
        )

    def insert(self, attributes):

        document = Document(attributes)

        self.database.driver.create_document(
            self.database,
            self,
            document
        )

        self.last_id = document.id

        return document
