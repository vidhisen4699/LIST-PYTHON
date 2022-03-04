'''
i=int(input("Enter"))
rev=0
x=i
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
if(rev==x):
    print("palindrom")
else:
    print("Not Palindrom")        
'''

'''s=input("Enter Number") 
revstr=(s[::-1]) 
if revstr==s:
    print("palindrom")
else:
    print("Not Palindrom")
'''


list =["mom",121,"saloni",434,"nayan","vidhi","dad",122]
palindrom=[]
notpalidrom=[]

palindrom=0
notpalidrom=0
i=0
while i<len(list):
    revstr=(list[::-1]) 
    if revstr==list[i]:
        palindrom.append(i)
        palindrom=palindrom+1
    else:
        notpalidrom.append(i)
        notpalidrom=notpalidrom+1
    i=i+1
print("List of palindrom Number",palindrom)
print("list of notPalindrom Number",notpalidrom)    

    


# list =["mom","saloni","nayan","vidhi","dad"]
# bubble short
# To-Do list
# picking unpicking