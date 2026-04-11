# Day 9 — Functions + Loop + Return
# Topic: writing functions that loop through data and return a result
# Key rule: return goes OUTSIDE the loop, at the same indentation as "for"
# Rule: write your answer BELOW each exercise, then we review together

# =============================================================
# EXERCISE 1
# Write a function called "count_online" that takes a dictionary
# of servers and returns HOW MANY are "online".
# Then call it and print the result.
# Expected output: 3
# =============================================================

servers = {
    "web": "online",
    "db": "offline",
    "api": "online",
    "cache": "online"
}


def count_online(servers):
    total = 0 
    for server, status in servers.items():
        if status == "online":
            total += 1 
    return total 
    
result = count_online(servers)
print(result)

# =============================================================
# EXERCISE 2
# Write a function called "total_price" that takes a dictionary
# of items and their prices, and returns the SUM of all prices.
# Then call it and print the result.
# Expected output: 79.97
# =============================================================

cart = {
    "keyboard": 29.99,
    "mouse": 14.99,
    "headset": 34.99
}

def total_price(cart):
    total = 0 
    for item, price in cart.items():
        total += price
    return total

result = total_price(cart)
print(result)


# =============================================================
# EXERCISE 3
# Write a function called "count_accurate" that takes a dictionary
# of AI models and their accuracy scores (%), and returns HOW MANY
# models have accuracy ABOVE 90.
# Then call it and print the result.
# Expected output: 3
# =============================================================

models = {
    "gpt-4": 94.2,
    "claude": 96.8,
    "gemini": 88.1,
    "llama": 91.5,
    "mistral": 79.3
}

def count_accurate(models):
    total = 0 
    for model, accuracy in models.items():
        if accuracy > 90:
            total += 1
    return total

result = count_accurate(models)
print(result)



# =============================================================
# EXERCISE 4
# Write a function called "get_slow_endpoints" that takes a dictionary
# of API endpoints and their response times (ms), and returns a LIST
# of endpoint names that are slower than 300ms.
# Then call it and print the result.
# Expected output: ['/api/users', '/api/orders', '/api/reports']
# =============================================================

endpoints = {
    "/api/health": 45,
    "/api/users": 870,
    "/api/products": 210,
    "/api/orders": 640,
    "/api/reports": 1200
}

def get_slow_endpoints(endpoints):
    slow = []
    for endpoint, ms in endpoints.items():
        if ms > 300:
            slow.append(endpoint)
    return slow 

result = get_slow_endpoints(endpoints)
print(result)

# =============================================================
# EXERCISE 5
# Write a function called "total_bandwidth" that takes a dictionary
# of servers and their bandwidth usage (in GB), and returns the
# TOTAL bandwidth used across ALL servers.
# Then call it and print the result.
# Expected output: Total bandwidth: 3.3TB
# =============================================================

usage = {
    "web-01": 820,
    "web-02": 640,
    "db-01": 1100,
    "cdn-01": 740
}

def total_bandwidth(usage):
    total = 0
    for server, gb in usage.items():
        total += gb
    return total 

result = total_bandwidth(usage)
print(f"Total bandwidth: {result / 1000:.1f}TB")
