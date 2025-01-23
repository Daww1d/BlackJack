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
        self.numCards = len(self.hand)
        self.bust = False

    def give(self, amount):
        for i in range(amount):  # Draws cards as specified in parameter
            self.hand.append(random.choice(gameDeck.cards))

    def giveChips(self, amount):
        self.chips += amount  # adds chips to player

    def removeChips(self, amount):
        self.chips -= amount  # removes chips from player

    def handValue(self):
        tempVal = 0
        for card in self.hand:
            tempVal += card.value
        self.value = tempVal
        if self.value > 21:
            self.bust = True

    def countCards(self):
        self.numCards = len(self.hand)

    def emptyHand(self):
        for card in self.hand:
            gameDeck.cards.append(card)
        self.hand = []


class Dealer:

    def __init__(self):
        self.hand = []
        self.value = 0
        self.numCards = len(self.hand)
        self.bust = False

    def give(self, amount):
        for i in range(amount):
            self.hand.append(random.choice(gameDeck.cards))

    def handValue(self):
        tempVal = 0
        for card in self.hand:
            tempVal += card.value
        self.value = tempVal
        if self.value > 21:
            self.bust = True

    def countCards(self):
        self.numCards = len(self.hand)

    def emptyHand(self):
        for card in self.hand:
            gameDeck.cards.append(card)
        self.hand = []


# =========
# functions
# =========


def ask():
    while True:  # makes sure player choses hit or bet correctly
        try:
            decision = str(input("Do you want to hit or stay (h/s) : "))
        except:
            print("Invalid input")

        if decision == "s" or decision == "h":
            return decision
            break
        else:
            print("Invalid input : must be s or h")


def deal(playerAmount=0, dealerAmount=0):
    gameDealer.give(dealerAmount)
    gamePlayer.give(playerAmount)


def winCalc():
    gamePlayer.handValue()
    gameDealer.handValue()

    updateValues()

    if (gamePlayer.value > gameDealer.value) and (gamePlayer.bust == False):
        gamePlayer.giveChips(amount * 2)
        print(f"Player wins {amount * 2} chips! You now have {gamePlayer.chips} chips")
    elif (gamePlayer.value < gameDealer.value) and (gameDealer.bust == False):
        print(f"Dealer wins, you lose. You now how {gamePlayer.chips}")
    elif gamePlayer.value == gameDealer.value:
        gamePlayer.giveChips(amount)
        print(
            f"You draw , you get your wagered chips back. You have {gamePlayer.chips} chips"
        )


def dealerTurn():
    while gameDealer.value < 17:
        deal(0, 1)
        gameDealer.handValue()
        gameDealer.countCards()
        print(
            f"The dealer draws a {gameDealer.hand[gameDealer.numCards-1].rank} of {gameDealer.hand[gameDealer.numCards-1].suit}. The total value of their hand is {gameDealer.value}"
        )


def cleanHands():
    gameDealer.emptyHand()
    gamePlayer.emptyHand()


def updateValues():
    gamePlayer.handValue()
    gameDealer.handValue()
    gamePlayer.countCards()
    gameDealer.countCards()


# =============
# main program
# =============

gameDeck = Deck()  # create deck
gameDealer = Dealer()  # create dealer


print("Welcome to my blackjack game, whats your name player?")
while True:  # makes sure bet is valid
    try:
        playerName = str(input("My name is , "))  # gets a number of chips
    except:
        print("Invalid input")
    break

gamePlayer = Player(playerName)  # creates player
amount = 0
decision = None
gamePlayer.giveChips(50)
print(
    "You start with 50 chips, each turn you get to choose the amount you wish to wager\nIf you win you get back double your chips, if you loose you loose all your chips."
)

while True:  # Loops for ever
    while True:  # makes sure bet is valid
        try:
            amount = int(
                input("\nHow much do you want to wager : ")
            )  # gets a number of chips
        except:
            print("Invalid input")

        if (amount > gamePlayer.chips) or (
            amount < 0
        ):  # occurs if player tries to wager more chips than they have or negative
            print("You cant bet that amount of chips")
        else:
            break

    gamePlayer.removeChips(amount)  # takes wagered chips from player
    print(f"You have {gamePlayer.chips} left\n")

    deal(2, 1)

    updateValues()

    print(
        f"Your hand is , {gamePlayer.hand[0].rank} of {gamePlayer.hand[0].suit} and {gamePlayer.hand[1].rank} of {gamePlayer.hand[1].suit}. The value of your hand is {gamePlayer.value}"
    )
    print(
        f"The dealers card is , {gameDealer.hand[0].rank} of {gameDealer.hand[0].suit}. The value of their hand is {gameDealer.value} "
    )

    playerChoice = ask()

    while (playerChoice != "s") and (gamePlayer.bust == False):
        deal(1)
        gamePlayer.countCards()
        gamePlayer.handValue()
        print(
            f"Your draw a {gamePlayer.hand[gamePlayer.numCards - 1].rank} of {gamePlayer.hand[gamePlayer.numCards - 1].suit}.The value of your hand is {gamePlayer.value} "
        )
        playerChoice = ask()

    dealerTurn()  # draws dealers cards

    winCalc()  # Checks who won and gives rewards

    cleanHands()  # removes cards from player and dealer and puts them back into deck

    updateValues()  # updates attributes of dealers and players card count and handworth
