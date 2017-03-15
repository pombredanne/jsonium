#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class JSONSerializer:

    def encoder(self, o):
        return o

    def decoder(self, dict_obj):
        for key, value in dict_obj.items():
            pass
        return dict_obj
