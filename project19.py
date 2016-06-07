#!/usr/bin/env python3

import datetime

sundays = 0
#Cycle years/months
for y in range(1901, 2001):
	for m in range(1, 13):
		if datetime.date.weekday(datetime.date(y, m, 1)) == 6:
			sundays += 1

print("There are", sundays, "on the first of the month between 1 Jan 1901 and 31 Dec 2000")
