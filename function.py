# Write a function call max_of_three that takes three parameters
# as input an returns the largest of the three. The function
# use conditional statements to compare the values and 
# determine the greatest.

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a>=b and a>=c:
    print("The greatest number: is", a)
elif b>=a and b>=c:
    print("The greatest number: is", b)
else:
    print("The greatest number is:", c)
