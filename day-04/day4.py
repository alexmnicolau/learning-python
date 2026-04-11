# ============================================
# DAY 4 — Lists + Loops (Take 2 — Proper Teaching First)
# ============================================
# Run this file after each section: python3 day4.py


# ============================================
# LESSON: "if" inside a "for" loop
# ============================================
# This is the #1 thing you need to learn today.
# It's simpler than you think. Watch:

# Example 1 — Check each number, is it big or small?
numbers = [5, 20, 3, 50, 8]

for n in numbers:
    if n >= 20:
        print(f"{n} is big")
    else:
        print(f"{n} is small")     #i understood this one, more about intendation(spaces are important)

print("---")  # just a separator

# Example 2 — Find a specific item in a list
tools = ["python", "docker", "git", "python", "node"]

for tool in tools:
    if tool == "python":
        print(f"Found it: {tool}")   # got this one too, needs practice

print("---")

# Example 3 — Collect items into a new list
big_numbers = []  # start with empty list

for n in numbers:
    if n >= 20:
        big_numbers.append(n)  # add to the new list

print(f"Big numbers: {big_numbers}")    # a bit more complicated for me, but i will exercise it more.

print("---")


# ============================================
# EXERCISE 1 — Find the hacker (easy)
# ============================================
# Loop through the users list.
# If the user is "darknet", print "INTRUDER: darknet"
# For everyone else, print "OK: [name]"

users = ["alex", "darknet", "bot7", "admin"]

# your code below:

for user in users:
         if user == "darknet":
              print(f"Intruder: {user}")
        else:
              print(f"Ok: {user}")

# ============================================
# EXERCISE 2 — Error filter (medium)
# ============================================
# Loop through the codes list.
# If a code is 400 or above, add it to the errors list.
# After the loop, print the errors list.
# (Look at Example 3 above — same pattern!)

codes = [200, 404, 201, 500, 301]
errors = []  # start empty, you fill it in the loop

# your code below:
for c in codes:
     if c >= 400:
          errors.append(c)
          print(errors)


# ============================================
# EXERCISE 3 — Fix Bug 2 from earlier
# ============================================
# Fix the condition so it ONLY prints "Reachable" when
# status is "online" OR status is "standby"
# (Remember: you need status == on BOTH sides of "or")

status = "offline"
if status == "online" or status == "standby":
    print("Reachable")
else:
    print("Not reachable")

# ^ fix the if line above. Right now it prints "Reachable" even though status is "offline"!

if status == "online" or == "standby":
     print("Reachable")
else:
     print("Not reachable")

# ============================================
# DONE? Paste your code back to me!
# ============================================
