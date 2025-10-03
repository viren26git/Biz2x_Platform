grocery = ["bread", "milk", "eggs", "butter","Buns","curd","12"]  # list of grocery items
print("Grocery List:", grocery)
grocery.sort()
print("Grocery List:", grocery)

# replcaing the element in the list 
index = grocery.index('butter')
print("Index of 'butter':", index)
grocery[index] = 'jam'  # updating butter to jam 
print("Updated Grocery List:", grocery)

grocery.pop()   # pop will remove the lst item from the list
print("Grocery List after pop():", grocery)

grocery.extend(['cookies', 'chocolates','milk'])  # adding multiple items to the list
print("Grocery List after extend():", grocery)

backup_list = grocery.copy()  # copying the list
print("Copied Grocery List:", backup_list)

changed_list = [item.upper() for item in grocery]   # list comprehension to convert items to uppercase
print("Changed Grocery List to Uppercase:", changed_list)

print("First item in the grocery list:", grocery[0])  # accessing the first item
print("Last item in the grocery list:", grocery[-1])  # accessing the last item

print("Number of items in the grocery list:", len(grocery))  # length of the list

print("first two items, grocery[:2]", grocery[:2])

grocery.insert(2, 'rice')  # inserting 'rice' at index 2
print("Grocery List after insert():", grocery)

grocery.remove('milk')  # removing 'milk' from the list 
print("Grocery List after remove():", grocery)

del grocery[3]  # deleting item at index 3
print("Grocery List after del:", grocery)

print("is eggs are there in the list or not?", 'eggs' in grocery)  # checking if 'eggs' is in the list

grocery.extend(['milk', 'chocolates','milk'])
print("Number of times 'milk' appears in the list:", grocery.count('milk'))  # count occurrences of 'milk'

grocery.reverse()  # reversing the list
print("Reversed Grocery List:", grocery)

grocery.clear()  # clearing the list
print("Cleared Grocery List:", grocery) 