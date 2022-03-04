list=[1,4,6,3,3,5,1,4]
unique_List=[]
print('previous list',list)
for a in list:
    if a not in unique_List:
        unique_List.append(a)
print("After Calculation list:",unique_List)
