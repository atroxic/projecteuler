#!/usr/bin/env python3

import sys, os, csv

def letter2number(char):
	return ord(char.lower()) - 96

try:
	file = sys.argv[1]
except:
	file = input("Enter file to open: ")

f = open(file, 'r')
reader = csv.reader(f, delimiter=',')
for row in reader:
	list = row
f.close()
list.sort()

total = 0

for name in list:
	sum = 0
	for x in name:
		sum += letter2number(x)
	total += sum * (list.index(name) + 1)

print("The total of all the name scores is: " + str(total))
