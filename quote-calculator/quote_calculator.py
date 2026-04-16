# Freelance Quote Calculator
# Build a tool that generates a price quote for a client.


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



    
    
    
    

    







    



