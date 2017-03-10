#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from jsonium.abstract import Driver
from jsonium.storages import StorageFactory


class FileDriver(Driver):

    def __init__(self, *args, **kwargs):
        super(FileDriver, self).__init__(*args, **kwargs)
        storage_factory = StorageFactory()
        self.storage = storage_factory.build('jsonium.storages.FileStorage')
