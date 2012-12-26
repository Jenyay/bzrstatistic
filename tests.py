#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import datetime

from logparser import LogParser


class LogParserTest (unittest.TestCase):
    def setUp (self):
        pass


    def tearDown (self):
        pass


    def loadFile (self, fname):
        with open (fname) as fp:
            return fp.read()


    def testParseItemsWithMerge (self):
        fname = u"examples/example_3_small.log"

        parser = LogParser (self.loadFile (fname))
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

        parser = LogParser (self.loadFile (fname))
        self.assertEqual (len (parser.commits), 13)

        self.assertEqual (parser.commits[0].date, 
                datetime.datetime (2012, 12, 14, 11, 8, 23))

        self.assertEqual (parser.commits[1].date, 
                datetime.datetime (2012, 12, 10, 20, 21, 9))

        self.assertEqual (parser.commits[-1].date, 
                datetime.datetime (2012, 11, 24, 10, 43, 23))




if __name__ == "__main__":
    unittest.main()
