import random

"""
"Rock, Paper, and Scissors is a children's game
where players use hand gestures to represent rock, paper, or scissors.
Rock beats scissors, scissors beat paper, and paper beats rock.
Write a Python program to create a Rock, Paper, Scissors game in Python using if-else statements.
Do not create any fancy GUI. Use proper functions to check for a win."
"""

# HINT: 2-dimensional list

#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FIRST APPROACH:

"""
We can either write this with 
1- we take input from user, with options 'Rock, Paper and Scissor'
2- we randomly generate an option using 'random' method with list containing [Rock, Paper, and Scissor]
3- we write if-elif-else conditions for all combinations
"""

# SECOND APPROACH (As per the hint from harry)

"""
We have a 2-dimensional list, Almost a matrix with combinations as below:
Row- Player's choice
Column- Computer's choice

We have 3 options (Rock, Paper and Scissor) for both player and computer
So the matrix will be somewhat as below:

            R   P   S
        R   D   L   W
        P   W   D   L
        S   L   W   D
        
Here we have different outcomes to different combinations of player and computer choices at different indexes

Listing the indexes down:

Suppose this 2D-list in assigned to a variable named 'Combinations', So:

***** IMPORTANT: KEEP IN MIND THE WIN-LOSE IS TO BE DISPLAYED FOR THE PLAYER'S (USER'S) PERSPECTIVE *****

Combinations[0][0] = Rock-Rock = Draw for player
Combinations[0][1] = Rock-Papers = Lose for player
Combinations[0][2] = Rock-Scissor = Win for player
Combinations[1][0] = Paper-Rock = Win for player
Combinations[1][1] = Paper-Paper = Draw for player
Combinations[1][2] = Paper-Scissor = Lose for player
Combinations[2][0] = Scissor-Rock = Lose for player
Combinations[2][1] = Scissor-Paper = Win for player
Combinations[2][2] = Scissor-Scissor = Draw for player

Now, We can assign either write the full strings 'Draw', 'Win' & 'Lose' inside the 2D list 'Combinations', or
We can create the list with '-1','0' & '1' to simplify and later define the values as '-1' for lose, '0' for draw & '1' for win

"""

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Let's start with 2nd approach:

Options = ['Rock', 'Paper', 'Scissor']
inpt= input(f"Choose any of the options below\n{Options}:\n")

Result_mapping={0:'Draw', -1:'Lose', 1:'Win'}
Option_mapping={0:'Rock',1:'Paper',2:'Scissor'}

Combinations = [[0,-1,1]
                ,[1,0,-1],
                [-1,1,0]]



Cominpt = random.choice(Options)

if Cominpt=='Rock':
    Cominpt_int=0
elif Cominpt=='Paper':
    Cominpt_int=1
else:
    Cominpt_int = -1

if inpt=='Rock':
    inpt_int=0
elif inpt=='Paper':
    inpt_int=1
else:
    inpt_int = -1

print(Cominpt)

Result_inpt = Combinations[inpt_int][Cominpt_int]     # If 'inpt_int' is '-1' (user input is scissor), then 'Combinations[-1][Cominpt_int]' will be computed as 'Combinations[len(Combinations)-1][Cominpt_int]'
Result_final = Result_mapping[Result_inpt]

print(Result_final)

