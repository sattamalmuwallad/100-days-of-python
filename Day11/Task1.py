from pic import sattam ## The name of the image is sattam
import random

def score(data):
    if add(data) == 21 and len(data)==2:
        return -1
    if 11 in data and add(data) > 21:
        data.remove(11)
        data.append(1)
    return add(data)
    
         
def add(hand):
    sum = 0
    for i in hand:
        sum += i
    return sum


def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)



def play(): 
    print(sattam)
    player_hand = [deal(),deal()]
    computer_hand = [deal(),deal()]
    gameover = False

    while not gameover:
        playerScore = score(player_hand)
        computerScore = score(computer_hand)

        print(f"your cards:{player_hand}, current score: {playerScore}")
        print(f"Computer First Card: {computer_hand[0]}")

        if playerScore == -1 or playerScore > 21:
            gameover=True
        else: 
            cont = input("Type 'y' to get another card or type 'n' to pass: ")
            if cont.lower() == "y":
                player_hand.append(deal())
            else:
                gameover = True

        
    
while True:
    play()
    call = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if call.lower() != "y":
        break

