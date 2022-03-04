# Que:)Write a Python program to count the number of elements in a list within a specified range.

list1 = [10,20,30,40,40,40,70,80,99]
list2 = ['a','b','c','d','e','f']

min=40           # Solve first list 40<100
max=100
ctr=0
for x in (list1):
    if min <= x <= max:
        ctr+= 1
print(ctr)

min='a'   # solve second list a<e
max='e'
ctr=0
for x in (list2):
    if min <= x <=max:
        ctr+=1
print(ctr)             
