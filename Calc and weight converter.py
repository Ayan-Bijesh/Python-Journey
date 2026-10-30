# Python calculator

operator = input("Enter the operator (+,-,*,/): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if operator == "+":
    print(round(num1 + num2, 3))
elif operator == "-":
    print(round(num1 - num2, 3))
elif operator == "*":
    print(round(num1 * num2, 3))
elif operator == "/":
    print(round(num1 // num2, 3))
else:
    print("Invalid operator.")

# Python weight converter

unit = input("Enter your preferred weight unit (kgs,lbs): ")
to_convert = float(input("Enter the weight to be converted: "))
if unit == "kgs":
    result = round(to_convert // 2.20462, 2)
    print(f"The entered weight in kilograms is {result}")
elif unit == "lbs":
    result = round(to_convert * 2.20462, 2)
    print(f"The entered weight in pounds is {result}")
else:
    print("Invalid unit.")