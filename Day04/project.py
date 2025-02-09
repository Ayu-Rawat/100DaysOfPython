import random

computerChoice = random.randint(0,2)
lst1=["paper","rock","scissors"]
lst2 = [
    '''      
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    '''   
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

print("Welcome to Rock Paper Scissors Game")
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. : "))
print()
print(f"User chose {lst1[userChoice]}")
print(lst2[userChoice])
print(f"Computer chose {lst1[computerChoice]}")
print(lst2[computerChoice])

if userChoice == computerChoice:
    print("It's a draw")
elif userChoice == 0 and computerChoice == 1:
    print("You lose")
elif userChoice == 0 and computerChoice == 2:
    print("You win")
elif userChoice == 1 and computerChoice == 0:
    print("You win")
elif userChoice == 1 and computerChoice == 2:
    print("You lose")
elif userChoice == 2 and computerChoice == 0:
    print("You lose")
elif userChoice == 2 and computerChoice == 1:
    print("You win")
else:
    print("Invalid input")