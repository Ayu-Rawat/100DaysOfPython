print("Welcome to the secret auction program.")
continueTheProgram = "yes"
d = {}

while continueTheProgram == "yes":
    name = input("Enter the name of bidder: ")
    bidAmt = float(input("Enter the bid: "))
    d[name] = bidAmt
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    
    if choice == "yes":
        continue
    elif choice == "no":
        continueTheProgram = "no"
        highestBid = max(d.values())
        winner = [name for name, bid in d.items() if bid == highestBid][0]
        print(f"The bid winner is {winner} with a bid amount of {highestBid}")
    else:
        print("Invalid input")
        break
