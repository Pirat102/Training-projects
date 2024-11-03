transaction_history = []

def add_funds(balance):
    try: 
        money = float(input("How much you want to deposit?: $"))
        balance += money
        transaction_history.append({"income":money})
    except: print("Please select a correct amount")
    return balance



def spend_funds(balance):
    try:
        money = float(input("How much you want to spend?: $"))
        if balance >= money:
            balance -= money
            transaction_history.append({"outcome":money})
        else: print("You balance is too low!")
    except: print("Please select a correct amount")
    return balance

def check_acc(balance):
    print(f"Your balance is: ${balance:.2f}")

def check_history(transaction_history):
    print(f"Your transaction history: {transaction_history}")

def main_menu():
    

    balance = 0
    while True:
        print("1. Add funds")
        print("2. Spend funds")
        print("3. Check acc")
        print("4. Check transaction history")
        print("5. Leave for now")
        
        try: 
            decision = int(input("Choose an option (1:5): "))
            if decision == 1:
                balance = add_funds(balance)
            elif decision ==2:
                balance = spend_funds(balance)
            elif decision ==3:
                check_acc(balance)
            elif decision ==4:
                check_history(transaction_history)
            elif decision ==5:
                print("Thank you for using our service!")
                break
        except: print("Please choose a correct number.")



main_menu()