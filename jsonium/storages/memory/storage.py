#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os.path
import json
from jsonium.abstract import Storage
from jsonium.contrib.serializers import JSONSerializer


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

    def write_file(self, fp, raw, **kwargs):
        sep = os.path.sep
        path = fp.split(sep)
        depth = self.__root__
        for segment in path[:-1]:
            if segment not in depth:
                depth.__setitem__(segment, {})
            depth = depth.get(segment, {})
        for segment in path[-1:]:
            depth.__setitem__(segment, raw)
        return True

    def write_json(self, fp, dict_obj, **kwargs):
        serializer = kwargs.get('serializer', JSONSerializer())
        raw = json.dumps(dict_obj, default=serializer.encoder)
        return self.write_file(fp, raw)

    def read_file(self, fp, **kwargs):
        sep = os.path.sep
        path = fp.split(sep)
        depth = self.__root__
        for segment in path[:-1]:
            if (not depth) or (segment not in depth):
                raise IndexError
            depth = depth.get(segment, {})
        for segment in path[-1:]:
            if (not depth) or (segment not in depth):
                raise IndexError
            depth = depth.get(segment, {})
            data = depth
        return data

    def read_json(self, fp, **kwargs):
        serializer = kwargs.get('serializer', JSONSerializer())
        raw = self.read_file(fp, **kwargs)
        dict_obj = json.loads(raw, object_hook=serializer.decoder)
        return dict_obj
