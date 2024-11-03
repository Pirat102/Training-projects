import random
COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGHT = 4

def generate_code():
    code = []
    
    for _ in range(CODE_LENGHT):
        code.append(random.choice(COLORS))
        
    print(code)
    return code

def guess_code():
    print(f"Avaible colors: {COLORS}")
    
    while True:
        
        guess = input("Guess: ").upper().split(" ")
        
        if len(guess) != CODE_LENGHT:
            print(f"You must guess {CODE_LENGHT} colors")
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try Again.")
                break
        else:
            break
        
    return guess
        
def check_code(real_code, guess):
    print(real_code, guess)


check_code(generate_code(), guess_code())