# Day 8 — .items() Drilling
# Topic: looping through dictionaries with .items()
# Pattern: for key, value in dict.items()
# Rule: write your answer BELOW each exercise, then we review together

# =============================================================
# EXERCISE 1
# Loop through the models dictionary and print each line like:
# Claude is made by Anthropic
# GPT-4 is made by OpenAI
# =============================================================

models = {
    "GPT-4": "OpenAI",
    "Claude": "Anthropic",
    "Gemini": "Google",
    "Llama": "Meta"
} 
for model, company in models.items():
    print(f"{model} is made by {company}")
    

# =============================================================
# EXERCISE 2
# You have a dictionary of VPS servers and their status.
# Loop through it and print ONLY the servers that are "offline":
# db-server is offline
# backup-server is offline
# (skip the ones that are "online")
# =============================================================

servers = {
    "web-server": "online",
    "db-server": "offline",
    "api-server": "online",
    "backup-server": "offline"
}
for server, status in servers.items():
    if status == "offline":
        print(f"{server} is {status}")


# =============================================================
# EXERCISE 3
# You have a dictionary of API endpoints and their response times (in ms).
# Loop through it and print ONLY endpoints slower than 200ms:
# /api/users is slow: 350ms
# /api/orders is slow: 520ms
# =============================================================

endpoints = {
    "/api/health": 45,
    "/api/users": 350,
    "/api/products": 120,
    "/api/orders": 520
}

for api, points in endpoints.items():
    if points > 200:
        print(f"{api} is slow:{points}ms")




# =============================================================
# EXERCISE 4
# You have a dictionary of crypto prices (in USD).
# Loop through it and build a NEW list called "expensive"
# that contains only the coin names priced above $1000.
# Then print the list.
# Expected output: ['BTC', 'ETH']
# =============================================================

crypto = {
    "BTC": 62000,
    "ETH": 3200,
    "DOGE": 0.15,
    "SOL": 145
}

expensive = []

for coin, price in crypto.items():
    if price > 1000:
        expensive.append(coin)
print(expensive)


# =============================================================
# EXERCISE 5
# You have a dictionary of bots and how many messages they sent today.
# Calculate the TOTAL messages sent across all bots and print it.
# Expected output: Total messages: 1340
# =============================================================

bots = {
    "reddit-bot": 312,
    "telegram-bot": 528,
    "discord-bot": 215,
    "slack-bot": 285
}

total = 0

for bot, messages in bots.items():
    total += messages
print(total)

