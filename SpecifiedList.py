# Que:12). Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Expected Output : ['Green', 'White', 'Black']

list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
newlist=[]
for i in list:
    if i not in ('Red','Pink','Yellow'):
        newlist.append(i)
print(newlist)    




