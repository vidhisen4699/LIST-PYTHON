x=[101,102,103,104,105,106,107]
print('origonal list')
n=len(x)

for i in range(n):
    print(i,'=',x[i])
print()

print("from 1st position to 4th position")
a=x[1:5]

for i in a:
    print(i)
print()


print("form 0th position to last position")
b=x[0:]
for i in b:
    print(i)
print()    


