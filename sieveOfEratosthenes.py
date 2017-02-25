'''
Sieve of Eratosthenes
Author: John Larkin
Date: 2/21/17
Purpose: 
	This is a clever sieve algorithm to effectively find all of the numbers below some threshold that are prime. 

'''

import sys
import math

try:
	n = int(raw_input("What is the number to find primes below?: "))
except:
	print("That is not a valid integer. The program is halting.")
	sys.exit(0)

if n < 2:
	print("The range is not valid (<2). The program is halting.")
	sys.exit(0)

a = [True] * n

upper_limit = int(math.ceil(math.sqrt(n)))

for i in range(2, upper_limit):
	if a[i]:
		for j in range(i**2, n, i):
			a[j] = False

ans = [i for i, val in enumerate(a) if val]
print("Our primes are: {}".format(ans))
