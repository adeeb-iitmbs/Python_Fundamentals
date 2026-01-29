# Variables, Data Types and Some Basics of Python

# 1. Variables
# Variables are used to store data values and data values can be of different types.
x = 5               # Integer
y = 3.14            # Float
name = "Alice"      # String
is_student = True   # Boolean

# 2. Data Types
# Common data types in Python include:
# 1. Integer (int): Whole numbers, e.g., 1, -5, 100
# 2. Float (float): Decimal numbers, e.g., 3.14, -0.001, 2.0
# 3. String (str): Sequence of characters, e.g., "Hello", 'Python'
# 4. Boolean (bool): Represents True or False values

# keywords -
# In Python, keywords are reserved words that have special meaning and cannot be used as variable names.
# Examples of keywords: sum, in, for, if, else, while, return, etc.

# Comments -
# Comments are used to explain code and are ignored by the Python interpreter.
# Single-line comments start with the '#' symbol.
# This is a single-line comment

"""
This is a multi-line comment.
It can span multiple lines.
"""
# 3. Basic Input and Output
# Output
print("Hello, World!")  # Prints a string to the console
# Input
user_name = input("Enter your name: ")  # Takes input from the user
print(f"Hello, {user_name}!")  # Greets the user with their name

# 4. Basic Arithmetic Operations
a = 10
b = 3
addition = a + b          # Result: 13
subtraction = a - b       # Result: 7
multiplication = a * b    # Result: 30
division = a / b          # Result: 3.3333...
floor_division = a // b   # Result: 3
modulus = a % b           # Result: 1
exponentiation = a ** b   # Result: 1000

# 5. Type Conversion
num_str = "100"
num_int = int(num_str)      # Convert string to integer
num_float = float(num_str)  # Convert string to float
int_to_str = str(num_int)   # Convert integer to string
float_to_int = int(num_float)  # Convert float to integer
float_to_str = str(num_float)  # Convert float to string
int_to_float = float(num_int)  # Convert integer to float


# Note: These notes are AI-assisted and part of my learning process.