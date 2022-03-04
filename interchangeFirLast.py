
newList=[]
size=int(input("Enter size of the list:"))

i=0
while i<=size:
    val=int(input("Enter Number"))
    newList.append(val)
    i=i+1

i=0
while i<len(newList):
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    i=i+1
print(newList)    