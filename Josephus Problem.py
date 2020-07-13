#!/usr/bin/env Python
# coding=utf-8
"""
out_number = 3
total_number = 10
for i in range(total_number +1):
    List[i] = input("input name:")
index = 1
print(List)

while len(List) != 1:
    temp = List.pop()
    if index != out_number:
        List.append(temp)
    else:
        index = 0
    print(List)
    index +=index
"""
def Josephus(n,k):
    if n == 1:
        return n
    return (Josephus(n - 1, k) + k - 1) % n +1

number_of_participant = int(input("please input the number of participant:"))
list_of_participant = []
for i in range(number_of_participant):
    name = raw_input("please enter the name of participant:")
    list_of_participant.append(name)
    i +=i
print("names of participants:",list_of_participant)
kill_num = int(input("enter the kill number:"))
survivor_number = Josephus(number_of_participant,kill_num)
print("number of the survivor:",survivor_number)
survivor = list_of_participant[survivor_number - 1]
print("survivor :{}").format(survivor)
