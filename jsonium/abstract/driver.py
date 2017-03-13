#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from jsonium.abstract.storage import Storage


class Driver:

    _storage = None

    def __init__(self, *args, **kwargs):
        pass

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, storage):
        if not isinstance(storage, Storage):
            raise TypeError('storage must be an instance of jsonium.abstract.Storage')
        self._storage = storage

    def create_database(self, db_object):
        raise NotImplementedError

    def create_table(self, db_object, tb_object):
        raise NotImplementedError
