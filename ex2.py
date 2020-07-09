#!/usr/bin/env python
#coding=utf-8

import random

max_score = 100
total_num = 40
get_scores = [random.randint(0,max_score) for x in range(total_num)]
print (get_scores)

sumup = sum(get_scores)
average = sumup/total_num
number_under_average = len([x for x in get_scores if x<average])

print ("The average score is :{}" ).format(average)
print ("The number of student whose score is less than average is:{}") \
.format(number_under_average)

sort_scores = sorted(get_scores,reverse=True)
print (sort_scores)