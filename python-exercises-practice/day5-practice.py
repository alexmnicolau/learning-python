# ============================================
# DAY 5 — EXTRA PRACTICE
# Topic: Looping through a dictionary
# ============================================

# QUICK LESSON: What are .items(), key, and value?
#
# A dictionary is like a phone book:
#   "Alex" → "0721-111-111"
#   "Raluca" → "0722-222-222"
#
# .items() gives you ALL the pairs, one by one.
# YOU choose the names for each pair. We call them "key" and "value":
#
#   for key, value in phonebook.items():
#       print(f"{key} → {value}")
#
# Round 1: key = "Alex",   value = "0721-111-111"
# Round 2: key = "Raluca", value = "0722-222-222"
#
# "key" and "value" are just variable names — you could call them
# "k" and "v", or "name" and "number", anything you want.
# The FIRST one always gets the key, the SECOND one gets the value.


# ============================================
# EXERCISE — Loop through this bot's config
# ============================================
# Use a for loop with .items() to print each setting like this:
#   bot_name: Jarvis
#   version: 3.1
#   language: Python
#   active: True
#
# Remember: ONE print line inside the loop. The loop does the repeating.

bot = {
    "bot_name": "Jarvis",
    "version": 3.1,
    "language": "Python",
    "active": True
}

# your code below:
for bot_name, value in bot.items():
    print(f"{bot_name} {value}")

