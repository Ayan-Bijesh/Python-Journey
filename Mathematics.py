apples = 6
# Normal vs augmented assignment operator.

# Addition
sum_apples = apples + 1
sum_apples += 1
# Subtraction
diff_apples = apples - 1
diff_apples -= 1
# Multiplication
product_apples = apples * 2
product_apples *= 2
# Division
quo_apples = apples / 2
quo_apples /= 2
# Exponents
expo_apples = apples ** 2
expo_apples **= 2
# Modulus (remainder)
remainder = apples % 2
remainder %= 2

# Built-in functions
x = 3.14
y = -4
z = 5
# Round function
print(round(x))
# Absolute value (distance away from 0)
print(abs(y))
# Power function (raise the base to the given power)
print(pow(3,4))
# Max and Min functions
print(max(x,y,z))
print(min(x,y,z))

# Math functions by importing
import math
x = 9
y = 8.3

# Value of pi
print(math.pi)
# Value of e
print(math.e)
# To find square root
print(math.sqrt(x))
# To find lower and upper round off
print(math.ceil(y))
print(math.floor(y))
# Exercises
# To find the circumference of a circle

radius = float(input("Enter radius: "))
circumference = 2 * math.pi * radius
print(f"The circumference of a circle with radius {radius}cm is {round(circumference,2)}cm")

# To find area of a circle
radius = float(input("Enter radius: "))
area = math.pi * radius**2
print(f"The area of the circle is {round(area,2)}cm^2")

# To find hypotenuse of a triangle
l = float(input("Enter length of a triangle: "))
b = float(input("Enter breadth of a triangle: "))
h = math.sqrt(pow(l,2)+pow(b,2))
print(f"The length of the third side is {round(h)}cm.")

