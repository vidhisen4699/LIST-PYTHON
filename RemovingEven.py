# list=[2,4,1,3,5,6,7,8,9,10,12,11,13,15,17,33]
# newlist=[]
# i=0
# while i<len(list):
#     if i%2==0:
#         list.remove(i)
#     else:
#         newlist.append(i)
    
num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)

'''
# second Method
list=[]
n=int(input('Enter Number'))
for i in range(0,n):
    item=int(input())
    list.append(item)
print('User list is:',list)
for i in list:
    if i%2==0:
        list.remove(i)
print('The new list is:',list)
print()

'''

