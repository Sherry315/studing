#!/usr/bin/env Python
# coding=utf-8

import csv
import os
import zipfile       

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
    def __str__(self): 
        return "{} {} {}".format(self._name, self._gender, self._age)
    def display(self):
        print("name:{} gender:{} age:{}".format(self._name, self._gender, self._age))


class Josephus(object):
    def __init__(self, people, start = 1, step = 1):
        self._people = people
        self.start = start
        self.step = step
    
    @property
    def append(self, person):
        self._people.append(person)
    def total_number(self):
        return len(self._people)
    def pop(self):
        out_number = (self.start + self.step -1) % self.total_number()
        return self._people.pop(out_number)
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.total_number() > 0:
            return self._people.pop()
        else:
            raise StopIteration


def create_info_str(str_name):
    chart_of_person = []
    for i in range(len(str_name)):
        chart_of_person.append(Person(str_name[i].split(" ")[0], str_name[i].split(" ")[1], str_name[i].split(" ")[2]))
    return chart_of_person

    
class ZipReader(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        flag = zipfile.is_zipfile(self.file_path)
        chart_zip =[]
        if flag:
            zip_file = zipfile.ZipFile(self.file_path, "r")
            file_to_be_read = zip_file.namelist()[0]
            personal_information = []
            for line in file_to_be_read:
                personal_information.append(line.strip('\n'))
            file_to_be_read.close()
            chart_zip = create_info_str(personal_information)
        return chart_zip

class TxtReader(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        flag = os.path.isfile(self.file_path)
        chart_txt = []
        if flag:
            personal_information = open(self.file_path)
            document = []
            for line in personal_information:
                document.append(line.strip('\n'))
            personal_information.close()
            chart_txt = create_info_str(document)
            return chart_txt

class CsvReader(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        flag = os.path.isfile(self.file_path)
        chart_csv = []
        if flag:
            with open(self.file_path, "r") as f:
                messages = csv.reader(f)
                document = []
                for line in messages:
                    # document.append(line.strip('\n'))  #csv seperated by ","
                    document.append(line.strip('\n'))
            chart_csv = create_info_str(document)
        return chart_csv
                

