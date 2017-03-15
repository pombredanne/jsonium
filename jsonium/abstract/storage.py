#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Storage(object):

    def __init__(self, *args, **kwargs):
        pass

    def mkdir(self, dir_fd, **kwargs):
        raise NotImplementedError

    def write_file(self, fp, raw, **kwargs):
        raise NotImplementedError

    def write_json(self, fp, dict_obj, **kwargs):
        raise NotImplementedError

    def read_file(self, fp, **kwargs):
        raise NotImplementedError

    def read_json(self, fp, **kwargs):
        raise NotImplementedError
