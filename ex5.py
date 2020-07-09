#!/usr/bin/env Python
# coding=utf-8

from math import sqrt

a = input("enter a:")
b = input("enter b:")
c = input("enter c:")
delta = b*b - 4*a*c

try:
	if delta<0:
		raise ValueError("delta under zero")
	else:
		x1 = (-b+sqrt(delta))/2*a
		x2 = (-b-sqrt(delta))/2*a
		print(x1,x2)
except ValueError as ex:
	print(ex)
