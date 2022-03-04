List=[1,33,23,44,23,22,23,45,44,44,1,1,1,1,2]
Result=[]
for i in List:
    if i not in Result:
        Result.append(i)
print(Result)


