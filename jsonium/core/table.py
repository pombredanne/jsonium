#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Table:

    _database = None

    def __init__(self, name, db_object):
        self.name = name
        self.database = db_object
        self.database.driver.create_table(self.database, self)

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

    def __repr__(self):
        return '<jsonium.core.Table name="{name}">'.format(
            name=self.name,
        )
