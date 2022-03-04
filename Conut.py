char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i=1
# char=[]
# while i<=len(char_list):
#     print(char_list.count(append.char_list))
#     i=i+1
# print(char_list.count())

count=0
temp=0
index=0
for x in range(0,list):
    temp =list.count(list[x])

    if (temp>count):
        count=temp
        index=x

mostFrequentNumber=list[index]
print('The most frequent number of list is:',mostFrequentNumber)
print("The number appeared",count,'time in list')
