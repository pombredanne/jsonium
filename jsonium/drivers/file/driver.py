#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os.path
from jsonium.abstract import Driver
from jsonium.storages import StorageFactory


class FileDriver(Driver):

    def __init__(self, *args, **kwargs):
        super(FileDriver, self).__init__(*args, **kwargs)
        storage_factory = StorageFactory()
        self.storage = storage_factory.build('jsonium.storages.FileStorage')

    def create_database(self, db_object):
        return self.storage.mkdir(os.path.join('databases', db_object.name))

    def create_table(self, db_object, tb_object):
        table_is_created = self.storage.mkdir(os.path.join(
            'databases',
            db_object.name,
            'tables',
            tb_object.name,
            'documents',
        ))
        meta_is_created = self.storage.mkdir(os.path.join(
            'databases',
            db_object.name,
            'tables',
            tb_object.name,
            'meta',
        ))
        index_folder_is_created = self.storage.mkdir(os.path.join(
            'databases',
            db_object.name,
            'tables',
            tb_object.name,
            'indexes',
        ))
        return table_is_created & meta_is_created & index_folder_is_created
