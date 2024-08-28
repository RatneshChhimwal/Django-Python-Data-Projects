import random

# Define questions, choices, and correct answers
questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "Which gas do plants absorb from the atmosphere during photosynthesis?",
    "Who wrote the play \"Romeo and Juliet\"?",
    "Who painted the Mona Lisa?",
    "What is the chemical symbol for the element gold?"
]

choices = [
    "(a) Berlin\n(b) Madrid\n(c) Rome\n(d) Paris",
    "(a) Venus\n(b) Mars\n(c) Jupiter\n(d) Saturn",
    "(a) Oxygen\n(b) Carbon dioxide\n(c) Nitrogen\n(d) Hydrogen",
    "(a) Charles Dickens\n(b) William Shakespeare\n(c) Jane Austen\n(d) Leo Tolstoy",
    "(a) Vincent van Gogh\n(b) Leonardo da Vinci\n(c) Pablo Picasso\n(d) Michelangelo",
    "(a) Go\n(b) Au\n(c) Ag\n(d) Ge"
]

answers = ["d", "c", "b", "b", "b", "b"]

# Initialize player's total winnings
winnings = 0

# Define a function to display a question and options:

def display_question(question_index):                   # The function is named 'display_question' and takes the argument 'question_index'
    print(questions[question_index])                    # To display questions based on the value of argument 'question_index'
    print(choices[question_index])                      # To display choices based on the value of argument 'question_index'

# Main game loop:

for i in range(0,len(questions)):                       # We defined a 'for' loop to iterate through the list with starting index '0' till 'Len(questions) -1'

    # 'for' loop starts with 'zero' so it stores the question at the zero index ('What is the capital of France?') and moves to 1st index once the code inside is executed

    display_question(i)         # We define function 'display_question' with 'strings(questions)' at different indexes from list 'questions' starting with index 'zero'

    # The above line 'display_question(i)' prints the question 'What is the capital of France?' as the 'print' statement is pre-defined for this function at line 29 & 30



    # Ask the player for their answer:

    player_answer = input("Enter your answer (a, b, c, or d): ").lower()  # A simple input statement, the 'lower()' method is used to convert the input into lower-case


    # Check if the player's answer is correct:

    if player_answer == answers[i]:                     # Here we have started an if loop comparing the user input with the answer at the index 'i' from 'answers' list
        print("Correct! You've won $1,000!")
        winnings += 1000                                # '1000' is incremented in the variable 'winnings'
    else:
        print("Sorry, that's incorrect. Game over.")
        break                                           # This 'break' condition closes the loop once the question is answered incorrectly



    # Check if the player has won the game (answered all questions correctly):

    if i == len(questions) - 1:                                                 # This 'if' condition checks if 'i' has reached the last index 'len(questions) - 1'
        print("\nCongratulations! You've won the game and $1,000,000!")


# Display the player's total winnings

print(f"\nTotal Winnings: ${winnings}")                                        # This 'f-string' prints the total update winnings
