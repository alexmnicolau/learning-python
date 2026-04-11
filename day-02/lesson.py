# ============================================
# DAY 2 — Making Decisions: if, elif, else
# ============================================
#
# Yesterday you learned how to store data and print it.
# Today you teach Python how to THINK — make decisions based on conditions.
#
# Run this file:
#   python3 ~/python-learning/day-02/lesson.py


# === PART 1: Comparisons — Asking Questions ===
#
# Before Python can make decisions, it needs to compare things.
# A comparison always gives you True or False.

age = 29

print(age == 29)    # True   (== means "is equal to?")
print(age == 30)    # False
print(age != 30)    # True   (!= means "is NOT equal to?")
print(age > 18)     # True   (> means "greater than?")
print(age < 18)     # False  (< means "less than?")
print(age >= 29)    # True   (>= means "greater than or equal to?")
print(age <= 28)    # False  (<= means "less than or equal to?")

# IMPORTANT: == is for comparing. = is for assigning.
#   age = 29   → puts 29 into age
#   age == 29  → asks "is age equal to 29?"


# === PART 2: if — The Basic Decision ===
#
# "if" checks a condition. If it's True, the indented code runs.
# If it's False, Python skips it.

temperature = 35

if temperature > 30:
    print("It's hot outside!")

# The INDENTATION (4 spaces) is critical in Python.
# Everything indented under the "if" belongs to that decision.
# When Python sees a non-indented line, the "if" block is over.

print("This line always runs — it's not indented under the if.")


# === PART 3: if / else — Two Choices ===
#
# "else" catches everything that didn't match the "if".

age = 29

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Only ONE of these will ever run. Never both.


# === PART 4: if / elif / else — Multiple Choices ===
#
# "elif" means "else if" — it adds more options.
# Python checks from top to bottom and runs the FIRST one that's True.

score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Try changing score to 95, 82, 55, etc. and run again.


# === PART 5: Combining Conditions — and, or, not ===
#
# Sometimes you need to check more than one thing at once.

age = 29
has_id = True

# "and" — BOTH must be True
if age >= 18 and has_id:
    print("You can enter the club.")

# "or" — at least ONE must be True
is_student = False
is_employee = True

if is_student or is_employee:
    print("You get a discount.")

# "not" — flips True to False, False to True
is_banned = False

if not is_banned:
    print("Welcome!")


# === PART 6: Checking Text ===
#
# Comparisons work on strings too, not just numbers.

name = "Alex"

if name == "Alex":
    print("Hello, boss!")
else:
    print(f"Hello, {name}!")

# You can check if text contains something with "in":
email = "alex@gmail.com"

if "@" in email:
    print("This looks like a valid email.")
else:
    print("This doesn't look like an email.")

# You can check if a string is empty:
user_input = ""

if user_input:
    print(f"You typed: {user_input}")
else:
    print("You didn't type anything.")

# In Python, an empty string "" is considered False.
# Any string with text in it is considered True.
# This is a very common pattern you'll use a lot.


# ============================================
# EXERCISES — Try these yourself!
# ============================================
#
# Exercise 1: Create a variable "hour" with any number from 0 to 23.
#             If hour is less than 12, print "Good morning"
#             If hour is between 12 and 17, print "Good afternoon"
#             Otherwise, print "Good evening"
#
# Exercise 2: Create two variables: "username" and "password".
#             If username is "alex" AND password is "python123",
#             print "Login successful"
#             Otherwise print "Wrong credentials"
#
# Exercise 3: Create a variable "product_name" with any text.
#             Check if it contains the word "SPF".
#             If yes, print "This is a sunscreen product"
#             If no, print "This is not a sunscreen product"
#
# Write your code below this line:
# -----------------------------------

hour = 20
if hour < 12:
        print("Good morning")
elif hour <= 17:
        print("Good afternoon")
else:
        print("Good evening")
    
username = "alex"
password = "python123"

if username == "alex" and password == "python123":
    print("Login successful")
else:
    print("Wrong Credentials")

product_name = "sheikalabel"
if "SPF" in product_name:
        print("This is a sunscreen product")
else:
        print("This is not a sunscreen product")