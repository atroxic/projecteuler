#!/usr/bin/env python3

def factorial(num):
	if num <= 1:
		return num
	else:
		return num * factorial(num - 1)

def count_digits(num):
	total = 0
	num = str(num)
	for x in iter(num):
		total += int(x)
	return total

ask = input("Enter a number: ")

try:
	answer = factorial(int(ask))
	count = count_digits(answer)
except:
	print("Invalid Number")
else:
	print(ask, "factoralized is", answer, "and the sum of the digits is", count)

	
