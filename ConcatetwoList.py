list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
#Expected output:
#  ['My', 'name', 'is', 'Kelly']

'''Use the zip() function. This function takes two or more iterables (like list, dict, string),
    aggregates them in a tuple, and returns it.'''

list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)