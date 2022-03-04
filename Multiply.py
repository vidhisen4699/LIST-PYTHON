# Que:2). Write a Python program to multiply all the items in a list. 

list=[1,2,3,4,5,6,7,8,9,10]
multiply=1
i=0
while i<len(list):
    multiply=multiply*list[i]
    i=i+1
print('Multiplying of the numbers',multiply)    