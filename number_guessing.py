import random


playing = input("Do you want to play? yes or no: ").strip().lower()

while playing == "yes":
    number = random.randint(1,50)
    attempts = 0
    while True:
        try:
            pick = int(input("Pick a number between 1-50: "))
            if pick < number:
                print("The number is higher! ")
                attempts += 1
            elif pick > number:
                print("The number is lower! ")
                attempts += 1
            else:
                attempts += 1
                print(f"Congratulations you won the game in {attempts} attempts! The number was {number} ")
                break
        except ValueError:
                    print("Invalid input. Please enter a number.")
    playing = input("Do you want to play? yes or no: ").strip().lower()

    


