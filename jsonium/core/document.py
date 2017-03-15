#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import copy
import json
from jsonium.contrib.serializers import JSONSerializer


class Document(dict):

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(self, key):
        if key not in self.keys():
            self.__setitem__(key, Document())
        return self.__getitem__(key)

    def __init__(self, **attrs):
        super(Document, self).__init__()
        for key, value in attrs.items():
            self.__setitem__(key, value)

    def to_dict(self):
        return copy.deepcopy(dict(self))

    def to_json(self, **kwargs):
        serializer = kwargs.get('serializer', JSONSerializer())
        raw = json.dumps(self.__dict__, default=serializer.encoder)
        return raw

    @classmethod
    def from_json(self, raw, **kwargs):
        serializer = kwargs.get('serializer', JSONSerializer())
        attrs = json.loads(raw, default=serializer.decoder)
        return Document(**attrs)

    def __repr__(self):
        return '<jsonium.core.Document id={pk}>'.format(
            pk=self.id,
        )
