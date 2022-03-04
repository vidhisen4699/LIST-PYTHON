

NumList=[]
Number=int(input("How Many element you want to enter"))
i=0 
while i<Number:
    value=int(input("Enter Number"))
    NumList.append(value)
    i=i+1

i = 0
while(i < Number):
    j = i + 1
    while(j < Number):
        if(NumList[i] > NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp
        j = j + 1
    i = i + 1

print("Element After Sorting List in Ascending Order is : ", NumList)
