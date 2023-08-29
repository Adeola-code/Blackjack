############### Blackjack Project #####################

import random
from replit import clear
import art
#Create a deal_card() function that uses the List below to *return* a random card.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    card = random.choice(cards)
    return card
#Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 

def calculate_score(list):
    """Take a list of cards and return the score calculated from the cards"""
# Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if len(list)==2 and sum(list)==21:    
        return 0
        calculate_score()
#Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in list and sum(list) >21:
        list.remove(11)
        list.append(1)
    return sum(list)
 #Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if computer_score==user_score:
        return "It's a draw 🙃"
    elif computer_score==0:
        return "You lose, opponent has a blackjack😫"
    elif user_score==0:
        return "You win with a blackjack😎"
    elif user_score>21:
        return "You lose. You went over😯"
    elif computer_score>21:
        return "You win. Opponent went over😊"
    elif computer_score > user_score:
        return "You lose😭"
    else:
        return "You win🙃"  
# Deal the user and computer 2 cards each using deal_card() and append().
def play_game():
    print(art.logo)
    user_cards = []
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    game_ends=False
    computer_cards = []
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    #The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    
    while not game_ends:
        #Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards: {user_cards},current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if computer_score==0 or user_score==0 or user_score>21:
            game_ends=True
        else:
            #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            draw_card=input("Do you want to draw another card? 'y' or 'n' ")
            if draw_card=="y":
                user_cards.append(deal_card())
            else:
                game_ends=True
        
        
    
    #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score!= 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(f"Your final hand is {user_cards}, your final score is {user_score}")
    print(f"Computer's final hand:{computer_cards},computer's final score: {computer_score}")
    print(compare(user_score,computer_score))
#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blacjack? 'y' or 'n' ").lower()=="y":
    clear()
    play_game()    

