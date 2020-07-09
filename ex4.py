#!/usr/bin/env python
#coding=utf-8
"""
calculate the 100th digit of the Fibonacci sequence

"""
a = 1
b = 1

for i in range(99):
	a,b = b,a+b
	
print (a)