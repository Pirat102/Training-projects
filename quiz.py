import random

questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".py", ".pt", ".pyt", ".python"],
        "correct": 0  # Indeks poprawnej odpowiedzi
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "lambda", "define"],
        "correct": 1
    },
    {
        "question": "What is the output of the following code: print(2 ** 3)?",
        "options": ["5", "6", "8", "9"],
        "correct": 2  # 2 ** 3 = 8
    },
    {
        "question": "Which of the following data types is **immutable** in Python?",
        "options": ["list", "dictionary", "set", "tuple"],
        "correct": 3  # Tuple is immutable
    },
    {
        "question": "What is the correct way to start a **for loop** in Python?",
        "options": ["for i in range(5)", "for (i=0; i<5; i++)", "foreach i in range(5)", "loop i over range(5)"],
        "correct": 0  # Correct syntax is "for i in range(5)"
    }
]

def asking_questions():
    score = 0
    playing = True
    while playing:
        # Losowanie pytań
        shuffled_questions = questions[:]
        random.shuffle(shuffled_questions)
        
        for question in shuffled_questions:
            print(question["question"])
            for i, option in enumerate(question["options"]):
                print(f"{i + 1}. {option}")
            
            while True:
                try:
                    answer = int(input("Choose one answer (1-4): ")) - 1
                    if 0 <= answer < len(question["options"]):
                        if answer == question["correct"]:
                            print("Great answer!")
                            score += 1
                        else:
                            print("Wrong answer!")
                        break
                    else:
                        print("Invalid option. Please choose a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        print(f"Your score is {score} / {len(questions)}")
        
        # Opcjonalnie: pytaj, czy użytkownik chce kontynuować
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            playing = False

asking_questions()
