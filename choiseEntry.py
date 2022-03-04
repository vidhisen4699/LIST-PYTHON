# choise if you want to add the items and not so spot and print the final list.



list=[]
while True:
    element=input('Enter element')
    list.append(element)
    choise=input("want to quit? press yes,otherwise press another key")
    if choise=='yes':
        break
print("List is:",list)

