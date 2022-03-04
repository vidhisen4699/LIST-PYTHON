# check_even_odd=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# evenlist=[]
# oddlist=[]

# for i in check_even_odd:
#     if i%2==0:
#         evenlist.append(i)
#     else:
#         oddlist.append(i)
# print("Even Lists:",evenlist)
# print("Odd Lists:",oddlist)


check=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
evenlist=[]
oddlist=[]
i=0
while i<=len(check):
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
    i=i+1
print("Even Lists:",evenlist)
print("Odd Lists:",oddlist)