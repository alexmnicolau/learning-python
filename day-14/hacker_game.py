# Guess the pin


correct_pin = 4321
attempts = 5

print("Hello, player! think about reversing the most common password in the world [4 digits only]:")

while True:

    if attempts == 0:
        print("SYSTEM LOCKED. Intruder detected.")
        break

    try:
        guess = int(input("Enter your PIN -> "))
    except ValueError:
        print("Invalid PIN, numbers only.")
    else:
        if guess == correct_pin:
            print("ACCESS GRANTED. Welcome, root.")
            break
        else:
            attempts -= 1
            print(f"This is not valid. {attempts} attempts remaining.")
