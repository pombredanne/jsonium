#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from jsonium.abstract import Driver
from jsonium.drivers import DriverFactory


class Jsonium:

    _name = None
    _driver = None

    def __init__(self, name, driver):
        self.name = name
        self.driver = driver
        self.driver.create_database(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name must be an instance of str')
        self._name = name

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver):
        if not isinstance(driver, Driver):
            raise TypeError('driver must be an instance of jsonium.abstract.Driver')
        self._driver = driver
