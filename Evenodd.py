''' Write a code that works for any list, and that tells how many odd numbers and how many even numbers are there in a given list.
    elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]  '''

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
evenList=[]
oddList=[]

i=0
while i<=len(elements):
    if i%2==0:
        evenList.append(i)
    else:
        oddList.append(i)
    i=i+1

print("even list:",evenList)
print("Odd list:",oddList)            
