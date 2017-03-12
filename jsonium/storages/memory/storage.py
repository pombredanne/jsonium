#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os.path
from jsonium.abstract import Storage


class MemoryStorage(Storage):

    __root__ = None

    def __init__(self, *args, **kwargs):
        super(MemoryStorage, self).__init__(*args, **kwargs)
        self.__root__ = {}

    def mkdir(self, dir_fd, **kwargs):
        sep = os.path.sep
        path = dir_fd.split(sep)
        depth = self.__root__
        for segment in path:
            if segment not in depth:
                depth.__setitem__(segment, {})
            depth = depth.get(segment, {})
        return True
