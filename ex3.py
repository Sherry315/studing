#!/usr/bin/env python
#coding=utf-8

str = "I  want  to  sleep."
print str

no_space_str = str.split(" ")
print no_space_str

sep = [i for i in no_space_str if i!=""]
print sep

new = " ".join(sep)
print new