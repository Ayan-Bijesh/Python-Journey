# Calculator which produces the area of a rectangle with user given input.

length = int(input("Enter the length of a rectangle:"))
breadth = int(input("Enter the breadth of a rectangle:"))
area = length * breadth
print(f"The area of a rectangle with length {length}cm and breadth {breadth}cm is {area}cm^2")

# A shopping cart and the total bill

item = input("Enter the desired item:")
price = int(input("Enter the price of your desired item:"))
quantity = int(input("Enter the quantity of your desired item:"))
total_bill = price * quantity
print(f"You have bought {quantity} {item}s.")
print(f"Your total bill is ${total_bill}.")