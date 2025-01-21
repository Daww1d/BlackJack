import random


class PlayingCard:

    def __init__(self, given_suit, given_rank, given_value):
        self.suit = given_suit
        self.rank = given_rank
        self.value = given_value

    def giveSuit(self):
        return self.suit

class Deck:

    def __init__(self):
        self.cards = []

        # Generate a deck of cards
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = [
            "Ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
        ]
        values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        for i in range(4):
            for j in range(13):
                new_card = PlayingCard(suits[i], ranks[j], values[j])
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        for i in range(num_cards):  # do for the amount of cards wanted
            Player.give(self.cards[0])  # adds first index card to players hand
            self.cards.pop(0)  # removes the card from deck

    def show(self):
        print()

class Player:

    def __init__(self, given_name):
        self.name = given_name
        self.chips = 0
        self.hand = []
        self.value = 0

    def give(self, amount):
        for i in range(amount): #Draws cards as specified in parameter
            self.hand.append(random.choice(gameDeck.cards))

    def giveChips(self, amount):
        self.chips += amount  # adds chips to player

    def removeChips(self, amount):
        self.chips -= amount  # removes chips from player

class Dealer:

    def __init__(self):
        self.hand = []
    
    def give(self, amount):
        for i in range(amount):
            self.hand.append(random.choice(gameDeck.cards))

#=========
#functions
#=========

def hitOrStay():
    while True:#makes sure player choses hit or bet correctly
        try:
            decision = str(input("Do you want to hit or stay (h/s) : "))
        except:
            print("Invalid input")
        
        if decision == "s" or decision == "h":
            break
        else:
            print("Invalid input : must be s or h")
    

#=============
# main program
#=============

gameDeck = Deck() #create deck
gameDealer = Dealer() #create dealer


print("Welcome to my blackjack game, whats your name player?")
playerName = input("My name is , ")
gamePlayer = Player(playerName) # creates player
amount = 0
decision = None
gamePlayer.giveChips(50)
print("You start with 50 chips, each turn you get to choose the amount you wish to wager\nIf you wint you get back double your chips, if you loose you loose all your chips. ")

while True:#Loops for ever
    while True: #makes sure bet is valid
        try:
            amount = int(input("How much do you want to wager : ")) #gets a number of chips
        except:
            print("Invalid input")

        if amount > gamePlayer.chips: #occurs if player tries to wager more chips than they have
            print("You dont have enought chips") 
        else:
            break
        
    gamePlayer.removeChips(amount)# takes wagered chips from player
    print(f"You have {gamePlayer.chips} left")
    
    gameDealer.give(2)
    gamePlayer.give(2)


    hitOrStay()
    