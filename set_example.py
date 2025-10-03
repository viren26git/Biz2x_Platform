products = {"laptop", "mobile", "tablet", "desktop", "smartwatch"}
print(products)

products.add("earbuds")  # adding an item to the set
products.add("earbuds")  # adding an item to the set
products.add("earbuds")  # adding an item to the set
print("After adding earbuds:", products)

products.remove("tablet")  # removing an item from the set
print("After removing tablet:", products)

prod = {"camera", "speaker","mobile", "laptop"}
result = products.union(prod)  # union of two sets
print("Union of products and prod:", result)

result = products.intersection(prod)  # intersection of two sets
print("Intersection of products and prod:", result)

print(products)
print(prod)

if products == prod:
    print("Both sets are equal")
else:
    print("Both sets are not equal")
    
set_A = {1, 3, 2, 4, 5}
set_B = {1, 2, 3, 4, 5}

if set_A == set_B:
    print("Both sets are equal")
else:
    print("Both sets are not equal")
    
products.pop() # pop will remove a random item from the set
print("After pop():", products)

print(products)
print(prod)

result2 = products.difference(prod)  # difference of two sets
print("Difference of products and prod:", result2)

result3 = products^prod  # symemtric difference of two sets means the uncommon elements from both the sets
print("symmnetric Difference of products and prod:", result3)

a = products.discard("desktop")  # discard will remove the item if present else will do nothing
print("After discarding desktop:", products)

products.update(prod) 
print(products)

products.clear()  # clearing the set
print("After clearing the set:", products)

del products   # deleting the entire set
#print("After deleting prod set", products)

