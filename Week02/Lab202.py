choices = ["Rock", "Paper", "Scissors"]

playerInput = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")
playerChoice = int(playerInput)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
else:
    compInput = input("Enter computer's choice (1-3): ")
    computerChoice = int(compInput)
    
    if computerChoice < 1 or computerChoice > 3:
        print("Error: Choice must be between 1 and 3.")
    else:
        pName = choices[playerChoice - 1]
        cName = choices[computerChoice - 1]
        
        print(f"You chose: {pName}")
        print(f"Computer chose: {cName}")

        if playerChoice == computerChoice:
            print("It's a tie!")
        elif playerChoice == 1 and computerChoice == 3:
            print("Rock beats Scissors - You win!")
        elif playerChoice == 2 and computerChoice == 1:
            print("Paper beats Rock - You win!")
        elif playerChoice == 3 and computerChoice == 2:
            print("Scissors beats Paper - You win!")
        else:
            print("You lose!")

        if pName != "Rock":
            print("You didn't pick the classic Rock...")