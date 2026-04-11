# ============================================
# DAY 3 — Lists: Storing Multiple Things
# ============================================
#
# Before we start, let's warm up by fixing bugs
# from your previous mistakes. This is how you
# get better — practice what tripped you up.
#
# Run this file:
#   python3 ~/python-learning/day-03/lesson.py


# ============================================
# WARM-UP: Fix These Bugs! (from Day 1 & 2)
# ============================================
#
# Bug 1: This prints {'Romania'} instead of Romania.
#         Fix it so it prints just: Romania
#
# country = "Romania"
# print(country)
#
# Bug 2: This gives a SyntaxError. What's missing?
#
# name = "Alex"
# if name == "Alex":
#     print("Hello boss")
#
# Bug 3: This always prints "Good evening" even when hour is 14.
#         Fix the condition so 12-17 prints "Good afternoon".
#
# hour = 14
# if hour < 12:
#     print("Good morning")
# elif hour <= 17:
#     print("Good evening")
# else:
#      print("Good afternoon")
#
# Uncomment each bug, fix it, and run the file to test.
# Then comment them back out before moving on.


# ============================================
# PART 1: Creating Lists
# ============================================
#
# A list is a collection of items in a specific order.
# Think of it like a shopping list — multiple items, numbered.
# You create a list with square brackets [].

fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = ["Alex", 29, True, 3.14]  # lists can hold different types

print(fruits)
print(numbers)
print(mixed)
print()


# ============================================
# PART 2: Accessing Items (Indexing)
# ============================================
#
# Each item has a position number called an INDEX.
# IMPORTANT: Python starts counting at 0, not 1.
#
#   Index:    0        1        2
#           ["apple", "banana", "cherry"]

fruits = ["apple", "banana", "cherry"]

print(fruits[0])    # apple  (first item)
print(fruits[1])    # banana (second item)
print(fruits[2])    # cherry (third item)
print(fruits[-1])   # cherry (last item — negative counts from the end)
print(fruits[-2])   # banana (second to last)
print()


# ============================================
# PART 3: Changing Items
# ============================================
#
# Lists are MUTABLE — you can change them after creation.

colors = ["red", "green", "blue"]
print(f"Before: {colors}")

colors[1] = "yellow"  # replace "green" with "yellow"
print(f"After:  {colors}")
print()


# ============================================
# PART 4: Adding and Removing Items
# ============================================

ingredients = ["Aqua", "Glycerin"]
print(f"Start: {ingredients}")

# Add to the end
ingredients.append("Parfum")
print(f"After append: {ingredients}")

# Add at a specific position
ingredients.insert(1, "Zinc Oxide")  # insert at index 1
print(f"After insert: {ingredients}")

# Remove by value
ingredients.remove("Glycerin")
print(f"After remove: {ingredients}")

# Remove the last item
last = ingredients.pop()
print(f"Popped: {last}")
print(f"After pop: {ingredients}")
print()


# ============================================
# PART 5: Looping Through a List
# ============================================
#
# "for" lets you go through each item one by one.
# This is something you'll use EVERY DAY in Python.

products = ["Sunscreen SPF 50", "Nipple Cream", "Anti-Stretch Oil", "Thermal Spray"]

print("Product list:")
for product in products:
    print(f"  - {product}")
print()

# With index numbers (enumerate gives you position + item):
print("Product list with numbers:")
for i, product in enumerate(products, 1):  # 1 means start counting from 1
    print(f"  {i}. {product}")
print()


# ============================================
# PART 6: Useful List Operations
# ============================================

numbers = [5, 2, 8, 1, 9, 3]

print(f"List: {numbers}")
print(f"Length: {len(numbers)}")      # how many items
print(f"Smallest: {min(numbers)}")    # smallest value
print(f"Largest: {max(numbers)}")     # largest value
print(f"Sum: {sum(numbers)}")         # add them all up
print(f"Sorted: {sorted(numbers)}")   # returns a sorted copy
print()

# Check if something is in the list
print(f"Is 8 in the list? {8 in numbers}")      # True
print(f"Is 7 in the list? {7 in numbers}")      # False
print()


# ============================================
# PART 7: Slicing — Getting Parts of a List
# ============================================
#
# You can grab a portion of a list using [start:end]
# The start is included, the end is NOT included.

letters = ["a", "b", "c", "d", "e", "f"]

print(letters[1:4])    # ['b', 'c', 'd']  (index 1, 2, 3 — not 4)
print(letters[:3])     # ['a', 'b', 'c']  (from beginning to index 3)
print(letters[3:])     # ['d', 'e', 'f']  (from index 3 to end)
print(letters[-3:])    # ['d', 'e', 'f']  (last 3 items)
print()


# ============================================
# EXERCISES
# ============================================
#
# Exercise 1: Create a list of 5 EU countries.
#             Print the third country.
#             Then change the first country to "Romania" and print the whole list.
#
# Exercise 2: Create an empty list called "cart".
#             Append 3 products to it (any names you want).
#             Remove the second one.
#             Print the final cart and how many items are in it.
#
# Exercise 3: Given this list:
#             inci = ["Aqua", "Zinc Oxide", "Titanium Dioxide", "Parfum", "Dimethicone"]
#             Use a for loop to print each ingredient.
#             If the ingredient is "Parfum", print "⚠ Allergen disclosure needed!" next to it.
#             (Hint: use an if inside the for loop)
#
# Write your code below this line:
# -----------------------------------
country = ["Spain", "Portugal", "Bucharest", "Bulgaria", "France"]  #still needs practice
print(country[2])     #still needs practice
country[0] = "Romania" #still needs practice

cart = []
cart.append("orange")  #needs practice
cart.append("cola")    #needs practice
cart.append("sprite")  #needs practice
cart.remove("cola")
print(f"Cart:  {cart},  Items: {len(cart)}")


inci = ["Aqua", "Zinc Oxide", "Titanium Dioxide", "Parfum", "Dimethicone"]
print("Product list:")   # needs practice
for product in inci:     #needs practice
        print(f"  - {product}")    #needs practice
for product in inci:
     if product == "Parfum":
          print(f" - {product} Allergen disclosure needed!")
     else:
          print(f" - {product}")


