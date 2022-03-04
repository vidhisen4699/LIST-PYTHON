# Que:30) Write a Python program to get the frequency of the elements in a list.

import collections
list=[10,10,30,40,40,43,43,43,43,43,56,56,5,63,2,3]
print("Original List",list)
print("Frequancy of the digits")
ctr=collections.Counter(list)
print(ctr)

# import collections
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# print("Original List :",my_list)
# ctr = collections.Counter(my_list)
# print("Frequency of the elements in the List : ",ctr)
