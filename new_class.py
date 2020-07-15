#!/usr/bin/env Python
# coding=utf-8

class Person(object):
    def __init__(self, name, gender, age):
        self._name = name
        self._gender = gender
        self._age = age
    
    def get_name(self):
        return self._name
    def get_gender(self):
        return self._gender
    def get_age(self):
        return self._age
    def display(self):
        print("name:{} gender:{} age:{}".format(self._name, self._gender, self._age))


class Josephus(object):
    def __init__(self, start, step, people):
        self._people = people
        self.start = 1
        self.step = 1
    
    @property
    def append(self, person):
        self._people.append(person)
    def total_number(self):
        return len(self._people)
    def pop(self, person):
        out_number = (self.start + self.step -1) % self.total_number
        return self._people.pop(out_number)
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.total_number > 0:
            return self._people.pop()
        else:
            raise StopIteration



        


