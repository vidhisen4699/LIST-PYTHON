'''  How many Crorepati?
kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]

Write a program that tells in the above list that how many people are there in the above list who are :

1 - `Crorepati`
2 - `Lakhpati`
3 - `Dilwale`

All those who have money more than or equal to 1 crore are known as Crorepati. All those who have money money greater than or equal to 1 lakh, those are called Lakhpati. Rest of the people are called Dilwale.

For example, the output of the list given above is as follows.

4 Crorepati
3 Lakhpati
4 Dilwale
'''

kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
Crorepati=[]
Lakhpati=[]
Dilwale=[]

i=0
while i<=len(kitna_paisa_hai):
    if 10000000>=len(i):
        Crorepati.append(i)
        print(Crorepati)
    elif 1000000>=len(i):
        Lakhpati.append(i)
        print(Lakhpati) 
    else:
        print(Dilwale)  
        Dilwale.append(i)         
    i=i+1
