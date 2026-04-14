# Freelance Quote Calculator
# Build a tool that generates a price quote for a client.

# INSTRUCTIONS:
# 1. Define a main() function — all your code goes inside it
# 2. Ask for the client's name using input()
# 3. Clean the name — remove extra spaces (strip) and capitalize it (title)
# 4. Ask for the number of hours (convert to float)
# 5. Ask for the hourly rate in $ (convert to float)
# 6. Ask for the tax percentage (convert to float)
# 7. Calculate:
#    - subtotal = hours * rate
#    - tax_amount = subtotal * tax / 100
#    - total = subtotal + tax_amount
# 8. Round the total to 2 decimal places using round()
# 9. Print a formatted quote like this:
#
#    --- QUOTE ---
#    Client: NoOne
#    Hours: 10.0
#    Rate: $85.00/hr
#    Subtotal: $850.00
#    Tax (19%): $161.50
#    Total: $1011.50
#    --- END ---
#
# 10. Call main() at the bottom of the file

# YOUR CODE BELOW:

def main():
    print("--- QUOTE ---")
    name = input("What's your name? ").strip().title()
    print("--- QUOTE ---")
    print(f"Client: {name}")
    hours = float(input("How many hours? "))
    print(f"Hours: {hours}")
    rate = float(input("What's your hourly rate in $? "))
    print(f"Rate: ${rate:.2f}/hr")
    subtotal = hours * rate
    print(f"Subtotal: ${subtotal:.2f}")
    tax = float(input("What's your TAX percentage? "))
    tax_amount = subtotal * tax / 100
    total = round(subtotal + tax_amount, 2 )
    print(f"Tax ({tax}%): ${tax_amount}")
    print(f"Total: ${total}")
    print(" --- END ---")
main()



    
    
    
    

    







    



