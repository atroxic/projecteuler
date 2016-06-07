#!/usr/bin/env python3

def find_divisors(num):
	result = []
	result_sum = 0
	for x in range(1, num):
		if num % x == 0:
			result.append(x)
			result_sum += x
	return result_sum

final_sum = 0
print("Working...", end="", flush=True)


for x in range(10000):
	amount = find_divisors(x)
	if x % 100 == 0:
		print('.', end='', flush=True)
	if x == find_divisors(amount) and x != amount:
		final_sum += x
print("\nTotal of all amicable numbers is: " + str(final_sum))
