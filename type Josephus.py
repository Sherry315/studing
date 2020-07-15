#!/usr/bin/env Python
# coding=utf-8

def get_info(file_name):
    from new_class import Person

    personal_information_document = open(file_name)
    personal_information = []
    for line in personal_information_document.readline():
        personal_information.append(line.strip('\n'))
    personal_information_document.close()

    chart_of_person = []
    for i in range(len(personal_information)):
        chart_of_person.append(Person(personal_information[i].split(" "[0]), personal_information[i].split(" "[1]), personal_information[i].split(" "[2])))
    return chart_of_person

from new_class import Josephus
file_name = "information.txt"

people = get_info(file_name)
josephus = Josephus(start, step, people)
print("out:",josephus.pop())
print("out in order:")
[x.display() for x in josephus]
