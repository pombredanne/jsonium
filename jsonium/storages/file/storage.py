#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import os.path
import json
from jsonium.abstract import Storage
from jsonium.contrib.serializers import JSONSerializer


class FileStorage(Storage):

    def __init__(self, *args, **kwargs):
        super(FileStorage, self).__init__(*args, **kwargs)

    def mkdir(self, dir_fd, **kwargs):
        mode = int(kwargs.get('mode', 755))
        sep = os.path.sep
        path = dir_fd.split(sep)
        current_segment = str()
        for segment in path:
            current_segment += segment + sep
            if not (os.path.exists(current_segment) and os.path.isdir(current_segment)):
                os.mkdir(current_segment, mode)
        return True

    def write_file(self, fp, raw, **kwargs):
        mode = int(kwargs.get('mode', 755))
        sep = os.path.sep
        path = fp.split(sep)
        current_segment = str()
        for segment in path[:-1]:
            current_segment += segment + sep
            if not (os.path.exists(current_segment) and os.path.isdir(current_segment)):
                os.mkdir(current_segment, mode)
        for _ in path[-1:]:
            fd = sep.join(path)
            with open(fd, 'w+') as f:
                f.write(raw)
        return True

    def write_json(self, fp, dict_obj, **kwargs):
        serializer = kwargs.get('serializer', JSONSerializer())
        raw = json.dumps(dict_obj, default=serializer.encoder)
        return self.write_file(fp, raw, **kwargs)

    def read_file(self, fp, **kwargs):
        data = None
        with open(fp, 'r') as f:
            data = '\n'.join(f.readlines())
        return data

    def read_json(self, fp, **kwargs):
        serializer = kwargs.get('serializer', JSONSerializer())
        raw = self.read_file(fp, **kwargs)
        dict_obj = json.loads(raw, object_hook=serializer.decoder)
        return dict_obj
