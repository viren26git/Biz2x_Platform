def calcualte(num1, num2, num3):
    def find_square(n):    # nested functions
        return n * n
    
    def find_cube(n):
        return n * n * n
    
    cube = find_cube(num2)
    square = find_square(num1)
    
  
    return square, cube

a = int(input("Enter a number: "))
m = int(input("Enter a number: "))
n = int(input("Enter a number: "))

b, c = calcualte(a,m,n)
print(f"Square: {b}, Cube: {c}")


def outer():
    y = 20  # enclosing variable
    
    def inner():
        x = 10  # local variable
        print("Inner function:", x)
        print("Enclosing variable:", y)
    inner()

outer()
# print("Outer function:", x)  # x is not defined here, will raise an

d = 30  # gloal variable
def func():
    #global d
    d += 10
    print("Global variable:", d)
    
func()
print("Global variable outside function:", d)



# LEGB rule below:

x= "Global"

def outer(): 
    x2 = "Enclosing"
    
    def inner():
        x1 = "Local"
        print("Inner:", x)
        
    inner()
  
outer()