#!/usr/bin/python

import sys, datetime

# Mapper - Average sales per day of the week

def dayOfWeek(str_date):
    date = datetime.datetime.strptime(str_date, '%Y-%m-%d')
    return date.strftime('%A')

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
	date, time, city, item, cost, payment = data
	date = dayOfWeek(date)
	print "{0}\t{1}".format(date, cost)
