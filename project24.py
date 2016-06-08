#!/usr/bin/env python3

import time
from itertools import permutations
start = time.time()

digits = list(range(10))

permutation_list = list(permutations(digits))
permutation_list.sort()
print("The 1,000,000th permutation in lexicographic order is " + ''.join(map(str, permutation_list[999999])))
