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
#base = float(input("Enter the base of the triangle: "))
#height = float(input("Enter the height of the triangle: "))

# Calculate and display the area
#print("The area of the triangle is:", calculate_area_triangle(base, height))

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
#principal = float(input("Enter the principal amount: "))
#rate = float(input("Enter the rate of interest (as a percentage): "))
#years = float(input("Enter the time in years: "))
# Calculate and display the simple interest
#print("The simple interest is:", simple_interest(principal, rate, years))

# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.
def apply_discount(price, discount):
    """
    Apply a discount to a given price.
    :param price: The original price of the product
    :param discount: The discount percentage (from 0 to 100)
    :return: The new price after applying the discount
    """
    return price - (price * discount / 100)


print('Exercise 3:', apply_discount(100, 25))
print('Exercise 3:', apply_discount(80, 10))

# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.
def convert_temperature(temperature, unit):
    """
    Convert temperature between Celsius and Fahrenheit.
    :param temperature: The temperature to convert
    :param unit: The unit of the temperature ('C' for Celsius, 'F' for Fahrenheit)
    :return: The converted temperature
    """
    if unit == 'C':
        return (temperature * 9/5) + 32
    elif unit == 'F':
        return (temperature - 32) * 5/9
    else:
        raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit.")


print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.
def sum_to(n):
    """
    Calculate the sum of all integers from 1 to n.
    :param n: The upper limit
    :return: The sum of integers from 1 to n
    """
    return sum(range(1, n + 1))


print('Exercise 5:', sum_to(6))
print('Exercise 5:', sum_to(10))
# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments 
# and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.
def largest (a, b, c):
    """
    Find the largest of three integers.
    :param a: First integer
    :param b: Second integer
    :param c: Third integer
    :return: The largest integer
    """
    return max(a, b, c)


print('Exercise 6:', largest(1, 2, 3))
print('Exercise 6:', largest(10, 4, 2))

# Exercise 7: Calculate a Tip
#
# Create a function called `calculate_tip`. It should 
# take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.
#
# Examples:
# calculate_tip(50, 20) should return 10.
#
# Write your function and test its output below.
def calculate_tip(bill_amount, tip_percentage):
    """
    Calculate the tip based on the bill amount and tip percentage.
    :param
    bill_amount: The total bill amount
    :param tip_percentage: The tip percentage (as a whole number)
    :return: The calculated tip
    """
    return (bill_amount * tip_percentage) / 100


print('Exercise 7:', calculate_tip(50, 20))

# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes
# an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.
def product (*args):
    """
    :function - Calculate the product of an arbitrary number of numbers.
    :param args: The numbers to multiply
    :return: The product of the numbers
    """
    result = 1
    for number in args:
        result *= number
    return result
print('Exercise 8:', product(-1, 4))
print('Exercise 8:', product(2, 5, 5))

# Exercise 9: Basic Calculator
#
# Create a function named `basic_calculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basic_calculator(10, 5, 'subtract') should return 5.
# basic_calculator(10, 5, 'add') should return 15.
# basic_calculator(10, 5, 'multiply') should return 50.
# basic_calculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.
def basic_calculator(num1, num2, operation):
    """
    Perform basic arithmetic operations based on the provided operation.
    :param num1: The first number
    :param num2: The second number
    :param operation: The operation to perform ('add', 'subtract', 'multiply', 'divide')
    :return: The result of the operation
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'.")

print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))
print('Exercise 9 Result:', basic_calculator(10, 5, "add"))
print('Exercise 9 Result:', basic_calculator(10, 5, "multiply"))
print('Exercise 9 Result:', basic_calculator(10, 5, "divide"))

