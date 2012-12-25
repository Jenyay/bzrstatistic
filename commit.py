#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Commit (object):
    """
    Класс для хранения информации об одном коммите
    """
    def __init__ (self, date):
        """
        date - дата коммита
        """
        self.date = date
