#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Нарисовать статистику по коммитам по логам bzr с помощью Matplotlib

Использование: python plotstat.py logfile.txt
"""

import sys

import pylab
import matplotlib.dates

from logparser import LogParser
from statistic import Statistic, Daily, Daily10, Monthly


if __name__ == "__main__":
    if len (sys.argv) < 2:
        print "Using: python plotstat.py logfile.txt"
        exit (1)

    fname = sys.argv[-1]

    try:
        with open (fname) as fp:
            logstr = fp.read()
    except IOError, e:
        print "Can't open {0}".format (fname)
        exit (1)

    parser = LogParser (logstr)
    stat = Statistic (parser.commits)
    dateList = stat.getStat (Daily10)

    dates, count = zip (*dateList)

    # Преобразуем даты в числовой формат
    dates_float = [matplotlib.dates.date2num (date) for date in dates]

    # Вызовем subplot явно, чтобы получить экземпляр класса AxesSubplot,
    # из которого будем иметь доступ к осям
    axes = pylab.subplot(1, 1, 1)

    # Пусть в качестве меток по оси X выводится только год
    axes.xaxis.set_major_formatter (matplotlib.dates.DateFormatter("%Y.%m"))

    # Отобразим данные
    pylab.bar (dates_float, count, width = 10)

    pylab.grid()
    pylab.show()
