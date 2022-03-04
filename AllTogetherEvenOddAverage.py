'''Write a code that works for all lists. It should print the output as the following like for all the odd numbers and all the even numbers and for all the numbers in the given list, it should calculate the following :

count
sum
average
and then print it.

Sample Output:
count of odd numbers ….
count of even numbers ….
count of all the numbers ….
sum of odd numbers ….
sum of even numbers ….
sum of all the numbers ….
average of odd numbers ….
average of even numbers ….
average of all the numbers ka ….
'''

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
        print('List of the even numbers',evenList)
        print('total of the even numvers',even)
        print('average of the even numbers',even_average)
    else:
        oddList.append(i)
        odd=odd+i
        odd_average=odd/len(oddList)
        print('List of the odd numbers',oddList)
        print('total of the odd numvers',odd)
        print('average of the even numbers',odd_average)
    i=i+1 



