# Day 10 — Combining 2 Concepts
# Topic: functions that combine loops + conditions + lists + sums
# Rule: write your answer BELOW each exercise, then we review together

# =============================================================
# EXERCISE 1
# Write a function called "get_online_names" that takes a dictionary
# of servers and their status, and returns a LIST of names that are "online".
# Then call it and print the result.
# Expected output: ['web-01', 'api-01', 'cdn-01']
# =============================================================

servers = {
    "web-01": "online",
    "db-01": "offline",
    "api-01": "online",
    "backup-01": "offline",
    "cdn-01": "online"
}

def get_online_names(servers):
    online = []
    for server, status in servers.items():
        if status == "online":
            online.append(server)
    return online
     
results = get_online_names(servers)
print(results)
    


# =============================================================
# EXERCISE 2
# Write a function called "count_high_scores" that takes a dictionary
# of players and their scores, and returns HOW MANY players
# scored above 500.
# Then call it and print the result.
# Expected output: 3
# =============================================================

scores = {
    "player1": 320,
    "player2": 780,
    "player3": 95,
    "player4": 610,
    "player5": 540
}

def count_high_scores(scores):
    total = 0
    for player, score in scores.items():
        if score > 500:
            total += 1
    return total

results = count_high_scores(scores)
print(results)


# =============================================================
# EXERCISE 3
# Write a function called "get_expensive_models" that takes a dictionary
# of AI models and their cost per 1M tokens (in USD), and returns a LIST
# of model names that cost MORE than 10 USD.
# Then call it and print the result.
# Expected output: ['gpt-4', 'claude-opus', 'gemini-ultra']
# =============================================================

models = {
    "gpt-4": 30.0,
    "gpt-3.5": 2.0,
    "claude-opus": 15.0,
    "claude-haiku": 0.25,
    "gemini-ultra": 12.0,
    "gemini-flash": 0.35
}

def get_expensive_models(models):
    expensive = []
    for model, cost in models.items():
        if cost > 10:
            expensive.append(model)
    return expensive
results = get_expensive_models(models)
print(results)

# =============================================================
# EXERCISE 4
# Write a function called "total_revenue" that takes a dictionary
# of products and their sales revenue (in USD), and returns the
# TOTAL revenue across ALL products.
# Then call it and print the result.
# Expected output: 15850
# =============================================================

products = {
    "gpu-3090": 4200,
    "cpu-i9": 890,
    "ssd-2tb": 310,
    "ram-64gb": 450,
    "monitor-4k": 9000,
    "keyboard-pro": 1000
}

def total_revenue(products):
    total = 0
    for product, revenue in products.items():
        total += revenue
    return total 
results = total_revenue(products)
print(f"${results}")
    


# =============================================================
# EXERCISE 5
# Write a function called "get_failing_bots" that takes a dictionary
# of bots and their success rates (%), and returns a LIST of bot names
# with a success rate BELOW 80%.
# Then call it and print the result.
# Expected output: ['scraper-bot', 'notify-bot']
# =============================================================

bots = {
    "reddit-bot": 94.5,
    "scraper-bot": 61.2,
    "telegram-bot": 88.0,
    "notify-bot": 73.4,
    "discord-bot": 91.7
}

def get_failing_bots(bots):
    failing_bots = []
    for bot, rate in bots.items():
        if rate < 80:
            failing_bots.append(bot)
    return failing_bots
results = get_failing_bots(bots)
print(results)