print("Welcome to the tip calculator!")
billAmount=float(input("What was the total bill? : "))
tipPercentage=float(input("What percentage tip would you like to give? 10, 12, or 15? : "))
people=float(input("How many people to split the bill? : "))
totalBill = billAmount + (billAmount * tipPercentage / 100)
amountPerPerson = totalBill / people
print(f"Each person should pay : {amountPerPerson}")