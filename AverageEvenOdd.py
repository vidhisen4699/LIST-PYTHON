'''Write a code that works for any list, it shows the two averages as the output. One is the average of even numbers and the other is the average of odd numbers from the given list.
   elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] '''

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
        even_average=even/len(evenList)
    else:
        oddList.append(i)
        odd=odd+i
        odd_average=odd/len(oddList)
    i=i+1 

print(evenList,even,even_average)
print(oddList,odd,odd_average)



