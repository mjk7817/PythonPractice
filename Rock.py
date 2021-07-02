import random
choice = ["Rock", "Paper", 'Scissors']
computer = random.choices(choice)
player = False
cpuScore=0
playerScore = 0

while True:
    player = input("Rock, Paper, or Scissors? ").capitalize()
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose! ", computer, "covers ", player )
            cpuScore +=1
        else:
            print("You win!", player, " covers ", computer)
            playerScore+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose! ", computer, "cuts ", player)
            cpuScore+=1
        else:
            print("You win!", player, " covers ", computer)
            playerScore += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose... ", computer, "smashes ", player)
            cpuScore+=1
        else:
            print("You win! ", computer, "cuts ", player)
            playerScore+=1
    elif player == 'End':
        print("Final Scores:")
        print(f"CPU:{cpuScore}")
        print(f"Player:{playerScore}")
        break



