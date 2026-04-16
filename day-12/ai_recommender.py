# AI Model Recommender
# A CLI tool that recommends the best AI model based on your use case and budget.

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