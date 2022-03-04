# Que:20). Write a Python program access the index of a list. 
from operator import index

list=[1,4,7,3,44,5,66,8]
i=0
while i<len(list):
    print(list[i],index(i))
    i=i+1