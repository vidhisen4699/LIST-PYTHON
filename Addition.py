# Sum of the element in the List 

#.........USING OF FOR LOOP..........................................

a=[]
size=int(input("How many element you want to enter"))
for i in range(size):
    val=int(input("Enter Number"))
    a.append(val)
sum=0
for i in range(size):
    sum=sum+a[i]
print("Sum of list element=",sum)


#.........USING OF WHILE LOOP..........................................

a=[]
size=int(input("How Many element you want to enter"))
i=0 
while i<size:
    val=int(input("Enter Number"))
    a.append(val)
    i=i+1
sum=0
while i<size:
    sum=sum+a[i]
print("Sum of the Number",sum)

