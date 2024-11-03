import random

user_wins = 0
computer_wins = 0

choices = ("rock", "papper", "scissors")




while True:
    computer_choice = random.choice(choices)
    user_choice = input("Type rock/paper/scissors or q to quit: ").lower()
    computer_choice
    if user_choice == "q":
        break
    
    if user_choice not in choices:
        continue

    if user_wins == 3 or computer_wins == 3:
        print(f"The game is over! Your score is {user_wins}. Computer score is {computer_wins}")
        break
    
        
    if user_choice == computer_choice:
        print(f"Computer picked {computer_choice} \n It was a tie!")
        continue

    elif user_choice == "rock" and computer_choice == "scissors":
        user_wins += 1
        print(f"Computer picked {computer_choice}. You won!")
        
    
    elif user_choice == "scissors" and computer_choice == "papper":
        user_wins += 1
        print(f"Computer picked {computer_choice}. You won!")
        

    elif user_choice == "papper" and computer_choice == "rock":
        user_wins += 1
        print(f"Computer picked {computer_choice}. You won!")
        

    else:
        computer_wins += 1
        print(f"Computer picked {computer_choice}. You lost!")
        continue
    



print("Goodbye!")







