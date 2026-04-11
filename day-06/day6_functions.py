# ============================================
# DAY 6 — FUNCTIONS
# ============================================
# Think of a function like a MACHINE in a factory:
#
#   You put something IN  →  the machine does work  →  something comes OUT
#
#   def machine(input):
#       do something
#       return output
#
# You already used functions! print() is a function. input() is a function.
# Today you learn to BUILD YOUR OWN.
#
# ============================================


# --- STEP 1: The simplest function possible ---

def say_hello():
    print("Hello!")

say_hello()        # This CALLS the function — it runs the code inside
say_hello()        # You can call it as many times as you want

# That's it. "def" means "define a new function". The code inside runs when you call it.


# --- STEP 2: A function that takes INPUT ---

def say_hello_to(name):
    print(f"Hello, {name}!")

say_hello_to("Alex")       # name = "Alex"
say_hello_to("Jarvis")     # name = "Jarvis"

# "name" is called a PARAMETER — it's a placeholder.
# When you call the function, you fill in the placeholder with a real value.


# --- STEP 3: return vs print (THE MOST IMPORTANT PART) ---

# WITH PRINT — the function SHOWS the answer, but doesn't give it back
def add_and_print(a, b):
    print(a + b)

add_and_print(3, 5)        # Shows: 8
# But you can't DO anything with that 8. It's just on screen.

# WITH RETURN — the function GIVES BACK the answer, so you can use it
def add_and_return(a, b):
    return a + b

result = add_and_return(3, 5)    # result now holds 8
print(result)                     # 8
print(result * 2)                 # 16 — you can keep using it!

# Simple rule:
#   print  = just shows it (like shouting the answer)
#   return = gives it back to you (like handing you a note)


# --- STEP 4: Function with if/else inside ---

def check_age(age):
    if age >= 18:
        return "You can enter"
    else:
        return "Too young"

print(check_age(25))     # "You can enter"
print(check_age(14))     # "Too young"

# Same if/else you already know — just wrapped inside a function!


# ============================================
# YOUR EXERCISES — Write your code below
# ============================================

# EXERCISE 1 — Basic function
# Write a function called "double" that takes a number and RETURNS it multiplied by 2.
# Then call it and print the result.
#
# Example of what should happen:
#   print(double(5))   should show: 10
#   print(double(20))  should show: 40

# your code here:      #definetly needs more practice
def double(number):
    return number * 2
    result = number * 2
    print(double(5))
    print(double(20))
    
# EXERCISE 2 — Function with if/else
# Write a function called "access_check" that takes TWO inputs: username and role.
# If the role is "admin", return "Access granted".
# Otherwise, return "Access denied".
# Call it twice and print both results.
#
# Example:
#   print(access_check("Alex", "admin"))    should show: Access granted
#   print(access_check("Bob", "viewer"))    should show: Access denied

# your code here:   #got it but still needs more practice (tried a few times until i got this finished)
def access_check(username, role):
    if role == "admin":
        return (f"Access granted")
    else:
        return (f"Access denied")
    print(access_check("Bibi", "admin"))
    print(access_check("Papi", "customer"))

# EXERCISE 3 — Function + dictionary + loop
# Write a function called "show_expensive" that takes a dictionary of items (name: price)
# and PRINTS only the items that cost more than 100.
#
# Call it with this data:
# gear = {"GPU": 800, "Mouse": 25, "Monitor": 350, "Cable": 10}
#
# Expected output:
#   GPU: $800
#   Monitor: $350

# your code here:   # this was giving me a headache, practice untill perfect....but had some problems
def show_expensive(items):
    for name, price in items.items():
        if price > 100:
            print(f"{name}: ${price}")
gear = {"GPU": 800, "Mouse": 25, "Monitor": 350, "Cable": 10}
show_expensive(gear)