print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')

import random

word_list = [
    "apple", "banana", "orange", "tiger", "ocean", "pizza", "chair", "table", "happy", "music",
    "diamond", "thunder", "pumpkin", "library", "fantasy", "journey", "courage", "lantern", "mystery", "rainbow",
    "chrysanthemum", "labyrinth", "phenomenon", "zephyr", "juxtaposition", "kaleidoscope", "silhouette", "fluorescent", "perplexing", "enthusiasm"
]

random_word = random.choice(word_list)
blancks = ""
lives = 6
state = False

for i in range(0, len(random_word)):
    blancks += "_"

hangmanStage = [''' 
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''  
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''  
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''  
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''  
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''  
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |''']

def hasWon(str):
    for i in str:
        if i == "_":
            return False
    return True

def check(a, str):
    guessState = False
    for i in str:
        if a == i:
            guessState = True
    return guessState

while not state:
    print(f"Word to guess: {blancks}")
    choice = input("Guess a letter: ").lower()
    if check(choice, random_word):
        print("Correct guess!")
        for i in range(0, len(random_word)):
            if choice == random_word[i]:
                blancks = blancks[:i] + random_word[i] + blancks[i+1:]
        if hasWon(blancks):
            print(f"You have won! The word was '{random_word}'.")
            state = True
    else:
        lives -= 1
        print(f"You guessed {choice}, that's not in the word. You lose a life.")
        if lives > 0:
            print(hangmanStage[5 - lives])
            print(f"****************************{lives}/6 LIVES LEFT****************************")
        else:
            print(hangmanStage[5])
            print(f"You lost all your lives. Game over! The word was '{random_word}'.")
            state = True
