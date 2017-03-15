#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import collections


class Document(collections.defaultdict):

    def __init__(self, attributes, **kwargs):
        super(Document, self).__init__(default_factory=Document, **kwargs)
        for key, value in attributes.items():
            setattr(self, key, value)

    def __get__(self, instance, owner):
        return self