import csv
import pandas as pd

CSV_FILE = r"D:\SKILLS\PYTHON DEVELOPMENT\PYTHON MINI PROJECTS\Quiz_Game\Quiz.csv"
user_name = input("Enter your name\n")

def name_check():
    if isinstance(user_name, str):
        print(f"\nWelcome {user_name} to this python quiz, You will be presented 10 different questions,\nAnswer them correctly")
    else:
        print("Enter correct name")

def start_or_exit():
    print("\nChoose the below option to start or quit the game")
    print("1. Start the quiz")
    print("2. Exit the game")

    choice = input("\nEnter the choice: \n")
    if choice == "1":
        print(f"Okay, let's play {user_name}\n")

        Count = 0

        # Read the CSV file
        df = pd.read_csv(CSV_FILE)

        # Loop through each question
        for index, question in enumerate(df['QUESTIONS']):
            print(question)
            answer = input("Write the correct answer below:\n")

            # To check if user's answer is equal to the actual answer (case-insensitive comparison)
            if answer.strip().lower() == df['ANSWERS'][index].strip().lower():
                print("That's correct!\n")
                Count += 1
            else:
                print("Unfortunately, that's incorrect.\n")
        
        if Count in range(0, 4):
            print(f"Your score is {Count}/10. You have got a long way to go.")
        elif Count in range(4, 8):
            print(f"Your score is {Count}/10. Try harder next time.")
        else:
            print(f"Your score is {Count}/10. That's excellent!")

    elif choice == "2":
        quit()
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        return start_or_exit()


name_check()
start_or_exit()