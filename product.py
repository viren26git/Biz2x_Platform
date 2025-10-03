class Product:
    
    discount = 0   # self class attribute
    
    """def __init__(self,product_id,name,price,quantity):     # constructor with parameters
        self.product_id = product_id
        self.name = name
        self.price = price 
        self.quantity = quantity"""
        
    def __init__(self,*args):
        if len(args) == 0:
            self.product_id = None 
            self.name = None 
            self.price = None
        elif len(args) == 2:
            self.product_id, self.name = args
            self.price = 0
        elif len(args) == 4:
            self.product_id, self.name,self.price,self.country = args
        
       
    def display_product(self):                                  # 1st method to display product details
        print(f"Product id : {self.product_id}")
        print(f"Product name : {self.name}")
        print(f"Product price : {self.price}")
        print(f"Product quantity : {self.quantity}") 
        
    def apply_discount(self,discount_percentage):                 # 2nd method to apply discount on product price
        discount_amount = (self.price * discount_percentage) / 100
        discounted_price = self.price - discount_amount
        self.discount = discounted_price
        print(f"Discount amount: {discounted_price}")
    
    def total_value(self):
        return self.price * self.quantity
    

p = Product();
#print(f"{p.country}")
p1 = Product(104,'ABC')
# objects are defined outsid the class    
product1 = Product(101, 'Laptop', 80000, 'India')
print(f"{product1.country}")
print(""""""""""""""""""'')
product2 = Product(102, 'Smartphone', 50000, 20)
print(""""""""""""""""""'')

product1.display_product() 
print(""""""""""""""""""'')
product2.display_product()
print(""""""""""""""""""'')

product1.apply_discount(10)
print(""""""""""""""""""'')
product2.apply_discount(5)
print(""""""""""""""""""'')

product1.total_value()
print(f"Total value of {product1.name}: {product1.total_value()}")
print(""""""""""""""""""'')

product2.total_value()
print(f"Total value of {product2.name}: {product2.total_value()}")
