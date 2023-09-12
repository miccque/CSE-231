###############################################################################
#  Computer Project 6  
#  Simplified Texas Hold'em Poker 
#
#  This program provides functions to evaluate poker hands based on a given set
#  of cards in order to simulate a game of Texas Hold'em Poker. It includes 
#  functions to check for different hand combinations and to execute the optimal 
#  hand. After it compares both player's best hand a winner is determined and
#  players are allowed to continue playing until the deck runs out of available
#  cards. 
# 
# Functions:
#    sort_cards(cards): Sorts a list of cards in ascending order of rank and suit.
#    
#    sort_key(card): Key function used for sorting cards by rank and suit.
#    
#    less_than(c1,c2): Returns True if c1 is smaller in rank, True if ranks are 
#       equal and c1 has a 'smaller' suit, False otherwise
#    
#    min_in_list(L): Return the index of the mininmum card in L
#    
#   cannonical(H): Selection Sort: find smallest and swap with first in H,
#       then find second smallest (smallest of rest) and swap with second in H,
#       and so on...
#
#   flush_7(H): Checks if a hand contains a flush of at least 5 cards of the same 
#       suit.
#
#   straight_7(H): Checks if a hand contains a straight of at least 5 consecutive 
#       cards.
#
#   straight_flush_7(H): Checks if a hand contains a straight flush of at least 
#       5 consecutive cards of the same suit.
#   
#   four_7(H): Checks if a hand contains four cards of the same rank.
#
#   three_7(H): Checks if a hand contains three cards of the same rank.
#
#   two_pair_7(H): Checks if a hand contains two distinct pairs of cards with 
#       the same rank.
#
#   one_pair_7(H): Checks if a hand contains a pair of cards with the same rank.
#
#   full_house_7(H): Checks if a hand contains a full house combination.
#
#   main(): Entry point of the program, creates the deck, hands, community cards,
#       and determines the winner of the round.            
###############################################################################

import cards

def sort_cards(cards):
    """
    Sorts a list of cards in ascending order of rank and suit.
    
    Parameters:
        cards (list): A list of cards to be sorted.
    
    Returns:
        sorted_cards (list): A new list of cards sorted in descending order, 
            with the highest ranked cards first. Within the same rank, the cards 
            are sorted by suit rank.
    """    
    sorted_cards = sorted(cards, key=sort_key)
    # Returns cards in order of smallest to greatest with suit and rank
    return sorted_cards

def sort_key(card):
    """
    Key function used for sorting cards by rank and suit
    
    Parameters:
        card (Card): A card to determine the sorting key.
    
    Returns:
        card.rank() (int): An int containing the cards rank for sorting purposes 
        card.suit() (int): An int containing the cards suit for sorting purposes
    """
    # Cards will be sorted by rank in ascending order and then by suit in descending order.
    return card.rank(), card.suit()

def less_than(c1,c2):
    '''Return 
           True if c1 is smaller in rank, 
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise'''
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False
    
def min_in_list(L):
    '''Return the index of the mininmum card in L'''
    min_card = L[0]  # first card
    min_index = 0
    for i,c in enumerate(L):
        if less_than(c,min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index
        
def cannonical(H):
    ''' Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on...'''
    for i,c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i 
        H[i], H[min_index] = H[min_index], c  # swap
    return H

def flush_7(H):
    """
    Checks if a hand contains a flush of at least 5 cards of the same suit.

    Creates a dictionary containing suits and then iterates through H card by card
    appending that card's suit to the suit dictionary. Then iterates through
    each suit in the suit dict to see if they have at least 5 elements. If
    they do then the elements are sorted and a list of the first 5 are returned.
    If these conditions are not met False is returned
    
    Parameters:
        H (list): A list of cards representing a hand + community cards.
    
    Returns:
        sorted_suit[:5] (list): If a flush is found, returns a list of the first 
            five cards of the same suit.
        False (Bool): If no flush is found, returns False.
    """
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4
    FLUSH = 5
    
    # Dict to store cards for each suit
    suits = {
        CLUBS: [],
        DIAMONDS: [],
        HEARTS: [],
        SPADES: []
        }
    # Iterate over each card in hand and organize them by their suit
    for card in H:
        suit = card.suit()
        suits[suit].append(card)
    
    # Check each suit to find a flush
    for suit in (CLUBS, DIAMONDS, HEARTS, SPADES):
        if len(suits[suit]) >= FLUSH:
            sorted_suit = sort_cards(suits[suit])
            # Return the first 5 cards from the suit with a flush
            return sorted_suit[:5]

    return False # No flush found return False

def straight_7(H):
    """
    Checks if a hand contains a straight of at least 5 consecutive cards.
    
    Sorts the hand and then creates three new lists. First list contains the
    first 5 cards of the sorted list, middle contains the middle five cards,
    and the rear contains the last five cards of the list. Then a final list
    called straight_hand is created to store a list which contains a straight.
    Then each of the three lists containing cards are iterated and checked to
    see if they meet the definition of a straight, if they do then straight_hand
    is given that lists value and is returned. If straight_hand is empty
    at the end of the process then False is returned.
    
    Parameters:
        H (list): A list of cards representing a hand + community cards.
    
    Returns:
        sorted_suit[:5] (list): If a straight is found, returns a list of the 
            straight.
        False (Bool): If no straight is found, returns False.
    """
    sorted_hand = sort_cards(H) # Sorts the hand in ascending order
    
    # Divide the hand into three sets of five cards each
    first_set = sorted_hand[:5] # Get the first five cards
    middle_set = sorted_hand[1:-1] # Get the middle five cards
    rear_set = sorted_hand[-5:] # Get the last five cards
    
    straight_hand = [] # Variable to track if the hand represents a straight
    
    # Checks if the first five elements are in sequential order
    is_straight = True # Tracks if the current set is a straight
    for i in range(len(first_set) -1 ):
        # Checks if the rank of the current card is not the rank of the next card -1
        if first_set[i].rank() != first_set[i + 1].rank() - 1:
            # If the condition is not satisfied, it isnt a straight
            is_straight = False
            break
        
    if is_straight:
        straight_hand = first_set
    
    # Checks if the middle five elements are in sequential order
    if not straight_hand:
        is_straight = True
        for i in range(len(middle_set) -1 ):
            # Checks if the rank of the current card is not the rank of the next card -1
            if middle_set[i].rank() != middle_set[i +1].rank() - 1:
                # If the condition is not satisfied, it isnt a straight
                is_straight = False
                break
        
        if is_straight:
            straight_hand = middle_set
    
    # Checks if the last five elements are in sequential order
    if not straight_hand:
        is_straight = True
        for i in range(len(rear_set) -1 ):
            # Checks if the rank of the current card is not the rank of the next card -1
            if rear_set[i].rank() != rear_set[i +1].rank() - 1:
                # If the condition is not satisfied, it isnt a straight
                is_straight = False
                break
        
        if is_straight:
            straight_hand = rear_set
        
    if straight_hand:
        # Returns the hand representing a straight
        return straight_hand
    
    return False # No straight is found return False
        
def straight_flush_7(H):
    """
    Checks if a hand contains a straight flush of at least 5 consecutive cards 
    of the same suit.
    
    Creates a dictionary containing suits and then iterates through H card by card
    appending that card's suit to the suit dictionary. Then iterates through
    each suit in the suit dict to see if they have at least 5 elements. If the
    condition is met then a new list is created by sorting the corresponding
    suit list. Then the sorted list containing the flush cards is iterated and 
    checked to see if they meet the definition of a straight, if they do then 
    the sorted list is returned. If false then False is returned.

    Parameters:
        H (list): A list of cards representing a hand + community cards.
    
    Returns:
        sorted_hand (list): If a straight flush is found, returns a list of the 
            straight flush.
        False (Bool): If no straight flush is found, returns False.
    """
    CLUBS = 1 
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4
    FLUSH = 5
    
    # Dict to store cards for each suit
    suits = {
        CLUBS: [],
        DIAMONDS: [],
        HEARTS: [],
        SPADES: []
        }
    
    # Iterate over each card in hand and organize them by their suit
    for card in H:
        suit = card.suit()
        suits[suit].append(card)
    
    # Check each suit to find a flush
    for suit in (CLUBS, DIAMONDS, HEARTS, SPADES):
        if len(suits[suit]) >= FLUSH:  
            
            # Sort the first five cards by their rank and suit
            sorted_hand = sort_cards(suits[suit][:5])
            
            # Initializes straight_flush
            straight_flush = True
            
            # Iterates through the indices of the sorted cards list
            for i in range(len(sorted_hand) -1 ):
                # Checks if the rank of the current card is not the rank of the next card -1
                if sorted_hand[i].rank() != sorted_hand[i + 1].rank() - 1:
                    # If the condition is not satisfied, it isnt a straight flush
                    straight_flush = False
            
            if straight_flush:
                #Returns straight flush
                return sorted_hand
            
    return False # No straight-flush found return False

def four_7(H):
    """
    Checks if a hand contains four cards of the same rank.
    
    Sorts the hand and then iterates over the sorted hand to see if four cards
    have the same rank. If this condition is met then a list containing those
    cards are returned, if not False is returned.
    
    Parameters:
        H (list): A list of cards representing a hand + community cards.
    
    Returns:
        four (list): If a four of a kind is found, returns a list containing the 
            four of a kind.
        False (Bool): If no four of a kind is found, returns False.
    """
    sorted_hand = sort_cards(H) # Sorts the hand in ascending order
    FOUR_OF_A_KIND = 4 # Constant representing the number of cards for four of a kind
    
    # Iterate over the sorted hand to find four of a kind
    for i in range(len(sorted_hand) - FOUR_OF_A_KIND + 1):
        # If four cards have the same rank, return them as four of a kind
        if (sorted_hand[i].rank() == sorted_hand[i + 1].rank() and
        sorted_hand[i + 1].rank() == sorted_hand[i + 2].rank() and
        sorted_hand[i + 2].rank() == sorted_hand[i + 3].rank()):
            four = sorted_hand[i:i + FOUR_OF_A_KIND]
            return four
        
    return False # No four of a kind is found return False

def three_7(H):
    """
    Checks if a hand contains three cards of the same rank.
    
    Sorts the hand and then iterates over the sorted hand to see if three cards
    have the same rank. If this condition is met then a list containing those
    cards are returned, if not False is returned.
    
    Parameters:
        H (list): A list of cards representing a hand + community cards.
    
    Returns:
        four (list): If a three of a kind is found, returns a list containing the 
            three of a kind.
        False (Bool): If no three of a kind is found, returns False.
    """
    sorted_hand = sort_cards(H)  # Sorts the hand in ascending order
    THREE_OF_A_KIND = 3 # Constant representing the number of cards for three of a kind
    
    # Iterate over the sorted hand to find three of a kind
    for i in range(len(sorted_hand) - THREE_OF_A_KIND + 1):
        if (sorted_hand[i].rank() == sorted_hand[i + 1].rank() and
            sorted_hand[i + 1].rank() == sorted_hand[i + 2].rank()):
            # If three cards have the same rank, return them as three of a kind
            three = sorted_hand[i:i + THREE_OF_A_KIND]
            return three
    
    return False # No three of a kind found return False
        
def two_pair_7(H):
    """
    Checks if a hand contains two distinct pairs of cards with the same rank.
    
    Sorts the hand and creates an empty list to store pairs found in the hand
    then iterates over the sorted hand to find pairs of the same rank. If pairs 
    are found they are extracted and appended to the list containing pairs.
    After iterating through the hand the list containing pairs is checked to
    see if there are at least two distinct pairs by first checking there are at
    least two pairs and then iterates through the pairs to ensure their values
    are unique. If this condition is met then a list containing those
    pairs are returned, if not False is returned.
    
    Parameters:
        H (list): A list of cards representing a hand + community cards.
    
    Returns:
        pairs[0] + pairs[1] (list): If two pairs are found returns a list of the 
            two pairs of cards.
        False (Bool): If no two pairs are found, returns False.
    """
    sorted_hand = sort_cards(H) # Sorts the hand in ascending order
    PAIR_VAL = 2 # Constant representing the number of cards for two of a kind
    pairs = [] # List to store the pairs found in the hand
    
    # Iterate over the sorted hand to find pairs
    for i in range(len(sorted_hand) - 1):
        if sorted_hand[i].rank() == sorted_hand[i + 1].rank():
            # Extract the pair of cards with the same rank
            pair = [sorted_hand[i], sorted_hand[i + 1]]
            if pair not in pairs:
                pairs.append(pair)
    
    # Checks if two distinct pairs are found by first checking there are at least two
    # pairs and then iterates through the pairs to ensure their values are unique               
    if len(pairs) >= PAIR_VAL and \
        len(set([card.rank() for pair in pairs for card in pair])) >= PAIR_VAL:
        # Returns a list of the two pairs
        return pairs[0] + pairs[1]
    
    return False # No two pairs are found return False

def one_pair_7(H):
    """
    Checks if a hand contains a pair of cards with the same rank.
    
    Sorts the hand of cards and stores the sorting in a list. Then iterates over
    the sorted list to find a pair of the same rank. If one is found the pair
    is stored into a list and then returned. If no pair is found False is 
    returned.
    
    Parameters:
        H (list): A list of cards representing a hand + community cards.
    
    Returns:
        pair (list): If a pair is found returns a list of the pairs of cards.
        False (Bool): If no two pairs are found, returns False.
    """    
    sorted_hand = sort_cards(H) # Sorts the hand in ascending order
    
    for i in range(len(sorted_hand) - 1):
        if sorted_hand[i].rank() == sorted_hand[i + 1].rank():
            pair = [sorted_hand[i], sorted_hand[i+1]]
            return pair

    return False # No pair found return False

def full_house_7(H):
    """
    Checks if a hand contains a full house combination.
    
    Creates a copy of the hand, then the copy is sent to the function three_7()
    to determine if there is a three of a kind. If true then the values are stored
    in a variable and then removed from the hand. The modified hand is then sent
    to one_pair_7() to determine if there is a pair. If a pair is found
    then a list is created using the three of a kind and one pair lists, then
    returned. If these conditions are not all met False is returned.
    
    Parameters:
        H (list): A list of cards representing a hand + community cards.
    
    Returns:
        full_house (list): If a full house is found a list containing the full 
            house combination is returned.
        False (Bool): If no full house is found, returns False.
    """    
    hand = H.copy() # Create a copy of the hand list
    three_of_a_kind = three_7(hand) # Find three of a kind in the hand
    
    if three_of_a_kind:
        for card in three_of_a_kind:
            hand.remove(card) # Remove the three of a kind cards from the hand
            
        pair = one_pair_7(hand) # Find a pair in the modified hand
        
        if pair:
            if less_than(pair[0], three_of_a_kind[0]):
                # Create a full house with three of a kind + pair
                full_house = three_of_a_kind + pair 
            else:
                # Create a full house with a pair + three of a kind
                full_house = pair + three_of_a_kind
                
            return full_house # Return the full house combination
        
    return False # No full house is found return False

def main():
    D = cards.Deck() # Creates a deck of cards
    D.shuffle() # Shuffles the deck
    
    while True:
        # Initializes empty lists for community cards, player 1's hand, and player 2's hand
        community_list=[]
        hand_1_list=[]
        hand_2_list=[]
        
        # Deals community cards
        for i in range(5):
            community_list.append(D.deal())
        
        # Deals player 1's hand
        for i in range(2):
            hand_1_list.append(D.deal())
        
        # Deals player 2's hand
        for i in range(2):
            hand_2_list.append(D.deal())
        
        # Print game display info
        print()
        print("-"*40)
        print("Let's play poker!\n")
        print("Community cards:",community_list)
        print("Player 1:",hand_1_list)
        print("Player 2:",hand_2_list)
        print()
        
        # Combine community cards with player 1's and player 2's hands
        combined_hand_1 =community_list + hand_1_list
        combined_hand_2 = community_list +hand_2_list
        
        
        # Check the winning hands and determine the winner
        # These functions check if a hand has a specific poker combination and 
        # returns the combination if it exists. Then compare the hands and prints
        # the sorted winning result.
        
        # Checking for a straight flush
        if straight_flush_7(combined_hand_1) and straight_flush_7(combined_hand_2):
            print("TIE with a straight flush:", 
                  sort_cards(straight_flush_7(combined_hand_1)))
            
        elif straight_flush_7(combined_hand_1):
            print("Player 1 wins with a straight flush:", 
                  sort_cards(straight_flush_7(combined_hand_1)))
        
        elif straight_flush_7(combined_hand_2):
            print("Player 2 wins with a straight flush:", 
                  straight_flush_7(combined_hand_2))
        
        # Checking for four of a kind
        elif four_7(combined_hand_1) and four_7(combined_hand_2):
            print("TIE with four of a kind:", 
                  sort_cards(four_7(combined_hand_1)))

        elif four_7(combined_hand_1):
            print("Player 1 wins with four of a kind:", 
                  sort_cards(four_7(combined_hand_1)))
        
        elif four_7(combined_hand_2):
            print("Player 2 wins with four of a kind:", 
                  sort_cards(four_7(combined_hand_2)))
        
        # Checking for a full house
        elif full_house_7(combined_hand_1) and full_house_7(combined_hand_2):
            print("TIE with a full house:", 
                  sort_cards(full_house_7(combined_hand_1)))
        
        elif full_house_7(combined_hand_1):
            print("Player 1 wins with a full house:", 
                  sort_cards(full_house_7(combined_hand_1)))
        
        elif full_house_7(combined_hand_2):
            print("Player 2 wins with a full house:", 
                  sort_cards(full_house_7(combined_hand_2)))
        
        # Checking for a flush
        elif flush_7(combined_hand_1) and flush_7(combined_hand_2):
            print("TIE with a flush:", 
                  sort_cards(flush_7(combined_hand_1)))
        
        elif flush_7(combined_hand_1):
            print("Player 1 wins with a flush:", 
                  sort_cards(flush_7(combined_hand_1)))
        
        elif flush_7(combined_hand_2):
            print("Player 2 wins with a flush:", 
                  sort_cards(flush_7(combined_hand_2)))
        
        # Checking for a straight
        elif straight_7(combined_hand_1) and straight_7(combined_hand_2):
            print("TIE with a straight:", 
                  sort_cards(straight_7(combined_hand_1)))
        
        elif straight_7(combined_hand_1):
            print("Player 1 wins with a straight:", 
                  sort_cards(straight_7(combined_hand_1)))
        
        elif straight_7(combined_hand_2):
            print("Player 2 wins with a straight:", 
                  sort_cards(straight_7(combined_hand_2)))
        
        # Checking for a three of a kind
        elif three_7(combined_hand_1) and three_7(combined_hand_2):
            print("TIE with three of a kind:", 
                  sort_cards(three_7(combined_hand_1)))
        
        elif three_7(combined_hand_1):
            print("Player 1 wins with three of a kind:", 
                  sort_cards(three_7(combined_hand_1)))
        
        elif three_7(combined_hand_2):
            print("Player 2 wins with three of a kind:", 
                  sort_cards(three_7(combined_hand_2)))
        
        # Checking for two pairs
        elif two_pair_7(combined_hand_1) and two_pair_7(combined_hand_2):
            print("TIE with two pairs:", two_pair_7(combined_hand_1))
        
        elif two_pair_7(combined_hand_1):
            print("Player 1 wins with two pairs:", 
                  sort_cards(two_pair_7(combined_hand_1)))
            
        elif two_pair_7(combined_hand_2):
            print("Player 2 wins with two pairs:", 
                  sort_cards(two_pair_7(combined_hand_2)))
        
        # Checking for one pair
        elif one_pair_7(combined_hand_1) and one_pair_7(combined_hand_2):
            print("TIE with one pair:", sort_cards(one_pair_7(combined_hand_1)))
        
        elif one_pair_7(combined_hand_1):
            print("Player 1 wins with one pair:", 
                  sort_cards(one_pair_7(combined_hand_1)))
            
        elif one_pair_7(combined_hand_2):
            print("Player 2 wins with one pair:", 
                  sort_cards(one_pair_7(combined_hand_2)))
        
        # Checking for High-Card
        elif sort_cards(combined_hand_1)[:-6:-1] == sort_cards(combined_hand_2)[:-6:-1]:
            print("TIE high card", sort_cards(combined_hand_1)[:-6:-1])
        
        elif sort_cards(combined_hand_1)[:-6:-1] > sort_cards(combined_hand_2)[:-6:-1]:
            print("Player 1 wins with high card", 
                  sort_cards(combined_hand_1)[:-6:-1])
        
        elif sort_cards(combined_hand_2)[:-6:-1] > sort_cards(combined_hand_1)[:-6:-1]:
            print("Player 2 wins with high card", 
                  sort_cards(combined_hand_2)[:-6:-1])
       
        # Checks if the deck has enough cards to continue playing
        if len(D) < 9:
            print("Deck has too few cards so game is done.")
            break # Quits the program
        
        # Space line for formating
        print()
       
        # Prompt the user if they want to play another hand
        user_prompt = input("Do you wish to play another hand?(Y or N) ").lower()
        if user_prompt != 'y':
            break # Quits the program

if __name__ == "__main__":
    main()