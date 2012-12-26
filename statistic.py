#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime


def Daily (date):
    """
    Функция для округления даты до дня
    """
    return datetime.datetime (date.year, date.month, date.day)


def Daily10 (date):
    """
    Функция для округления даты до 10 дней (+/- один день на 31 день)
    """
    if date.day > 20:
        return datetime.datetime (date.year, date.month, 21)

    if date.day > 10:
        return datetime.datetime (date.year, date.month, 11)

    return datetime.datetime (date.year, date.month, 1)


def Monthly (date):
    """
    Функция для округления даты до месяца
    """
    return datetime.datetime (date.year, date.month, 1)


class Statistic (object):
    def __init__ (self, commits):
        """
        commits - список коммитов (экземпляров класса Commit)
        """
        self._commits = commits


    def getStat (self, truncation):
        """
        Создать статистику по коммитам.
        Возвращает список кортежей (дата, количество коммитов)
        truncation - функция для округления дат до определенного интервала (дня, месяца, года и т.п.)
        """
        # Ключ - дата, значение - количество коммитов в этот промежуток времени
        result = {}
        for commit in self._commits:
            date = truncation (commit.date)
            if date in result:
                result[date] += 1
            else:
                result[date] = 1

        resultlist = result.items()
        resultlist.sort (self._sortByDate)

        return resultlist


    def _sortByDate (self, item1, item2):
        if item1[0] > item2[0]:
            return 1

        if item1[0] < item2[0]:
            return -1

        return 0
