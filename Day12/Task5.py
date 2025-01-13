from random import randint
easylife = 10
hardlife = 5
def image():
      return r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

def check_guess(user,computer,lifes):
      if user > computer:
          print("Too High")
          return lifes -1 
      elif user < computer:
            print("Too Low")
            return lifes -1 
      else: print(f"You got it! The answer was {computer}")

def difficulty():
      level = input("Choose Diffculty. Type 'easy' and 'hard': ")
      if level.lower() == "easy":
            return easylife
      elif level.lower() == "hard":
            return hardlife
      else: 
        print("Wrong input enter either easy or hard please")
        exit()
def game():
    """Main game logic."""
    print(image())
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.") 
    computerguess = randint(1, 100)
    print(f"(Debug) The answer is {computerguess}") 
    lifes = difficulty()
    guess = -99 
    while guess != computerguess:
        print(f"You have {lifes} lives remaining.")
        
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        lifes = check_guess(guess, computerguess, lifes)
        
        if lifes == 0:
            print("You've run out of guesses, you lose.")
            break
        elif guess != computerguess:
            print("Guess again.")
                
game()