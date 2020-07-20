#!/usr/bin/env Python
#--coding=utf-8--

from new_class import Person
from new_class import CsvReader
from new_class import TxtReader
from new_class import ZipReader

def get_info(file_name_csv, file_name_zip, file_name_txt):
    
    """
    csvfile = reader.read_from_csv(file_name_csv)
    zipfile = reader.read_from_zip(file_name_zip)
    txtfile = reader.read_from_txt(file_name_txt)
    """

    csv_reader = CsvReader(file_name_csv)
    zip_reader = ZipReader(file_name_zip)
    txt_reader = TxtReader(file_name_txt)

    csvfile = csv_reader.read()
    zipfile = zip_reader.read()
    txtfile = txt_reader.read()

    chart_of_person = csvfile + zipfile + txtfile

    return chart_of_person

from new_class import Josephus
file_name_txt = r"F:\吴穹\studing\test.txt"
file_name_csv = r"‪F:\吴穹\studing\test.csv"
file_name_zip = r"‪F:\吴穹\studing\test.zip"

people = get_info(file_name_csv, file_name_zip, file_name_txt)
start = 1
step = 3
josephus = Josephus(people, start, step)
print("out:",josephus.pop())
print("out in order:")
[x.display() for x in josephus]
