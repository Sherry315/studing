#!/usr/bin/env Python
# coding=utf-8

from math import sqrt

def get_prime(n):
	if n <=1:
		return False
	up_bound = int(sqrt(n)+1)
	for x in range(2,up_bound+1):
		if n%x ==0:
			return False
	return True
	
primes_within_100 = [x for x in range(2,101) if get_prime(x)]
print primes_within_100