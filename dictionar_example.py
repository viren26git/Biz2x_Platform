product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 80000,
    "specs": {
        "RAM": "16GB",
        "Storage": "512GB SSD",
        "Processor": "Intel i7"
    }
}

print("Product Name:", product["name"])  # passing the key to print the attribute value
print("Product Brand:", product.get("brand"))  # another way to access the value using get()
print("Product Price:", product["price"])
print("Product Specs:", product["specs"])
print("Product RAM:", product["specs"]["RAM"])  # accessing nested dictionary value

product["stock"] = 50  # adding a new key-value pair
print("Updated Product Dictionary:", product)

if "brand" in product:
    print("Brand is present in the product dictionary", product["brand"])
else:
    print(" The brand  key doesnt exst in the product dictionary")
    
print(product.keys()) # printing all the keys

product["price"] = 75000  # updating the price
print("Updated Price:", product["price"])
print(product)

for key, value in product.items():  # iterating through the dictionary
    print(f"{key}: {value}")
    
product.pop("stock")
print(product)

keys = list(product.keys())
print(product[keys[0]]) # accessing value using the first key from the keys list

values = product.values()
print("All values in the product dictionary:", type(values))

a= product.copy()  # copying the dictionary
print("Copied Product Dictionary:", a)

del product["price"]

# merging two dictionaries objects
warranty = {
    "Name": "Laptop",
    "brand": "Dell",
    "period": "2 year",
    "extended": "1 year",
}

product.update(warranty)
print("Merged Product Dictionary with Warranty:", product)

product.clear()  # clearing the dictionary
print("Cleared Product Dictionary:", product)
