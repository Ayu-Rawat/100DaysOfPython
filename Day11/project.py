import random

startOver = False

def resetGame():
    global computerCards
    global userCards
    global startOver
    global state
    state = False
    userCards = []
    computerCards = []

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
userCards = []
computerCards = []

state = False

def gameOver():
    global state
    state = False
    print(f"Your cards {userCards} which adds up to {sum(userCards)}")
    print("Your score went over 21, you lose!")
    resetGame()

while not startOver:
    choice = input("Do you want to play a game of cards? Type 'yes' or 'no': ").lower()
    if choice == 'yes':
        userCards.append(random.choice(cards))
        userCards.append(random.choice(cards))
        computerCards.append(random.choice(cards))
        computerCards.append(random.choice(cards))
        state = True
        while state:
            print(f"Your cards {userCards} which adds up to {sum(userCards)}")
            print(f"Computer first card is {computerCards[0]}")
            choice = input("Do you wish to draw another card Y / N ").lower()
            if choice == 'y':
                userCards.append(random.choice(cards))
                if sum(userCards) > 21:
                    gameOver()
            else:
                print(f"Your cards {userCards} which adds up to {sum(userCards)}")
                print(f"Computer cards {computerCards} which adds up to {sum(computerCards)}")
                if sum(userCards) > sum(computerCards):
                    print("You win")
                    resetGame()
                elif sum(userCards) == sum(computerCards):
                    print('It\'s a tie')
                    resetGame()
                else:
                    print("Computer wins")
                    resetGame()
    else:
        startOver=True
