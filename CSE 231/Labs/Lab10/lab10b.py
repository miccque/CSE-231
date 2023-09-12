import cards

class Battle(object):
    def __init__(self, current1 ='', current2 =''):
        self.current1 = current1
        self.current2 = current2
    
    def get_rank(self):
        if self.current1.rank() == 1:
            self.rank1 = 14
        else:
            self.rank1 = self.current1.rank()
        if self.current2.rank() == 1:
            self.rank2 = 14
        else:
            self.rank2 = self.current2.rank()
            
    def fight(self):    
        if self.rank1 > self.rank2:
            hand1_list.extend([self.current1, self.current2])
            print("Battle was 1: {}, 2: {}. Player 1 wins battle.".format(self.current1, self.current2))
        elif self.rank2 > self.rank1:
            hand2_list.extend([self.current2, self.current1])
            print("Battle was 1: {}, 2: {}. Player 2 wins battle.".format(self.current1, self.current2))
        else:
            hand1_list.append(self.current1)
            hand2_list.append(self.current2)
            print("Battle was 1: {}, 2: {}. Battle was a draw.".format(self.current1, self.current2))        

# Create the deck of cards

the_deck = cards.Deck()
# the_deck.shuffle()

hand1_list=[]
hand2_list=[]
for i in range( 5 ):
    hand1_list.append( the_deck.deal() )
    hand2_list.append( the_deck.deal() )

print("Starting Hands")
print("Hand1:", hand1_list)
print("Hand2:", hand2_list)
print()

current1 = hand1_list.pop(0)
current2 = hand2_list.pop(0)
battle = Battle(current1,current2)
battle.get_rank()
battle.fight()

print("hand1:", hand1_list)
print("hand2:", hand2_list)

user_input = input("\nKeep Going: (Nn) to stop:").lower() 
while user_input != 'n':
    current1 = hand1_list.pop(0)
    current2 = hand2_list.pop(0)
    battle = Battle(current1,current2)
    battle.get_rank()
    battle.fight()
    print("hand1:", hand1_list)
    print("hand2:", hand2_list)
    if len(hand1_list) == 0 or len(hand2_list) == 0:
        break
    user_input = input("\nKeep Going: (Nn) to stop:").lower()         

if len(hand1_list) > len(hand2_list):
    print("Player 1 wins!!!")
if len(hand2_list) > len(hand1_list):
    print("Player 2 wins!!!")



