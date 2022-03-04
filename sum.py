# Que:1) Write a Python program to sum all the items in a list. 
list=[1,2,3,4,5,6,7,8,9,10]
sum=0
i=0
while i<len(list):
    sum=sum+list[i]
    i=i+1
print('Sum of the items in this list',sum)    