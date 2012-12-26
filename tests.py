#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import datetime

from logparser import LogParser
from statistic import Statistic, Daily

def loadFile (fname):
    with open (fname) as fp:
        return fp.read()


class LogParserTest (unittest.TestCase):
    """
    Класс тестов разбора лога
    """
    def testParseItemsWithMerge (self):
        fname = u"examples/example_3_small.log"

        parser = LogParser (loadFile (fname))
        self.assertEqual (len (parser.commits), 20)

        self.assertEqual (parser.commits[0].date, 
                datetime.datetime (2010, 9, 19, 21, 7, 25))

        self.assertEqual (parser.commits[7].date, 
                datetime.datetime (2010, 10, 8, 19, 15, 16))

        self.assertEqual (parser.commits[8].date, 
                datetime.datetime (2010, 10, 8, 21, 43, 32))

        self.assertEqual (parser.commits[-1].date, 
                datetime.datetime (2010, 10, 17, 19, 17, 26))


    def testParseItems (self):
        fname = u"examples/example_1_small.log"

        parser = LogParser (loadFile (fname))
        self.assertEqual (len (parser.commits), 13)

        self.assertEqual (parser.commits[0].date, 
                datetime.datetime (2012, 12, 14, 11, 8, 23))

        self.assertEqual (parser.commits[1].date, 
                datetime.datetime (2012, 12, 10, 20, 21, 9))

        self.assertEqual (parser.commits[-1].date, 
                datetime.datetime (2012, 11, 24, 10, 43, 23))


    def testParseItems2 (self):
        fname = u"examples/example_1.log"

        parser = LogParser (loadFile (fname))
        self.assertEqual (len (parser.commits), 1003)


    def testParseEmpty (self):
        parser = LogParser (u"")
        self.assertEqual (len (parser.commits), 0)


class StatisticTest (unittest.TestCase):
    """
    Тест класса сбора статистики Statistic
    """
    def testStatisticDaily (self):
        fname = u"examples/example_1_small.log"
        parser = LogParser (loadFile (fname))

        stat = Statistic (parser.commits)
        statlist = stat.getStat (Daily)

        self.assertEqual (len (statlist), 6)
        self.assertEqual (statlist[0][0], datetime.datetime (2012, 11, 24))
        self.assertEqual (statlist[0][1], 6)

        self.assertEqual (statlist[-1][0], datetime.datetime (2012, 12, 14))
        self.assertEqual (statlist[-1][1], 1)


    def testStatisticEmpty (self):
        stat = Statistic ([])
        statlist = stat.getStat (Daily)

        self.assertEqual (len (statlist), 0)


if __name__ == "__main__":
    unittest.main()
