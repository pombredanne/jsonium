#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import os.path
from jsonium.abstract import Storage


class FileStorage(Storage):

    def __init__(self, *args, **kwargs):
        super(FileStorage, self).__init__(*args, **kwargs)

    def mkdir(self, dir_fd, **kwargs):
        mode = int(kwargs.get('mode', 644))
        sep = os.path.sep
        path = dir_fd.split(sep)
        current_segment = ''
        for segment in path:
            current_segment += segment + sep
            if not (os.path.exists(current_segment) and os.path.isdir(current_segment)):
                os.mkdir(current_segment, mode)
            else:
                continue
        return True
