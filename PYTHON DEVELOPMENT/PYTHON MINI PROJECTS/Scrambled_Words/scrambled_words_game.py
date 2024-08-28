from words_dictionary import *

user_name = input("Enter your name\n")

def name_check():
    if isinstance(user_name, str):
        print(f"\nWelcome {user_name} to this python game, You will be presented different scrambled words,\nUnscramble them correctly")
    else:
        print("Enter correct name")

def start_or_exit():
    print("\nChoose the below option to start or quit the game")
    print("1. Start the game")
    print("2. Exit the game")

    choice = input("\nEnter the choice: \n")
    if choice == "1":
        print(f"Okay, let's play {user_name}\n")
    
        for scrambled_key, scrambled_value in scrambled_words.items():
            max_chances = 3  # Reset max chances for each new word
            while max_chances > 0:
                print(f"The scrambled word is: {scrambled_key}\n")
                answer = input("Enter the above word unscrambled: ")
                
                if answer.lower() == scrambled_value.lower():
                    print("That's correct! Well done!\n")
                    break  # Move to the next word if the answer is correct
                else:
                    max_chances -= 1
                    if max_chances > 0:
                        print(f"That's incorrect. You have {max_chances} {'chance' if max_chances == 1 else 'chances'} left. Try again!")
                    else:
                        print(f"Sorry, no more tries left. The correct answer was '{scrambled_value}'.\n")
                    
    elif choice == "2":
        quit()
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        return start_or_exit()

name_check()
start_or_exit()
