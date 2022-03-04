
b=[]
txt=str.split("hello codder whatsup what to do today and what happend")
for i in txt:
    if (len(i)>5) :
        b.append(i)
print("list of words : ",b)