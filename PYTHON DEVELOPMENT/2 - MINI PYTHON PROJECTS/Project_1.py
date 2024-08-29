import random

User1 = input("Enter the 1st player's name\n")
User2 = input("Enter the 2nd player's name\n")
print(f"Welcome to the game {User1} & {User2}, kindly go through the rules for the game.")
List_users = [User1, User2]

# Fix 1: Initialize a dictionary to track scores for each user.
Scores = {User1: 0, User2: 0}

def Choice():
    while True:
        choice = input("Kindly choose one of the options below.\n1. Start the game\n2. Quit the game\n")
        if choice == "1":
            print("Sure, let's get started\n")
            for user in List_users:
                turn_score = 0  # Reset turn score for each user.
                while True:
                    print(f"Rolling dice for {user}\n")
                    Dice = random.randint(1, 6)
                    print(f"You got a {Dice}")
                    
                    if Dice == 1:  # If the player rolls a 1, they lose their turn score.
                        print("Oops! You rolled a 0, your turn is over, and you score nothing this round.")
                        turn_score = 0
                        break
                    else:
                        turn_score += Dice
                        print(f"Your current turn score is {turn_score}")
                    
                    option = input("1. Roll again!!\n2. Hold!!\n")
                    if option == "1":
                        continue
                    elif option == "2":
                        print("\n")
                        print("Let's see how your opponent does\n")
                        Scores[user] += turn_score  # Add turn score to user's total score.
                        break
                    else:
                        print("Invalid choice, Kindly choose '1' or '2'")
                
                print(f"{user}'s total score is now {Scores[user]}")
            
            if Scores[User1] > Scores[User2]:
                print(f"Congratulations {User1}! You've won the game with a score of {Scores[User1]}!")
            elif Scores[User2] > Scores[User1]:
                print(f"Congratulations {User2}! You've won the game with a score of {Scores[User2]}!")
            else:
                print("It's a tie! Both players have the same score!")
            return  # Exit the game loop after announcing the winner.
        
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice, Kindly choose '1' or '2'")

Choice()
