#!/usr/bin/env python
#coding=utf-8

test_str = "I  want  to  sleep."
print (test_str)

no_space_str = test_str.split(" ")
print (no_space_str)

seperated_str = [x for x in no_space_str if x!=""]
print (seperated_str)

new_str = " ".join(seperated_str)
print (new_str)