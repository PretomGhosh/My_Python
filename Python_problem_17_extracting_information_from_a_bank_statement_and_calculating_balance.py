deposit = []
withdrawal = []
transactions = [] # Taken 3 empty lists
print("Enter your transaction details here. Press Enter on an empty line to finish. ") #Prompt for entering the transaction details
while True:
    transaction = input()
    if not transaction:
        break
    transactions.append(transaction)
for items in transactions:
    items = items.split() #Splitted the items in the transactions list
    if len(items) == 2 and items[0].isalpha() and items[1].isdigit(): #Checked if the item contains both letters and amounts
            char = items[0]
            number = int(items[1]) #Created variables for the letters and amounts
            if char == 'D':
                 deposit.append(number) #If character represents Deposit adding the corresponding amount in the deposit list
            elif char == 'W':
                 withdrawal.append(number) #If character represents withdrawal adding the corresponding amount in the deposit list
            else:
                 continue
balance = sum(deposit)-sum(withdrawal) #Calculated balance by applying formula
print(f'The current balance is ${balance}')