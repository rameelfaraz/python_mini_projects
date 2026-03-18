def ask_question(character, question, answer):
    print()
    print("=" * 40)
    print(f"{character}: {question}")
    print("=" * 40)
    while True:
        user_answer = input("\nYour answer: ").strip().lower()
        if not user_answer:
            print(f"{character}: Input cannot be empty. Please enter your answer.")
            continue
        correct = answer.strip().lower()
        # Use difflib for better fuzzy matching
        import difflib
        similarity = difflib.SequenceMatcher(None, user_answer, correct).ratio()
        return similarity > 0.8

def quiz_game():
    easy_questions = [
        ("Which Wes Anderson film features a hotel concierge named Gustave H?", "The Grand Budapest Hotel"),
        ("Who plays the character Mr. Fox in 'Fantastic Mr. Fox'?", "George Clooney"),
        ("Which film features a boy named Sam and a girl named Suzy running away together?", "Moonrise Kingdom"),
        ("Who plays the narrator in 'The French Dispatch'?", "Anjelica Huston"),
        ("Which Wes Anderson film is about a fox stealing chickens?", "Fantastic Mr. Fox")
    ]

    medium_questions = [
        ("In which movie does a family of gifted children live in a New York City house?", "The Royal Tenenbaums"),
        ("Which Wes Anderson film is set on a train traveling across India?", "The Darjeeling Limited"),
        ("Who plays Steve Zissou in 'The Life Aquatic with Steve Zissou'?", "Bill Murray"),
        ("Which film features a character named Margot Tenenbaum?", "The Royal Tenenbaums"),
        ("Which Wes Anderson film is set in the fictional town of Ennui-sur-Blasé?", "The French Dispatch")
    ]

    hard_questions = [
        ("What is the name of the scout camp in 'Moonrise Kingdom'?", "Camp Ivanhoe"),
        ("Who plays the character Agatha in 'The Grand Budapest Hotel'?", "Saoirse Ronan"),
        ("What is the profession of M. Gustave in 'The Grand Budapest Hotel'?", "Concierge"),
        ("Which Wes Anderson film features a stop-motion animated dog pack?", "Isle of Dogs"),
        ("Which film features a prison escape and a bakery?", "The Grand Budapest Hotel")
    ]

    questions_dict = {
        "easy": easy_questions,
        "medium": medium_questions,
        "hard": hard_questions
    }

    character = "Monsieur Gustave"
    valid_levels = ["easy", "medium", "hard"]

    while True:
        print()
        print("*" * 50)
        print(f"{character}: Welcome to my Wes Anderson movie quiz!")
        print("*" * 50)
        print()
        print(f"{character}: Please select a difficulty level:")
        print("-" * 30)
        print("  Easy\n  Medium\n  Hard")
        print("-" * 30)
        while True:
            difficulty = input("Your choice: ").strip().lower()
            if not difficulty:
                print(f"{character}: Input cannot be empty. Please enter a difficulty level.")
                continue
            if difficulty not in valid_levels:
                print(f"{character}: Invalid choice. Please select from easy, medium, or hard.")
                continue
            break

        selected_questions = questions_dict[difficulty]
        score = 0
        print()
        print("=" * 40)
        print(f"{character}: Let's begin with {difficulty.capitalize()} questions!")
        print("=" * 40)
        print()
        for question_number, (q, a) in enumerate(selected_questions, 1):
            print()
            print(f"Question {question_number} of {len(selected_questions)}:")
            if ask_question(character, q, a):
                print()
                print("-" * 40)
                print(f"{character}: Correct! Well done.")
                print("-" * 40)
                score += 1
            else:
                print()
                print("-" * 40)
                print(f"{character}: Wrong! The correct answer was: {a}")
                print("-" * 40)
        print()
        print("*" * 50)
        print(f"{character}: Your score is {score} / {len(selected_questions)}.")
        print("*" * 50)
        print()
        # Bonus: Result message
        if score == len(selected_questions):
            print(f"{character}: Incredible! You are a true Wes Anderson expert!")
        elif score > len(selected_questions) // 2:
            print(f"{character}: Good job! You know your Wes Anderson movies.")
        else:
            print(f"{character}: Keep practicing! Maybe next time you'll impress me.")
        print()
        print("=" * 40)
        while True:
            play_again = input(f"{character}: Would you like to play again? (yes/no): ").strip().lower()
            if not play_again:
                print(f"{character}: Input cannot be empty. Please enter yes or no.")
                continue
            if play_again not in ["yes", "no"]:
                print(f"{character}: Invalid input. Please enter yes or no.")
                continue
            break
        if play_again != "yes":
            print(f"{character}: Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    quiz_game()
