#!/usr/bin/env python
#coding=utf-8

import random

score = [random.randint(0,100) for i in range(40)]
print score

num = len(score)
sumup = sum(score)
ave = sumup/num
less = len([i for i in score if i<ave])

print "The average score is :{}" .format(ave)
print "The number of student whose score is less than average is:{}" .format(less)

sort = sorted(score,reverse=True)
print sort