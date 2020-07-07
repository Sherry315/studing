#!/usr/bin/env Python
# coding=utf-8

from math import sqrt

def prime(n):
	if n <=1:
		return False
	for i in range(2,int(sqrt(n)+1)):
		if n%i ==0:
			return False
	return True
	
primes = [i for i in range(2,100) if prime(i)]
print primes