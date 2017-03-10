#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from jsonium.abstract import Driver
from jsonium.drivers import (
    FileDriver,
    MemoryDriver,
)


class DriverFactory:

    _drivers = None

    def __init__(self, *args, **kwargs):
        self.drivers = {
            'jsonium.drivers.FileDriver': FileDriver,
            'jsonium.drivers.MemoryDriver': MemoryDriver
        }

    @property
    def drivers(self):
        return self._drivers

    @drivers.setter
    def drivers(self, drivers):
        if not isinstance(drivers, dict):
            raise TypeError('drivers must be an instance of dict')
        self._drivers = {}
        for driver_name, driver in drivers.items():
            self.register(driver_name, driver)

    def register(self, driver_name, driver):
        if not isinstance(driver_name, str):
            raise TypeError('driver_name must be an instance of str')
        if not issubclass(driver, Driver):
            raise TypeError('driver must be an instance of jsonium.abstract.Driver')
        self.drivers.__setitem__(driver_name, driver)

    def build(self, driver_name, **kwargs):
        if driver_name not in self.drivers:
            raise IndexError('driver {driv_name} does not exist'.format(
                driv_name=driver_name,
            ))
        driver_class = self.drivers.get(driver_name, Driver)
        driver = driver_class(**kwargs)
        return driver
