'''Write a code, that counts the numbers between 20 and 40 and then print its count.'''

num=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
c=0
while i<len(num):
    if 20<=num[i]<=40:
        c=c+1
    i+=1
print("Print the number between 20 to 40 are:",c)    
