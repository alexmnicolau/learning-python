# ============================================
# DAY 4 — EXTRA PRACTICE
# Topic: "if" inside a "for" loop
# ============================================

# You're scanning a network. Check each port:
# - If the port is 22, print "Port 22: SSH — OPEN"
# - If the port is 443, print "Port 443: HTTPS — OPEN"
# - For everything else, print "Port [number]: CLOSED"

ports = [80, 22, 3000, 443, 8080]

for p in ports:
    if p == 22:
        print(f"Port {p}: SSH - OPEN")
    elif p == 443:
        print(f"Port {p}: OPEN")
    else:
        print(f"Port {p}: CLOSED")


