a=[]
size=int(input('Enter the size'))

for i in range(size):
    val=int(input('Enter Number'))
    a.append(val)
key=int(input('enter number to find frequency'))
count=0
for i in range(size):
    if (a[i]==key):
        count=count+1
print('Frequency=',count)         