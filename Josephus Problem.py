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
    if n ==1:
        return n
    return Josephus(n - 1, k) + k - 1 % n +1

total_num = int(input("enter total number of people:"))
kill_num = int(input("enter the kill number:"))
survivor = Josephus(total_num,kill_num)
print("survivor number:{}").format(survivor)
