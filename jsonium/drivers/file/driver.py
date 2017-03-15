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
        ok = True
        ok &= self.storage.mkdir(os.path.join(
            'databases',
            db_object.name,
            'tables',
            tb_object.name,
            'documents',
        ))

        ok &= self.storage.mkdir(os.path.join(
            'databases',
            db_object.name,
            'tables',
            tb_object.name,
            'meta',
        ))
        ok &= self.storage.mkdir(os.path.join(
            'databases',
            db_object.name,
            'tables',
            tb_object.name,
            'indexes',
        ))
        return ok

    def get_table_last_id(self, db_object, tb_object):
        dict_obj = self.storage.read_json(
            os.path.join(
                'databases',
                db_object.name,
                'tables',
                tb_object.name,
                'meta',
                'last_id.json',
            )
        )
        return dict_obj.get('last_id', None)

    def set_table_last_id(self, db_object, tb_object, last_id):
        return self.storage.write_json(
            os.path.join(
                'databases',
                db_object.name,
                'tables',
                tb_object.name,
                'meta',
                'last_id.json',
            ),
            {
                'last_id': last_id,
            },
        )

    def insert_document(self, db_object, tb_object, doc_object):
        return self.storage.write_json(
            os.path.join(
                'databases',
                db_object.name,
                'tables',
                tb_object.name,
                'documents',
                '{f_name}.json'.format(
                    f_name=doc_object.id,
                ),
            ),
            doc_object.to_dict(),
        )
