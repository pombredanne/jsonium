#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from jsonium.abstract import Storage
from jsonium.storages import (
    FileStorage,
    MemoryStorage,
)


class StorageFactory:

    _storages = None

    def __init__(self, *args, **kwargs):
        self.storages = {
            'jsonium.storages.FileStorage': FileStorage,
            'jsonium.storages.MemoryStorage': MemoryStorage,
        }

    @property
    def storages(self):
        return self._storages

    @storages.setter
    def storages(self, storages):
        if not isinstance(storages, dict):
            raise TypeError('storages must be an instance of dict')
        self._storages = {}
        for storage_name, storage in storages.items():
            self.register(storage_name, storage)

    def register(self, storage_name, storage):
        if not isinstance(storage_name, str):
            raise TypeError('storage_name must be an instance of str')
        if not issubclass(storage, Storage):
            raise TypeError('storage must be an instance of jsonium.abstract.storage')
        self.storages.__setitem__(storage_name, storage)

    def build(self, storage_name, **kwargs):
        if storage_name not in self.storages:
            raise IndexError('storage not found, {d_name} does not exist'.format(
                d_name=storage_name,
            ))
        storage_class = self.storages.get(storage_name, Storage)
        storage = storage_class(**kwargs)
        return storage
