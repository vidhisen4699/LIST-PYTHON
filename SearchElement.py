a=[]
size=int(input('Enter size of the List'))

for i in range(size):
    val=int(input('Enter Number'))
    a.append(val)
key=int(input('Enter Number to Search'))
flag=0
pos=0
for i in range(size):
    if (a[i]==key):
        flag=1
        pos=i+1
        break
    if flag==1:
        print('Element found at:',pos,'positive')
    else:
        print('Element not found')



