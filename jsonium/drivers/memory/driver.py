#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os.path
from jsonium.abstract import Driver
from jsonium.storages import StorageFactory


class MemoryDriver(Driver):

    def __init__(self, *args, **kwargs):
        super(MemoryDriver, self).__init__(*args, **kwargs)
        storage_factory = StorageFactory()
        self.storage = storage_factory.build('jsonium.storages.MemoryStorage')

    def create_database(self, db_object):
        return self.storage.mkdir(os.path.join('databases', db_object.name))

    def create_table(self, db_object, tb_object):
        return self.storage.mkdir(os.path.join(
            'databases',
            db_object.name,
            'tables',
            tb_object.name,
        ))
