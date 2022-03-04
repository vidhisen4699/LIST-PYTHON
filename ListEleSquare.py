# Given a list of numbers. write a program to turn every item of a list into its square.
numbers = [1, 2, 3, 4, 5, 6, 7]
result=[]
i=1
while i<len(numbers):
    result.append(i*i)
    i=i+1
print(result)
    
