import random

print("Welcome to the Name Guessing Game!")
randomNumber=random.randint(0,101)
guesses=0

def gameOver():
    global state
    state = False

while True:
    difficulty=input("Choose a difficult. Type 'easy' or 'hard' : ").lower()
    if difficulty=="easy":
        print("You have 10 attempts to guess the number")
        guesses = 10
        break
    elif difficulty=="hard":
        print("you have 5 attempts to guess the number")
        guesses = 5
        break
    else:
        print("Invalid Input!")

state = True
while state:
    guess=int(input('Make a guess : '))
    if guesses>1:
        if guess==randomNumber:
            print("You have made correct guess")
            gameOver()
        elif guess<randomNumber:
            print("Too low")
            guesses-=1
            print(f"You have {guesses} attempts to guess the numbers")
        elif guess>randomNumber:
            print("Too high")
            guesses-=1
            print(f"You have {guesses} attempts to guess the numbers")
    else:
        print("Out of guesses")
        gameOver()