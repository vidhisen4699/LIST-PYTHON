'''def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()
'''

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
newlist=[]

i=0
while i<len(list):
    newlist.append(i**2)
    i=i+1
print(list[:5])
print(list[-5:])

