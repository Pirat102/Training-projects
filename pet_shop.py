animals = {
    "cat" : 150, "fish" : 30, "parrot" : 100, "rabbit" : 150, "hamster" : 50, "hare" : 150, "guinea pig" : 150, "snake" : 300, "turtle" : 150
}

            
inventory = []

def buy(budget):
    while True:

        buy = input("What animal would you like to buy?: ").strip().lower()

        if buy in animals and budget >= animals[buy]:
            inventory.append(buy)
            budget -= animals[buy]
            print("Congratulations on your purchase!")
            answer = input("Do you want to continue shooping? yes/no: ").strip().lower()
            if answer == "yes":
                continue
            else:
                return budget
        elif buy in animals and budget < animals[buy]:
            print("You don't have enough money to buy this animal")
            answer = input("Do you want to continue shooping? yes/no: ").strip().lower()
            if answer == "yes":
                continue
            else:
                return budget
        else:
            print("We don't have this animal in stock.")






def shopping():
    for animal, price in animals.items():
        print(f"Animal: {animal} - ${price}")




def main():
    print("Welcome to our shop! What are you up to today?\n",
            "1. Display animals list\n", 
            "2. Buy an animal\n",
            "3. Check your bank account\n",
            "4. Display my pets\n",
            "5. Leave the shop\n")
    budget = 500
    
    while True:

        try:
            action = int(input("Choose your action (1-5): "))
            if action == 1:
                shopping()
            if action == 2:
                budget = buy(budget)
            if action == 3:
                print(f"You current budget is: ${budget}")
            if action == 4:
                print(f"Your pets: {inventory}" if inventory else "You have no pets yet.")
            if action == 5 :
                print("Thank you for visiting our shop")
                break
            else:
                print("Please choose a valid option between 1 and 5.")
        except ValueError:
            print("Wrong input, choose a number! ")
        

    


main()

