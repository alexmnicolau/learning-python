# ============================================
# DAY 1 — What is Python and How Does It Work?
# ============================================
#
# Python is a programming language. You write instructions in a file,
# and the computer reads them top to bottom, one line at a time.
#
# This line you're reading right now is a COMMENT.
# Comments start with # and Python ignores them completely.
# They're notes for humans, not for the computer.
#
# To run this file, type in your terminal:
#   python3 ~/python-learning/day-01/lesson.py
#
# Let's start.


# === PART 1: print() — Talking to the Screen ===
#
# print() is a command that shows text on your screen.
# It's the first thing you learn because it's how you see results.

print("Hello, I am learning Python.")
print("My name is Alex.")
print("I am 29 years old")
print("This is my first Python project")

# Whatever you put inside the quotes, Python will display it.
# Try changing the text above and running the file again.


# === PART 2: Variables — Giving Names to Things ===
#
# A variable is a name that holds a value.
# Think of it like a labeled box — you put something in, and
# you can use the label to get it back later.

name = "Alex"
age = 28
city = "Bucharest"

# Now these three words (name, age, city) each hold a value.
# You can use them with print():

print(name)
print(age)
print(city)

# You can also change what's inside a variable:
city = "Dubai"
print(city)  # Now it prints Dubai, not Bucharest


# === PART 3: Types — Different Kinds of Values ===
#
# Not everything is the same kind of data. Python has types:
#
#   "hello"   → str   (string = text, always in quotes)
#   42        → int   (integer = whole number)
#   3.14      → float (decimal number)
#   True      → bool  (boolean = yes or no, True or False)

product = "Sunscreen SPF 50"    # str
price = 14.99                   # float
quantity = 3                    # int
in_stock = True                 # bool

# You can check the type of anything:
print(type(product))    # <class 'str'>
print(type(price))      # <class 'float'>
print(type(quantity))   # <class 'int'>
print(type(in_stock))   # <class 'bool'>


# === PART 4: Doing Math ===
#
# Python can do math with numbers:

a = 10
b = 3

print(a + b)    # 13  (addition)
print(a - b)    # 7   (subtraction)
print(a * b)    # 30  (multiplication)
print(a / b)    # 3.333... (division — always gives a decimal)
print(a // b)   # 3   (integer division — cuts off the decimal)
print(a % b)    # 1   (remainder — 10 divided by 3 = 3 remainder 1)


# === PART 5: Combining Text — f-strings ===
#
# Often you want to mix text with variables. Use f-strings:
# Put an f before the quotes, and use {curly braces} for variables.

name = "Alex"
age = 28 
print(f"My name is {name} and I am {age} years old.")

# Without the f, it would print the literal text {name} — not the value.
# The f tells Python: "look inside the braces and replace with real values."

product = "Sunscreen"
price = 14.99
print(f"The {product} costs {price} EUR.")


# === PART 6: Getting Input from the User ===
#
# input() lets you ask a question and wait for the user to type something.
# IMPORTANT: input() always gives you a string, even if they type a number.

# Uncomment the 3 lines below (remove the #) to try it:
# user_name = input("What is your name? ")
# print(f"Hello, {user_name}!")
# print(f"Your name has {len(user_name)} letters.")


# ============================================
# EXERCISES — Try these yourself!
# ============================================
#
# Exercise 1: Create a variable called "country" with the value "Romania"
#             and print it.
#
# Exercise 2: Create two number variables, multiply them, and print the result.
#
# Exercise 3: Use an f-string to print:
#             "I live in Bucharest, Romania"
#             using two variables (one for city, one for country).
#
# Write your code below this line:
# -----------------------------------
country="Romania"
print(country)

number1 = 100
number2 = 2000
print(number1 * number2)

city = "Bucharest"
country = "Romania"
print(f"I live in {city}, {country}")