import random

print("Welcome to the password generator")
noOfLetters=int(input("How many letters would you like in password : "))
noOfSymbols=int(input("How many symbols would you like : "))
noOfNumbers=int(input("How many numbers would you like : "))
letters="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
numbers="1234567890"
symbols="@_$#"
selectedCharacter=[]
password=""

for i in range(0,noOfLetters):
    selectedCharacter.append(random.choice(letters))
for i in range(0,noOfSymbols):
    selectedCharacter.append(random.choice(symbols))
for i in range(0,noOfNumbers):
    selectedCharacter.append(random.choice(numbers))

random.shuffle(selectedCharacter)
print("Genrated password is: ",end="")
for i in selectedCharacter:
    print(i,end="")