# Typecasting = the process of converting a value of one data type to another.
#               (string,integer,float,boolean)
#               Explicit vs Implicit

name = "Ayan"
age = 14
gpa = 3.8
student = True
# To configure the type of data
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))
# To cast data into another type and checking
age = float(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))

student = str(student)
print(student)
print(type(student))

age = bool(age)
print(age)
# This is because when int is converted to bool,if the int is any number other than 0,
# It is always true.
name = bool(name)
print(name)
# This is because when str is converted to bool,if the str is anything other than empty
# It would always be true.