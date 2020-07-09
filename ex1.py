#!/usr/bin/env python
#coding=utf-8

get_test_list = [1,2,3,4,5,6,7,8,9,0]

temporary_store = get_test_list.pop(0)

get_test_list.append(temporary_store)

print (get_test_list)

