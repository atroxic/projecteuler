#!/usr/bin/env python3

import time

def sum_of_divisors(num):
	sum = 1
	p = 2
	while p*p <= num and num > 1:
		if num % p == 0:
			j = p * p
			num = num / p
			while num % p == 0:
				j = j * p
				num = num / p
			sum = sum * (j - 1)
			sum = sum / (p - 1)
		if p == 2:
			p = 3
		else:
			p = p + 2
	if num > 1:
		sum = sum * (num + 1)
	return sum

def sum_of_proper_divisors(num):
	return sum_of_divisors(num) - num

start = time.time()
sum = 0
for x in range(2, 10000):
	b = sum_of_proper_divisors(x)
	if b > x:
		if sum_of_proper_divisors(b) == x:
			sum = sum + x + b
print("Total of all amicable numbers: " + str(int(sum)))
print("Done in {:.2f} seconds".format(time.time() - start))
