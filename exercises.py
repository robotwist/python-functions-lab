# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.
def calculate_area_triangle(base, height):
    """
    Calculate the area of a triangle given its base and height.

    :param base: The base of the triangle
    :param height: The height of the triangle
    :return: The area of the triangle
    """
    return (base * height) / 2


print('Exercise 1:', calculate_area_triangle(10, 5))
print('Exercise 1:', calculate_area_triangle(7, 3))
# Ask the user for input
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate and display the area
print("The area of the triangle is:", calculate_area_triangle(base, height))

# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
#
# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.
def simple_interest(principal, rate, years):
    """
    Calculate simple interest given principal, rate of interest, and time.
    :param principal: The principal amount
    :param rate: The rate of interest (as a percentage)
    :param years: The time in years
    :return: The calculated simple interest
    
    
    """
    return (principal * rate * years) / 100


print('Exercise 2:', simple_interest(1000, 5, 2))
print('Exercise 2:', simple_interest(1500, 3.5, 5))
# Ask the user for input
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (as a percentage): "))
years = float(input("Enter the time in years: "))
# Calculate and display the simple interest
print("The simple interest is:", simple_interest(principal, rate, years))


