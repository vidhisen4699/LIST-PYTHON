l=[1,2,3,4,5,6,7,8,9,10]
b=[]
i=0
c=0
while i<len(l):
    b.append(l[i])
    if c==3:
        b.append('20')
        c-=4
    c=c+1
    i=i+1
print(b)        