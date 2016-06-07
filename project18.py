#!/usr/bin/env python3

print("Enter the pyramid, followed by a blank line:")
sentinel = ''
pyramid = '\n'.join(iter(input, sentinel))
pyramid = pyramid.split('\n')
new_pyramid = []
for x in pyramid:
	new_pyramid.append(x.split(' '))

def combine_lines(line1, line2):
	result = []
	for i, x in enumerate(line2):
		val1 = x + line1[i]
		val2 = x + line1[i + 1]
		result.append(max(val1, val2))
	return result

def to_num(arr):
        result = []
        for x in arr:
                if type(x) is list:
                        result.append(to_num(x))
                else:
                        result.append(int(x))
        return result

pyramid = to_num(new_pyramid)


#combine_lines(pyramid[len(pyramid) - 1], pyramid[len(pyramid) - 2])
pyramid.reverse()
while len(pyramid) > 1:
	pyramid[1] = combine_lines(pyramid[0], pyramid[1])
	del pyramid[0]

print("The maximum possible sum is", str(pyramid[0][0]))
