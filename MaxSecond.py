
a=[]
size=int(input("Enter size of the list:"))

i=0
while i<=size:
    val=int(input("Enter Number"))
    a.append(val)
    i=i+1

maxval=max(a)
print("Mix value in list is:",maxval)
a.remove(maxval)
smax=max(a)
print("Second mix value in the list=",smax)

'''
a=[]
size=int(input("Enter size of the list:"))

i=0
while i<=size:
    val=int(input("Enter Number"))
    a.append(val)
    i=i+1

a.sort()
print("Mix value in list is:",a[size-1])
print("Second mix value in the list=",a[size-2])
'''