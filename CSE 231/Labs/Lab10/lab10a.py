##
## Demonstrate some of the operations of the Deck and Card classes
##

import cards

# Seed the random number generator to a specific value so every execution
# of the program uses the same sequence of random numbers (for testing).

import random
random.seed( 100 )

def display_outcome(player1_card,player2_card):
    print()
    if player1_card.rank() == 3:
        player1_card.rank() = 100
        
    if player1_card.rank() == player2_card.rank():
        print( "Tie:", player1_card, "and", player2_card, "of equal rank \n" )
    elif player1_card.rank() > player2_card.rank():
        print( "Player #1 wins:", player1_card, "of higher rank than", player2_card,'\n' )
    else:
        print( "Player #2 wins:", player2_card, "of higher rank than", player1_card,'\n' )

# Create a deck of cards

my_deck = cards.Deck()


# Shuffle the deck, then display it in 13 columns

my_deck.shuffle()
print( "===== shuffled deck =====" )
my_deck.display()


# Deal five cards to each player (alternating)

print( "Dealt five cards to each player (alternating)" )
print()

player1_list=[]
player2_list=[]
for i in range( 5 ):
    player1_list.append( my_deck.deal() )
    player2_list.append( my_deck.deal() )

# Display each player's cards and the cards still in the deck

print( "===== player #1 =====" )
print()
print( player1_list )
print()
print( "===== player #2 =====" )
print()
print( player2_list )
print()
print( "===== remaining cards in deck =====" )
my_deck.display()


# First card dealt to Player #1
player1_card = player1_list.pop( 0 )
print( "First card dealt to player #1:", player1_card )
print("Player #1 hand:",player1_list)
# First card dealt to Player #2
player2_card = player2_list.pop( 0 )
print( "First card dealt to player #2:", player2_card )
print("Player #2 hand:",player2_list)

display_outcome(player1_card, player2_card)

player1_card = player1_list.pop( 0 )
print( "Second card dealt to player #1:", player1_card )
print("Player #1 hand:",player1_list,'\n')

player2_card = player2_list.pop( 0 )
print( "Second card dealt to player #2:", player2_card )
print("Player #2 hand:",player2_list,'\n')

player1_card = player1_list.pop()
print("Last card in hand of player #1:", player1_card)
player2_card = player2_list.pop()
print("Last card in hand of player #2:", player2_card)

if player1_card.rank() > player2_card.rank():
    print('\n',player1_card, "of higher rank than", player2_card)
else:
    print('\n',player2_card, "of higher rank than", player1_card)
# Compare the ranks of the two cards
