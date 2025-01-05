import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]

print("Welcome to Rock Paper Scissors!")
computer = random.choice(choice)
user = input("Please enter your choice: Rock, Paper or Scissors: ").lower()
if user == "rock" or user == "paper" or user == "scissors":
    if user == "scissors" and computer == rock:
        print(f"Your choice: {choice[2]}")
        print(f"Computer chose: {computer}")
        print("You lose")
    elif user == "rock" and computer == paper:
        print(f"Your choice: {choice[0]}")
        print(f"Computer chose: {computer}")
        print("You lose")
    elif user == "paper" and computer == scissors:
        print(f"Your choice: {choice[1]}")
        print(f"Computer chose: {computer}")
        print("You lose")
    elif user == "scissors" and computer == paper:
        print(f"Your choice: {choice[2]}")
        print(f"Computer chose: {computer}")
        print("You win")
    elif user == "rock" and computer == scissors:
        print(f"Your choice: {choice[0]}")
        print(f"Computer chose: {computer}")
        print("You win")
    elif user == "paper" and computer == rock:
        print(f"Your choice: {choice[1]}")
        print(f"Computer chose: {computer}")
        print("You win")
    else:
        print(f"Your choice: {user}")
        print(f"Computer chose: {computer}")
        print("It's a draw")
else:
    print("Invalid input. Please try again.")
    exit(1)