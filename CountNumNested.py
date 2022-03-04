'''Count Number Of Elements In Nested Lists
In this section, you’ll learn how to count the number of elements in nested lists.

Nested lists are list which contains more than one sublists as items. You can count the number of elements in nested lists using the map function and the sum function.

First the map function applies a function to each item in the iterable.

In the below example, the map function applies the len() to each sub-lists available in the list a.

Then it sums all the returned values. Hence you’ll get the number of elements in the nested list.
'''

a = [[3,4],[1,2],[55,66,77]]
print(sum(map(len,a)))