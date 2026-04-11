# ============================================
# DAY 7 — FULL EXERCISE DAY
# Everything from Day 1-6, no new concepts
# ============================================


# ═══ WARM-UP (variables, f-strings, print) ═══

# EXERCISE 1 — Variables & f-strings
# Create 3 variables: server_name, cpu_usage, is_online
# server_name = "VPS-Alpha"
# cpu_usage = 73.5
# is_online = True
# Print: "VPS-Alpha | CPU: 73.5% | Online: True"

# your code here:
server_name = "VPS-Alpha"
cpu_usage = 73.5 
is_online = True
print(server_name)
print(f"CPU: {cpu_usage}%")
print(f"Online: {is_online}")



# ═══ IF / ELIF / ELSE ═══

# EXERCISE 2 — Conditions
# Write code that checks a variable called "ping" (set it to 250).
# If ping is below 50, print "Excellent"
# If ping is below 100, print "Good"
# If ping is below 200, print "Slow"
# Otherwise, print "Critical"
#
# Expected output: Critical

# your code here:
ping = 250
if ping < 50:
       print("Excellent")
elif ping < 100:
       print("Good")
elif ping < 200:
       print("Slow")
else:
       print("Critical")

# EXERCISE 3 — Conditions with AND/OR
# Create two variables: has_api_key = True, credits = 0
# If has_api_key is True AND credits is above 0, print "Ready to go"
# Otherwise, print "Cannot start — check your credits"
#
# Expected output: Cannot start — check your credits

# your code here:
has_api_key = "True"
credits = 0
if has_api_key == "True" and credits > 0:
    print("Ready to go")
else:
      print("Cannot start - check your credits")

# ═══ LISTS & LOOPS ═══

# EXERCISE 4 — Loop through a list
# Create a list called "models" with these values: "Haiku", "Sonnet", "Opus"
# Loop through the list and print each model on its own line.
#
# Expected output:
#   Haiku
#   Sonnet
#   Opus

# your code here:
models = ["Haiku", "Sonnet", "Opus"]
for model in models:
      print(model)


   

# EXERCISE 5 — If inside a for loop
# Create a list of numbers: scores = [88, 42, 95, 67, 100, 55]
# Loop through them. Print only the scores that are above 80.
#
# Expected output:
#   88
#   95
#   100

# your code here:
scores = [88, 42, 95, 67, 100, 55]
for score in scores:
    if score > 80:
        print(score)




# EXERCISE 6 — List indexing (0-based)
# Create a list: tools = ["Claude", "GPT", "Gemini", "Llama", "Mistral"]
# Print the FIRST item (index 0)
# Print the THIRD item (index 2)
# Print the LAST item (index -1)
#
# Expected output:
#   Claude
#   Gemini
#   Mistral

# your code here:
tools = ["Claude", "GPT", "Gemini", "Llama", "Mistral"]
print(tools[0])
print(tools[2])
print(tools[4])
      
      
    
    
    

# ═══ DICTIONARIES ═══

# EXERCISE 7 — Create and access a dictionary
# Create a dictionary called "server" with:
#   "name": "jarvis"
#   "ip": "49.13.230.244"
#   "status": "running"
# Print the server name and its status using f-string.
#
# Expected output: jarvis is running

# your code here:   
server = { 
    "name": "jarvis",
    "ip": "49.13.230.244",
    "status": "running"
}
print(f"{server['name']} is {server['status']}")


# EXERCISE 8 — Loop a dictionary with .items()
# Create a dictionary:
# agent = {"name": "Opus", "tokens": 4096, "vision": True}
# Loop through it and print each key-value pair like:
#   name: Opus
#   tokens: 4096
#   vision: True

# your code here:
agent = {"name": "Opus", "tokens": 4096, "vision": True}
for name, value in agent.items():
      print(f"{name}: {value}")
    

# ═══ FUNCTIONS ═══

# EXERCISE 9 — Simple function with return
# Write a function called "triple" that takes a number and returns it * 3.
# Call it with 7 and print the result.
#
# Expected output: 21

# your code here:
def triple(number):
      return number *3

print(triple(7))


# EXERCISE 10 — Function with if/elif/else
# Write a function called "classify_temp" that takes a number (temperature).
#   If above 35: return "Hot"
#   If above 20: return "Warm"
#   If above 5: return "Cool"
#   Otherwise: return "Cold"
# Call it 3 times with 40, 22, and -3. Print each result.
#
# Expected output:
#   Hot
#   Warm
#   Cold

# your code here:
def classify_temp(temperature):
     if temperature > 35:
           return "Hot"
     elif temperature > 20:
           return "Warm"
     elif temperature > 5:
           return "Cool"
     else:
           return "Cold"
     
print(classify_temp(40))
print(classify_temp(22))
print(classify_temp(-3))



      

# ═══ COMBINING EVERYTHING ═══

# EXERCISE 11 — Function + list + loop + counter
# Write a function called "count_online" that takes a list of statuses.
# Count how many are "online" and return the count.
#
# Call it with: ["online", "offline", "online", "online", "offline"]
# Print the result.
#
# Expected output: 3

# your code here:
def count_online(statuses):
    count = 0
    for status in statuses:
           if status == "online":
                  count = count + 1
    return count
print(count_online(["online", "offline", "online", "online", "offline"]))   
            



# EXERCISE 12 — Function + dictionary + loop
# Write a function called "show_alerts" that takes a dictionary of servers (name: cpu).
# Loop through it. If cpu is above 80, print "ALERT: {name} at {cpu}%"
# Otherwise, print "OK: {name}"
#
# Call it with: {"VPS-1": 45, "VPS-2": 92, "VPS-3": 88, "VPS-4": 30}
#
# Expected output:
#   OK: VPS-1
#   ALERT: VPS-2 at 92%
#   ALERT: VPS-3 at 88%
#   OK: VPS-4

# your code here:
def show_alerts(servers):
     for name, cpu in servers.items():
          if cpu > 80:
                print(f"ALERT {name} at {cpu}%")
          else:
                print (f"OK: {name}")

show_alerts({"VPS-1": 45, "VPS-2": 92, "VPS-3": 88, "VPS-4": 30})



# EXERCISE 13 — Function + loop that adds (the pattern from Day 6)
# Write a function called "total_tokens" that takes a list of numbers.
# Start at 0, loop through the list, add each number to the total.
# Return the total.
#
# Call it with: [1024, 2048, 512, 4096]
# Print the result.
#
# Expected output: 7680

# your code here:
def total_tokens(numbers):
    total = 0
    for number in numbers:
          total = total + number
    return total
print(total_tokens([1024, 2048, 512, 4096]))


          

# EXERCISE 14 — Two functions working together
# Write TWO functions:
#   1. "sum_prices" — takes a list of prices, returns the total
#   2. "add_tax" — takes a total and a tax rate (%), returns total + tax
#
# Use them:
#   prices = [29, 49, 99]
#   total = sum_prices(prices)
#   final = add_tax(total, 19)
#   print(f"Subtotal: ${total}, With 19% tax: ${final}")
#
# Expected output: Subtotal: $177, With 19% tax: $210.63

# your code here:
def sum_prices(prices):
    total = 0
    for price in prices:
        total = total + price
    return total

def add_tax(total, tax_rate):
    return total + (total * tax_rate / 100)

prices = [29, 49, 99]
total = sum_prices(prices)
final = add_tax(total, 19)
print(f"Subtotal: ${total}, With 19% tax: ${final}")


# EXERCISE 15 — Full combo (the boss level)
# Write a function called "server_report" that takes a dictionary (name: cpu).
# Loop through it. For each server:
#   If cpu > 90: print "{name}: CRITICAL"
#   If cpu > 70: print "{name}: WARNING"
#   Otherwise: print "{name}: OK"
# After the loop, print a summary: "Total: X servers, Y alerts"
# (count how many are above 70 for alerts)
#
# Call it with: {"Alpha": 95, "Beta": 60, "Gamma": 85, "Delta": 40, "Echo": 99}
#
# Expected output:
#   Alpha: CRITICAL
#   Beta: OK
#   Gamma: WARNING
#   Delta: OK
#   Echo: CRITICAL
#   Total: 5 servers, 3 alerts

# your code here:
def server_report(servers):
    alerts = 0
    total = 0
    for name, cpu in servers.items():
        total = total + 1
        if cpu > 90:
            print(f"{name}: CRITICAL")
            alerts = alerts + 1
        elif cpu > 70:
            print(f"{name}: WARNING")
            alerts = alerts + 1
        else:
            print(f"{name}: OK")
    print(f"Total: {total} servers, {alerts} alerts")

server_report({"Alpha": 95, "Beta": 60, "Gamma": 85, "Delta": 40, "Echo": 99})