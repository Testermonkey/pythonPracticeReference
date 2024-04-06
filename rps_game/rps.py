#
#   Rock, Paper, Sissors
#   input user_choice
#   computer_choice random
#   user centric decision tree
#   1-rock
#   2-paper
#   1-sissors
import random

def results(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("draw")
        print(f"user choice {user_choice}")
        print(f"computer_choice, {computer_choice}")
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("user wins, rock covers paper")
        print(f"user choice {user_choice}")
        print(f"computer_choice, {computer_choice}")
    elif user_choice == 'sissors' and computer_choice == 'paper':
        print("user wins, sissors cuts paper")
        print(f"user choice {user_choice}")
        print(f"computer_choice, {computer_choice}")
    elif user_choice == 'rock' and computer_choice == 'sissors':
        print("user wins, rock breaks sissors")
        print(f"user choice {user_choice}")
        print(f"computer_choice, {computer_choice}")
    elif computer_choice == 'rock' and user_choice == 'sissors':
        print("computer wins, rock breaks sissors")
        print(f"user choice {user_choice}")
        print(f"computer_choice, {computer_choice}")
    elif computer_choice == 'sissors' and user_choice == 'paper':
        print("computer wins, sissors cuts paper")
        print(f"user choice {user_choice}")
        print(f"computer_choice, {computer_choice}")
    elif computer_choice == 'paper' and user_choice == 'rock':
        print("computer wins, paper covers rock")
        print(f"user choice {user_choice}")
        print(f"computer_choice, {computer_choice}")
        
choices = ['rock', 'paper', 'sissors']
computer_choice = random.choice(choices)


while True:
    user_choice = input(f"rock\npaper\nsissors\n..")
    if user_choice in choices:
        #print(f"user choice, {user_choice} ")
        break


results(user_choice, computer_choice)

