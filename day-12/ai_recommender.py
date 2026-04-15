# AI Model Recommender
# A CLI tool that recommends the best AI model based on your use case and budget.

# WHAT YOU NEED TO KNOW FROM TODAY'S LECTURE:
# - match statement: like if/elif but cleaner for exact value matching
#   match variable:
#       case "value1":
#           ...
#       case "value2":
#           ...
#       case _:          # _ means "anything else" (like else)
#           ...
#
# - Chaining comparisons: 0 <= budget < 20 means budget is between 0 and 19
# - Boolean: True / False — used to check yes/no answers
#   vision = input("...") == "yes"   → this gives True if user types "yes", False otherwise

# INSTRUCTIONS:
# 1. Define a main() function
# 2. Ask for use case: "What do you need AI for? (chat / code / image / speed): "
# 3. Ask for monthly budget: "Monthly budget in $? " — convert to int
# 4. Ask for vision support: "Do you need image/vision support? (yes/no): "
#    Convert the answer to a boolean: vision = answer == "yes"
# 5. Use a match statement on the use case:
#    case "code":
#        if budget == 0:
#            print recommended model for free code use
#        elif 0 < budget <= 20:
#            print recommended model for budget code use
#        else:
#            print recommended model for premium code use
#    case "chat":
#        same structure — free / budget / premium
#    case "image":
#        check if vision is True — if not, print a warning
#        then recommend based on budget
#    case "speed":
#        recommend based on budget
#    case _:
#        print("Invalid option.")
# 6. At the end of each recommendation, print one line explaining why
# 7. Call main() at the bottom

# MODELS TO USE IN YOUR RECOMMENDATIONS (pick what makes sense per case):
# Free:    Groq (Llama 3.3 70B), Google Gemini Free, Claude Free
# Budget:  GPT-4o Mini ($), Gemini Pro ($), Claude Haiku ($)
# Premium: GPT-4o, Claude Opus, Gemini Ultra

# YOUR CODE BELOW:

def main():
    use_case = input("What do you need AI for? (chat / code / image / speed) ")
    budget = int(input("Monthly budget in $? "))
    answer = input("Do you need image/vision support? (yes/no) ")
    vision = answer == "yes"
    match use_case:
        case "code":
            if budget == 0:
                print("Groq")
            elif 0 < budget <= 20:
                print("GPT-4o")
            else:
                print("Opus")
        case "chat":
            if budget == 0:
                print("Groq")
            elif 0 < budget <= 20:
                print("GPT-4o")
            else:
                print("Opus")
        case "image":
            if not vision:
                print("Warning: you selected image but said no to vision support")
            if budget == 0:
                print("Groq")
            elif 0 < budget <= 20:
                print("GPT-4o")
            else:
                print("Gemini ULTRA")
        case "speed":
            if budget == 0:
                print("Groq")
            elif 0 < budget <= 20:
                print("GPT-4o")
            else:
                print("Opus")
        case _:
            print("Invalid option")
main()