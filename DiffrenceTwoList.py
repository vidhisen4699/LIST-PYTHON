# Diffrence between two List

list1=[1,2,5,7,9,12]
list2=[6,7,3,90,12,23,34,45]
diff_List1_List2=list(set(list1)-set(list2))
diff_List2_List1=list(set(list2)-set(list1))
Total=diff_List2_List1+diff_List1_List2
print("Diffrence between two List:",Total)