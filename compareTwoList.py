listx1, listx2=[3, 7, 7, 9], [3, 5, 7, 9]
print (listx1 == listx2)

listx1, listx2=[9, 7, 5, 3], [3, 5, 7, 9]	#create two lists equal, but unsorted.
print(listx1 == listx2)

listx1, listx2 =[2, 3, 5, 7], [3, 5, 7, 9]	#create two different list
print(listx1 == listx2)

print(listx1.sort() == listx2.sort())	#order and compare
