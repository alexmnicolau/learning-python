# ============================================
# DAY 5 — Dictionaries
# ============================================
# A dictionary stores data as KEY: VALUE pairs.
# Think of it like a real dictionary: you look up a WORD (key) to get its MEANING (value).
# Run this file after each section: python3 day5.py


# ============================================
# LESSON: What is a dictionary?
# ============================================

# A list stores items by position (index 0, 1, 2...)
# A dictionary stores items by NAME (a key you choose)

# Example 1 — A server's info
server = {
    "name": "alpha",
    "ip": "192.168.1.10",
    "status": "online"
}

# To get a value, use the KEY (not an index number):
print(server["name"])       # prints: alpha
print(server["ip"])         # prints: 192.168.1.10
print(server["status"])     # prints: online

print("---")

# Example 2 — Adding and changing values
server["location"] = "Berlin"     # adds a NEW key
server["status"] = "offline"      # CHANGES an existing key

print(server["location"])   # prints: Berlin
print(server["status"])     # prints: offline (was "online", now changed)

print("---")

# Example 3 — Looping through a dictionary
# You can loop through all keys and values:
for key, value in server.items():
    print(f"{key} = {value}")     #not sure i got this right, needs better explanation.

print("---")


# ============================================
# EXERCISE 1 — Build a player profile
# ============================================
# Create a dictionary called "player" with these keys:
#   "username" → "ShadowX"
#   "level" → 42
#   "rank" → "Diamond"
#
# Then print each value using the key.
# Expected output:
#   ShadowX
#   42
#   Diamond

# your code below:  #i helped myself from the first phase of this tutorial, needs more practice but i understood the logic.
player = {
    "username": "ShadowX",
    "level": 42,  # numbers don't need "quotes"
    "rank": "Diamond"
}
print(player["username"])
print(player["level"])
print(player["rank"])


# ============================================
# EXERCISE 2 — Update the profile
# ============================================
# Using the "player" dictionary from Exercise 1:
# 1. Change the level to 43
# 2. Add a new key "clan" with value "NightOwls"
# 3. Print the full dictionary

# your code below:    # i helped myself here as well but i am getting it.
player["level"] = 43
player["clan"] = "NightOwls"
print(player)




# ============================================
# EXERCISE 3 — Loop through it
# ============================================
# Loop through the "player" dictionary and print each key and value like this:
#   username: ShadowX
#   level: 43
#   rank: Diamond
#   clan: NightOwls
#
# (Hint: look at Example 3)


# your code below:

for username, value in player.items():
    print(f" {username} {value}")
    



