# '''Write a code that prints the maximum in this list.'''


# ''' USING FOR LOOP................................
# a=[]
# Size=int(input("Enter size of the list:"))
# for i in range(Size):
#     val=int(input("Enter Number"))
#     a.append(val)
# max=a[0]
# for i in range(Size):
#     if(a[i]>max):
#         max=a[i]
# print("Max Number=",max)        

# '''

# #........USING WHILE LOOP............................

a=[]
Size=int(input("Enter size of the list:"))

i=0
while i<=Size:
    val=int(input("Enter Number"))
    a.append(val)
    max=a[i]
    i=i+1

i=0
while i<=Size:
    if(a[i]>max):
        max=a[i]
    i=i+1  
print("Max Number=",max)        
 










