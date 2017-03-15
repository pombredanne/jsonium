#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import (
    find_packages,
    setup,
)


VERSION = __import__('jsonium').VERSION


setup(
    name='Jsonium',
    version=VERSION,
    url='https://github.com/pythonium/jsonium',
    author='Pythonium Members and Contributors',
    description='A prototype of database engine based on JSON documents.',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
)
