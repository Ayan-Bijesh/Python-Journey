# Conversion between Celsius and Fahrenheit
unit = input("Enter the temperature unit the value needs to be converted to (C/F): ")
value = float(input("Enter the value to be converted: "))
if unit == "C":
    result = round((value - 32) * 5/9, 3)
    print(f"The given value in Celsius is {result}℃.")
elif unit == "F":
    result = round((value * 9/5) + 32, 3)
    print(f"The given value in Fahrenheit is {result}℉.")
else:
    print("Invalid unit.")