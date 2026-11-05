# Logical operators = used on conditional statements
#    and = checks if two or more conditions are True
#    or = checks if at least one condition is True
#    not = True if condition is False, and vice versa

# and operator
temp = 25
if temp > 0 and temp < 30:
    print("The temperature is good.")
else:
    print("The temperature is bad.")

# or operator
temp = 40
if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

# not operator
sunny = True
if not sunny:
    print("It is cloudy outside.")
else:
    print("It is sunny outside.")