print('''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|''')

shouldProgramContinue = True
firstNumber=float(input("Enter the first number: "))

def claculate(n1, n2, operation):
    if operation == '+':
        print(f"{n1} + {n2} = {n1 + n2}")
        return n1 + n2
    elif operation == '-':
        print(f"{n1} - {n2} = {n1 - n2}")
        return n1 - n2
    elif operation == '*':
        print(f"{n1} * {n2} = {n1 * n2}")
        return n1 * n2
    elif operation == '/':
        print(f"{n1} / {n2} = {n1 / n2}")
        return n1 / n2
    else:
        print("Invalid operation")

while shouldProgramContinue:
    print("+\n-\n*\n/")
    operation=input("Pick an operation: ")
    nextNumber=float(input("Enter the next number: "))
    result = claculate(firstNumber, nextNumber, operation)
    choice=input(f"Do you want to continue calculation with {result} Type 'yes' or 'no': ").lower()
    if choice == 'yes':
        firstNumber = result
    elif choice == 'no':
        shouldProgramContinue = False
        print("Goodbye")
    else:
        print("Invalid input")
        shouldProgramContinue = False
        print("Goodbye")