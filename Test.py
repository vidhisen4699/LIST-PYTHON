 # ques:1) reverse the Number
'''list=[1,2,3,4,5]    
print(list[::-1])
'''
''' 
list=[1,2,3,4,5,6,7,8]
list1=[]
i=1
while i<len(list)+1:
    list1.append(list[-i])
    i=i+1
print(list1)    
   ''' 

# Que:2) palindrom of the string
'''
value=['mom']
if(value[::-1]==value):
    print('yes')
else:
    print('no')  
'''

# Que:3) Unique Number in this list
'''
lst=[1,2,11,33,33,44,5,6,6,5,6,7]
print("Input List:",lst)

lst1=[]
count=0

for i in lst:
    if i not in lst1:
        count=count+1
        lst1.append(i)
print('output list:',lst1)
print("No. of unique items are:",count)        '''