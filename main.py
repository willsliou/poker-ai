# class Card:
#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value

        
# class Deck:
#     def __init__(self):
        
# class Player:
#     def __init__(self):


# Blackjack Rules
# 2 cards
# Goal: Get closest value to 21 without going over. 
# Go over 22 and you lose.
# Suit cards are all 10. Ace is 1 (for simplicity)

import random as random # random library in python uses Mersenne Twister randomizer
# https://docs.python.org/3/library/random.html#:~:text=Python%20uses%20the%20Mersenne%20Twister,random%20number%20generators%20in%20existence.


deck = [1,2,3,4,5,6,7,8,9,10]
# lfsr = 0xACE1u

# bit  = ((lfsr >> 0) ^ (lfsr >> 2) ^ (lfsr >> 3) ^ (lfsr >> 5) ) & 1;
# return lfsr =  (lfsr >> 1) | (bit << 15);


# Player values
player1 = 0
player2 = 0

# while (player1 <= 21 and player2 <= 21):
    
p1_input = False;
p2_input = False;
p1_num = 0;
p2_num = 0;

while (p1_num <= 21 and p2_num <= 21):

    # Get value for Player 1
    p1_input = input("Would you like to hit (Y) or stay? (N) ")

    # Check input
    # Set input
    if p1_input == "Y" or p1_input == "y":
        p1_input = True
    else:
        p1_input = False

    # If player 1 wants to hit
    if (p1_input == True):
        # Pick random.choice from sequence (array in deck) and assign it to randomNumber_1
        randomNumber_1 = random.choice(deck)
        print("Player 1 hit and got: ", randomNumber_1)
        p1_num += randomNumber_1
    else:
        print("Player 1 stayed.")
    # Check if Player 1 went over and lost the game
    if p1_num > 21:
        print("Player 1 lost with : ", p1_num)
        break

    # Print out current scores
    print("P1: ", p1_num, " " , "P2: ", p2_num)
    


    # Get value for Player 2
    p2_input = input("Would you like to hit (Y) or stay? (N) ")
    if p2_input == "Y" or p2_input == "y":
        p2_input = True
    else:
        p2_input = False

    if (p2_input == True):
        randomNumber_2 = random.choice(deck)
        print("Player 2 hit and got: ", randomNumber_2)
        p2_num += randomNumber_2
    # Check if Player 2 went over and lost the game
    if p2_num > 21:
        print("Player 2 lost with: ", p2_num)
        break

    # Print out current scores
    print("P1: ", p1_num, " " , "P2: ", p2_num)

    # Check winners
    if (p1_num == 21 and p2_num == 21):
        print("Tie.")
        break
    elif (p1_num == 21):
        print("Player 1 wins!")
    elif (p2_num == 21):
        print("Player 2 wins!")
        

