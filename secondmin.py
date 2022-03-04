
# a=[]
# Size=int(input("Enter size"))
# for i in range(Size):
#     val=int(input("Enter any Number"))
#     a.append(val)

# minval=min(a)
# print("min value in list is:",minval)
# a.remove(minval)
# smin=min(a)
# print("Second min value in the list=:",smin)





a=[]
Size=int(input("Enter size"))
i=0
while i<=Size:
    val=int(input("Enter any Number"))
    a.append(val)
    i=i+1

minval=min(a)
print("min value in list is:",minval)
a.remove(minval)
smin=min(a)
print("Second min value in the list=:",smin)




