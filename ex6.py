#!/usr/bin/env Python
# coding=utf-8

from __future__ import division

def average_score(scores):
	score_value = scores.values()
	sum_score = sum(score_value)
	average = sum_score/len(score_value)
	return average
	
def score_sort(scores):
	score_list = [(scores[x],x) for x in scores]
	sorted_list = sorted(score_list,reverse = True)
	return [(x[0],x[1]) for x in sorted_list]
	
def top_score(scores):
	score_list = score_sort(scores)
	max_score = score_list[0][1]
	return [(x[0],x[1]) for x in score_list if x[1]==max_score]
	
def bottom_score(scores):
	score_list = score_sort(scores)
	total_num = len(score_list)
	min_score = score_list[total_num-1][1]
	return [(x[0],x[1]) for x in score_list if x[1]==min_score]

"""
total_num = int(input("enter the number of student:"))
exam_result = {}
for i in range(total_num)
	student_name = input("enter student name:")
	student_score = input("enter score of {}:",format(student_name))
	exam_result[student_name] = student_score
	i +=i
"""

test_scores = {"a":82, "b":93, "c":60, "d":98, "e":98}

average = average_score(test_scores)
print("the average score is:{}".format(average))

sorted_scores = score_sort(test_scores)
print("the sorted scores are as follow:{}".format(sorted_scores))

top_student = top_score(test_scores)
print("the best student is:{}".format(top_student))

bottom_student = bottom_score(test_scores)
print("the bottom student is:{}".format(bottom_student))