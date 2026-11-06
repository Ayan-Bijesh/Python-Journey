# Conditional expression = A one-line shortcut for the if-else statement(ternary operator)
#                          Print or assign one of the two values based on a condition.
#                          X if condition else Y
num = 5
print("Positive" if num > 0 else "Negative")
num_2 = 7
result = "Even" if (num_2 % 2 == 0) else "Odd"
print(result)
a = 6
b = 7
max_num = a if a > b else b
print(max_num)
min_num = a if a < b else b
print(min_num)
age = 25
status = "Adult" if age >= 18 else "Child"
print(status)
temp = 25
weather = "Hot" if temp > 20 else "Cold"
print(weather)
user_role = "admin"
access_level = "Full access" if user_role == "admin" else "Limited access"