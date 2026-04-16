# Mario Level Runner
#        ? ? ? 
# A terminal game where Mario fights through 5 levels
# Pick the right move to defeat each enemy. Wrong move= lose a life.

def main():

    levels =[
    {"enemy": "Goomba", "status": "is attacking", "moves": ["hit", "jump", "slide"], "correct": 1},
    {"enemy": "DINO", "status": "is huge, what now?", "moves": ["throw rocks", "kill", "run"], "correct": 2},
    {"enemy": "Pumba", "status": "is attacking you", "moves": ["fight", "use smoke", "head kick"], "correct": 0},
    {"enemy": "Drogo", "status": "is holding the mushroom", "moves": ["fire", "steal mushroom", "friendly approach"], "correct": 1},
    {"enemy": "Bibi", "status": "has a present for you(?)", "moves": ["kick", "return mushroom", "run"], "correct": 1},
    ]
    lives = 3
    score = 0 

    for level in levels:
        print(f"\nLives: {lives} | Score: {score}")
        
        print(level["enemy"], level["status"])
        for i in range(len(level["moves"])):
            print(i +1, level["moves"][i], sep="-")

        while True:
            answer = input("What are you going to do? ")
            if answer in ["1", "2", "3"]:
                answer = int(answer)
                break
            print("Invalid: Try again")

        if answer == level["correct"] + 1:
            score += 100
            print(f"You won this fight!")
        else: 
            answer != level["correct"]
            score -= 100
            lives -= 1 
            print("You lost the fight")
        if lives == 0:
            print(f"Game Over! You were defeated by {level['enemy']}")
            return

    print("You are the WINNER!")
    print(f"Lives: {lives} | Score: {score}")

main()

   
    

    
