
def add_numbers(num1=2,num2=1):
    sum = num1 + num2
    print("Sum: ", sum)
    
    
add_numbers(10)
add_numbers(10,20)
add_numbers()



def find_sqaure(num):
    result = num * num
    return result

a = find_sqaure(5)
print("Square: ", a) 
print(result)


def find_max(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print(f"The maximum number among {x}, {y} and {z} is: {find_max(x,y,z)}")

def outer():
    y = 20  # enclosing variable
    
    def inner():
        x = 10  # local variable
        print("Inner function:", x)
        print("Enclosing variable:", y)
    inner()