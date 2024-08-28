import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3    # These are the number of rows in the slot window
COLS = 3    # These are the number of columns in the slot window

Symbol_Dict = {        # These are the symbols and their count in the whole wheel, As in the there are 2 "A"s and 3 "B"s and so on
    "A":3,
    "B":4,
    "C":5,
    "D":6
}

Symbol_Values = {        # These are the symbols and their multiplier values, So getting all 3 "A"s would multiply the bet by 5 times and so on
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbols, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbols)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!= len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row],end="")
        print()

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_line.append(line+1)

    return winnings, winning_line



def deposit():
    while True:
        amount = input("Enter the amount you want to deposit in numbers: \n")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than 0")
        else:
            print("Enter the correct amount")
            
    return amount

#In the slot machine game, the bet amount is determined by the number of lines the player chooses to bet on.

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" +str(MAX_LINES)+ ")?\n")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("lines should be greater than 0 and less then " +str(MAX_LINES))
        else:
            print("Enter valid number of lines")
            
    return lines

def get_bet():
    while True:
        bet = input("Enter the amount you want to bet on each line\n")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"The bet should be between {MIN_BET} and {MAX_BET}")
        else:
            print("Enter valid bet")
            
    return bet

def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You cannot bet more than your balance. Your available balance is Rs.{balance}")
        else:
            break

    # Deduct the total bet from the balance first
    balance -= total_bet

    print(f"You are betting Rs.{bet} on {lines} line(s), making your total bet Rs.{total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, Symbol_Dict)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, Symbol_Values)
    print(f"You won a total of Rs.{winnings}.")
    print(f"You won on line(s): {', '.join(map(str, winning_lines))}")

    # Update balance with net winnings
    balance += winnings

    return balance

def main():
    balance = deposit()
    while True:
        if balance <= 0:
            print("You have run out of balance. Game over!")
            break

        print(f"Current balance is Rs.{balance}")
        answer = input("Press Enter to play (or 'q' to quit): ")
        if answer.lower() == "q":
            break

        # Call spin and update balance
        balance = spin(balance)

    print(f"You left with Rs.{balance}")

main()