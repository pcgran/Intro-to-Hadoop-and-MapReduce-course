#!/usr/bin/python

import sys

# Reducer - Average sales per day of the week

currentDay = ""
total = 0
count = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 2:
	day, cost = data
	if currentDay == "":
	    currentDay = day
	if day == currentDay:
	    total += float(cost)
	    count += 1
	else:
	    print "{0}\t{1}".format(currentDay,str(total/count))
	    total = 0
	    count = 0
	    currentDay = day
	    # include first appearance of the day
	    total += float(cost)
	    count += 1

print "{0}\t{1}".format(day,str(total/count))
