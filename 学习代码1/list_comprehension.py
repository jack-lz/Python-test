#!/usr/bin/pyhton
#Filename: list_comprehension.py

listone = [2,3,4]
listtwo = [i*2 for i in listone if i>2]
print listtwo

listthree = []
for i in listone:
    if i > 2:
        listthree.append(i*2)

print listthree
