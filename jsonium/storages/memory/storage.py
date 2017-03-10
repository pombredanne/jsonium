#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from jsonium.abstract import Storage


class MemoryStorage(Storage):

    __root__ = None

    def __init__(self, *args, **kwargs):
        super(MemoryStorage, self).__init__(*args, **kwargs)
        self.__root__ = {}
