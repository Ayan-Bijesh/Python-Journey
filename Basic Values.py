# This is my first Python program
print("I like burgers!")
print("It's really good!")
### Variables and f strings
# A Variable = a container for a value (string,integer,float,boolean)
#              a variable behaves as if it was the value it contains

# Strings
first_name = "Ayan"
food = "burgers"
email = "ayanbijesh.codes@gmail.com"
print(first_name)
print(f"Hello {first_name}")
print(f"You like {food},don't you?")
print(f"Your email is: {email}")

# Integers
age = 14
quantity = 3
num_of_students = 22
print(f"You are {age} years old.")
print(f"You are buying {quantity} apples.")
print(f"There are {num_of_students} students in class 9.")

# Float (Floating point numbers)
price = 1.99
gpa = 3.8
distance = 5959.02
print(f"the price of one apple is ${price}.")
print(f"my gpa is: {gpa}")
print(f"the distance between India and Japan is {distance} kilometres.")

# Boolean
is_student = True
print(f"Are you a student?: {is_student}")
if is_student:
    print("You are a student.")
else:
    print("You are not a student.")
for_sale = False
if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")
is_online = True
if is_online:
    print("That person is online.")
else:
    print("That person is offline.")