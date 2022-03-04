'''a=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(a):
    if i==2 or i==3:
        i=i+1
    continue
print(i)
'''
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i == 3 or i==2:
      continue
    print(i)

 