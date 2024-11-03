import random
import time

OPERATORS = ("+", "-", "*")
MIN_OPERAND = 4
MAX_OPERAND = 12

def generate_problem(problem_count):
    problems_dict = {}
    for _ in range(problem_count):
        left = random.randint(MIN_OPERAND, MAX_OPERAND)
        right = random.randint(MIN_OPERAND, MAX_OPERAND)
        operator = random.choice(OPERATORS)
        expr = f"{left} {operator} {right}"
        answer = eval(expr)
        problems_dict[expr] = answer
    return problems_dict

def main():
    problems = generate_problem(10)
    
    input("Press enter to start!")
    print("------------------------")
    
    start_time = time.time()
    wrong = 0
    
    for i, (expr, correct_answer) in enumerate(problems.items()):
        while True:
            user_answer = input(f"Problem #{i + 1}: {expr} = ")
            try:
                if int(user_answer) == correct_answer:
                    print("\nCorrect!")
                    break
                else:
                    print("\nIncorrect!")
                    wrong += 1
            except ValueError:
                print("Please enter a valid number.")

    end_time = time.time()
    total_time = end_time - start_time
    
    print("------------------------")
    print(f"You finished in {round(total_time, 2)} seconds with {wrong} errors")

if __name__ == "__main__":
    main()
