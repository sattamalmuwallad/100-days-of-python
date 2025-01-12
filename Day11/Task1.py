from pic import sattam ## The name of the image is sattam
import random

def score(data):
    if sum(data) == 21 and len(data) == 2:
        return 21  
    if 11 in data and sum(data) > 21:
        data.remove(11)
        data.append(1)  
    return sum(data)
    
         
def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def result(p_score,c_score):
    if p_score == c_score:
        return "Tie"
    elif p_score == 21:
        return "You win! 😁"
    elif c_score == 21:
        return "You lose😭"
    elif p_score > 21:
        return "You went over. You lose😭"
    elif c_score > 21:
        return "Computer went over. You win! 😁"
    elif p_score > c_score:
        return "You win! 😁"
    else: return "You lose😭"
    
    


def playgame():
    print(sattam)
    player_hand = [deal(),deal()]
    computer_hand = [deal(),deal()]

    gameover = False
    while not gameover:
        playerScore = score(player_hand)
        computerScore = score(computer_hand)

        print(f"your cards:{player_hand}, current score: {playerScore}")
        print(f"Computer First Card: {computer_hand[0]}")

        if playerScore == 21 or playerScore > 21:
            gameover=True
        else: 
            cont = input("Type 'y' to get another card or type 'n' to pass: ")
            if cont.lower() == "y":
                player_hand.append(deal())
            else:
                gameover = True

    while computerScore != 21 and computerScore < 17:
        computer_hand.append(deal())
        computerScore = score(computer_hand)

    print(f"Your final hand: {player_hand}, final Score: {playerScore}")
    print(f"Computer's final hand: {computer_hand}, final Score: {computerScore}")      
    print(result(playerScore,computerScore))



while True:
    playgame()
    call = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if call.lower() != "y":
        break