student = ('Ravi',34,"Delhi","India","IT","Delhi")
print("student tuple, student", student)

print("Nmae",student[0])
print(" address details:", student[2:4])    # tuple slicing

if "A" in student:     #Mmeberhsip Test
    print("A is present in the tuple")
    
for a in student:          # for-in loop
    print("value:", a)
    
print("Length of the tuple:", len(student))

print(" Occuracingin the the student tuple", student.count("Delhi"))

print("Index of IT in the tuple:", student.index("IT"))


# Tuple to list conversion
student_list = list(student)    # converting the tuple to list
student_list.append("WIPRO Technologies")
student_list[3] = "Bangalore"
print( "The list is ", student_list)

# convert back to tuple from the list
student = tuple(student_list)
print("The modified tuple is ", student)

project_codes = ('P001', 'P002', 'P003') # another tuple
complete_tuple = student + project_codes  # concatenation of tuples
print("The complete tuple after concatenation is ", complete_tuple)

#tuple within the tuple = nested tuples
studdent_nested = (student, project_codes)
print("The nested tuple is ", studdent_nested)
print("Accessing nested tuple element:", studdent_nested[0][1])  # accessing
print("Accessing nested 2nd tuple element:", studdent_nested[1][1])  # accessing
print(student)

#Unpacking the tuple
name, age, city, country, dept, state, org = student
print("Unpacked Values - Name:", name, ", Age:", age, ", City:", city, ", Country:", country, ", Dept:", dept, ", State:", state)

scores = (56,89,23,90,87,66)
print("Minimum score:", min(scores))
print("Maximum score:", max(scores))
print("Sum of scores:", sum(scores))

#extended tuple unpacking = advanced operation
a, b, c, *rest = scores
print("a:", a)
print("b:", b)  
print("c:", c)
print("rest:", rest)  # rest will be a list of remaining elements

# comparision of tuples
print((3,4,5) == (3,4,5))
print((6,7,4) == (6,7,1))

s = list(scores)
s.sort
print(s)

# comparision of tuples
print((3,4,5) > (3,4,5))
print((6,7,4) > (6,7,1))

