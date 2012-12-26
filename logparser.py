#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import datetime

from commit import Commit


class LogParser (object):
    """
    Класс для парсинга лога
    """
    def __init__ (self, logstr):
        """
        logstr - содержимое лога
        """
        self._commitRegEx = re.compile (r".*timestamp: \w+ (?P<year>\d\d\d\d)-(?P<month>\d\d)-(?P<day>\d\d) (?P<hour>\d\d):(?P<minute>\d\d):(?P<second>\d\d)", flags=re.MULTILINE | re.UNICODE)

        self._commitList = self._parseLog (logstr)


    @property
    def commits (self):
        return self._commitList


    def _parseLog (self, logstr):
        """
        Разбор лога
        """
        # Выкидываем первую запись, т.к. она пустая
        allItems = re.split (r"^\s*-+$", logstr, flags=re.MULTILINE | re.UNICODE)[1:]
        commits = self._createCommits (allItems)

        return commits


    def _createCommits (self, items):
        """
        По элементам лога создать список коммитов
        """
        return [self._createCommitByItem (item) for item in items]

    
    def _createCommitByItem (self, item):
        match = self._commitRegEx.search (item)
        assert match != None

        date = datetime.datetime (
                int (match.group ("year")),
                int (match.group ("month")),
                int (match.group ("day")),
                int (match.group ("hour")),
                int (match.group ("minute")),
                int (match.group ("second")))

        return Commit (date)
