
a=[]
size=int(input("Enter size of the element"))
 
i=0
while i<=size:
    val=int(input("Enter Number"))
    a.append(val)
    i=i+1

maxval=max(a)
minval=min(a)

print("Max value in the list",maxval)
print("Min value in the list",minval)

