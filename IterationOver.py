'''Que:1). Iterate over both the values in a list and their indices
        grocery_list = ['flour','cheese','carrots']
Output:
#=> 0: flour
#=> 1: cheese
#=> 2: carrots
'''

grocery_list = ['flour','cheese','carrots']

i=0
while i<len(grocery_list):
    print(i,'=>',grocery_list[i])
    i=i+1
