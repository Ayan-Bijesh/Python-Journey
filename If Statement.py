# if = Do some code only IF some condition is true.
#      Else do something else

age = int(input("Enter your age: "))
if age>= 100:
    print("You're too old to sign up.")
elif age>= 18:
    print("You are signed up!")
elif age< 0:
    print("Invalid age.")
else:
    print("You must be 18+ to sign up.")

# Asking the user if they would like some food
response = input("Would you like some food?(Y/N)")
if response == "Y":
    print("Have some food!")
elif response == "N":
    print("No food for you!")
else:
    print("Invalid response.")

# Exercise
name = input("Enter your name: ")
if name == "":
    print("Please enter your name.")
else:
    print(f"Hello, {name}!")

# If statements with booleans
for_sale = True
if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")