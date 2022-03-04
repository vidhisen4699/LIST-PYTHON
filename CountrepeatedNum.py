myList=[12,23,22,12,23,44,55,55,44,77]
x=12
count=0
for ele in myList:
    if ele==x:
        count=count+1
print('{} has occured {} times'.format(x,count))
