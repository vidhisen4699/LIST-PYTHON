''''Write a code that works for any list, it should give two sums as outputs, one is the sum of odd numbers present in the list and the other is the sum of even numbers present in the list.
    elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]  '''


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
evenList=[]
oddList=[]

i=0
even=0
odd=0
while i<=len(elements):
    if i%2==0:
        evenList.append(i)
        even=even+i
    else:
        oddList.append(i)
        odd=odd+i
    i=i+1

print("even list:",evenList,even)
print("Odd list:",oddList,odd)            
