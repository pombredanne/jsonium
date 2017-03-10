#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from jsonium.abstract import Storage


class FileStorage(Storage):

    def __init__(self, *args, **kwargs):
        super(FileStorage, self).__init__(*args, **kwargs)
