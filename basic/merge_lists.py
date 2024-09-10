# Ex 10: Merge two lists using  condition
# write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

merged = [x for x in list1 if x%2 == 1]+[x for x in list2 if x%2 == 0]
print(merged)