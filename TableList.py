list=[1,2,3,4,5]
newList=[]
i=1
while i<=len(list):
    j=1
    while j<=10:
        t=j*i
        newList.append(t)
        j=j+1
    i=i+1

print(newList)

'''

# copyMethod

original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)
'''

'''# Assending order

list=[1,5,8,6,4,9,12,7]
list.sort()
    
print(list)    
'''

'''
# List iterasion

list=['b','d']
num=input('Enter number')
i=0
while i<len(num):
    print(list)
    i=i+1

'''

'''
for listIteration in range(len(list)):
    print(listIteration)
'''




'''
list=['b','d']
num=int(input('Enter number'))
i=1
while i<len(num):
    print(('b'**i)+('d'**i))
    i=i+1
'''
'''
 # Addition
l1=[1,2,3,3,4]
l2=[2,3,4,5]
l3=[4,5,6,7]

print(list(l1+l2+l3))'''