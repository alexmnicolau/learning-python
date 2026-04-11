# ============================================
# DAY 6 — REINFORCEMENT EXERCISES
# Only uses: variables, f-strings, if/elif/else,
# lists, loops, dictionaries, functions
# ============================================


# EXERCISE 1 — Function + if/elif/else
# Write a function called "threat_level" that takes a number (cpu_usage).
#   - If cpu_usage is above 90, return "CRITICAL"
#   - If cpu_usage is above 60, return "WARNING"
#   - Otherwise, return "NORMAL"
# Then call it 3 times with values 95, 75, and 30 — print each result.

# your code here:   #got it, needs more practice.
def threat_level(cpu_usage):
    if cpu_usage > 90:
        return "CRITICAL"
    if cpu_usage > 60:
        return "WARNING"
    else:
        return "NORMAL"
print(threat_level(95))
print(threat_level(75))
print(threat_level(30))


# EXERCISE 2 — Function + list + loop
# Write a function called "count_high_scores" that takes a list of numbers.
# Loop through the list and COUNT how many numbers are above 100.
# RETURN that count.
#
# Call it with this list and print the result:
# scores = [45, 120, 89, 200, 50, 150]
# Expected output: 3

# your code here:
def count_high_scores(scores):
    count = 0
    for score in scores:
        if score > 100:
            count = count + 1
    return count
scores = [45, 120, 89, 200, 50, 150]
print(count_high_scores(scores))

# EXERCISE 3 — Function + dictionary + loop
# Write a function called "show_status" that takes a dictionary of servers (name: cpu).
# Loop through it. If cpu is above 80, print "ALERT: {name}".
# Otherwise, print "OK: {name}".
#
# Call it with this data:
# servers = {"VPS-1": 45, "VPS-2": 92, "VPS-3": 10}
#
# Expected output:
#   OK: VPS-1
#   ALERT: VPS-2
#   OK: VPS-3

# your code here:
def show_status(servers):
    for name, cpu in servers.items():
        if cpu > 80:
            print(f"Alert: {name}")
        else:
            print(f"OK: {name}")

servers = {"VPS-1": 45, "VPS-2": 92, "VPS-3": 10}
show_status(servers)


# EXERCISE 4 — Two functions working together
# Write TWO functions:
#   1. "calculate_total" — takes a list of prices, RETURNS the sum
#   2. "apply_discount" — takes a total and a discount percentage, RETURNS the discounted price
#
# Then use them together:
#   prices = [50, 30, 20]
#   total = calculate_total(prices)
#   final = apply_discount(total, 10)
#   print(f"Total: ${total}, After 10% discount: ${final}")
#
# Expected output: Total: $100, After 10% discount: $90.0
#
# Hint for discount: total - (total * percentage / 100)

# your code here:
def calculate_total(prices):
    total = 0
    for price in prices:
        total = total + price
    return total
def apply_discount(total, percentage):
    return total - (total * percentage / 100)
prices = [50, 30, 20]
total = calculate_total(prices)
final = apply_discount(total, 10)
print(f"Total: ${total}, After 10% discount: ${final}")
    

# EXERCISE 5 — Full combo
# Write a function called "grade_students" that takes a dictionary (name: score).
# Loop through it. For each student:
#   - If score is above 90, print "{name}: A"
#   - If score is above 70, print "{name}: B"
#   - Otherwise, print "{name}: C"
#
# Call it with:
# students = {"Alex": 95, "Bob": 72, "Maria": 55, "Jarvis": 88}
#
# Expected output:
#   Alex: A
#   Bob: B
#   Maria: C
#   Jarvis: B

# your code here:
def grade_students(score):
    for name, grade in score.items():
        if grade > 90:
            print(f"{name}: A")
        elif grade > 70:
            print(f"{name}: B")
        else:
            print(f"{name}: C")
students = {"Alex": 95, "Bob": 72, "Maria": 55, "Jarvis": 88}
grade_students(students)
         