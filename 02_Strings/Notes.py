# Strings in Python

# 1. Creating Strings
# Strings can be created using single quotes, double quotes, or triple quotes.
single_quote_str = 'Hello, World!'
double_quote_str = "Hello, Python!"
triple_quote_str = '''This is a multi-line string.
It can span multiple lines.'''

# 2. String Operations

# Concatenation
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2  # Result: "Hello World"

# Repetition
repeated_str = str1 * 3  # Result: "HelloHelloHello"

# 3. String Methods
sample_str = "  Hello, Python!  "

# Strip whitespace
stripped_str = sample_str.strip()  # Result: "Hello, Python!"

# Convert to uppercase
upper_str = sample_str.upper()  # Result: "  HELLO, PYTHON!

# Convert to lowercase
lower_str = sample_str.lower()  # Result: "  hello, python!  "

# Replace substring
replaced_str = sample_str.replace("Python", "World")  # Result: "  Hello, World!  "

# Split string
split_str = sample_str.split(",")  # Result: ['  Hello', ' Python!  '] it will split at the comma and store in a list

# Join list into string
words = ['Hello', 'World']
joined_str = " ".join(words)  # Result: "Hello World" it will join the list elements with a space in between

# 4. String Formatting (f-strings)
name = "Alice"
age = 30
formatted_str = f"My name is {name} and I am {age} years old."  # Result: "My name is Alice and I am 30 years old."

# 5. String Indexing and Slicing
sample_str = "Hello, World!"
first_char = sample_str[0]            # Result: 'H'
last_char = sample_str[-1]            # Result: '!'
# slicing
substring = sample_str[0:5]           # Result: 'Hello'
# reverse slicing
reverse_str = sample_str[::-1]    # Result: '!dlroW ,olleH'
# step slicing
step_str = sample_str[::2]       # Result: 'Hlo ol!' (every second character)

# 6. String Length
length = len(sample_str)          # Result: 13

# 7. Escape Characters
escape_str = "He said, \"Hello, World!\"\nWelcome to Python."
# Result:
# He said, "Hello, World!"
# Welcome to Python.

# 8. Raw Strings
raw_str = r"C:\Users\Name\Documents"
# Result: 'C:\\Users\\Name\\Documents' (backslashes are treated literally)

# 9. Multiline Strings
multiline_str = """This is a string that spans
multiple lines."""
# Result:
# This is a string that spans
# multiple lines.

# 10. String Membership
is_hello_in_str = "Hello" in sample_str  # Result: True
is_python_in_str = "Python" in sample_str  # Result: False

# 11. String Comparison
str_a = "apple"
str_b = "banana"
is_equal = str_a == str_b        # Result: False
is_greater = str_a > str_b       # Result: False (lexicographical comparison) meaning 'a' comes before 'b'
is_less = str_a < str_b          # Result: True (lexicographical comparison)


# Note: These notes are AI-assisted and part of my learning process.