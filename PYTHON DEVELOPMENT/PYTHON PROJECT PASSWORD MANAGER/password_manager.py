import csv
import pandas as pd

user = input("Enter the username\n")
password = input("Enter password\n")

Store_password_list = []
encrypted_password_list = []

CSV_file = "Details.csv"
COLUMNS = ['Users','Passwords']

def saving_password():
    for character in password:
        Store_password_list.append(character)


def encrypt():
    for character in password:
        if character.isnumeric():
            character = int(character)+2
            encrypted_password_list.append("-"+str(character))
        elif character.isalpha():
            character= chr(ord(character)+1)
            encrypted_password_list.append(str(character))
        else:
            character = "*"
            encrypted_password_list.append(str(character))
        encrypted_password = ''.join(encrypted_password_list)
    print(encrypted_password)


def save_csv():
    try:
        df = pd.read_csv(CSV_file)
    except FileNotFoundError:
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(CSV_file, index=False)

    # Prepare data to be appended
    encrypted_password = ''.join(encrypted_password_list)
    new_data = pd.DataFrame([[user, encrypted_password]], columns=COLUMNS)

    # Append new data to the data-frame
    df = pd.concat([df, new_data], ignore_index=True)
    
    # Save the updated data-frame back to the CSV file
    df.to_csv(CSV_file, index=False)


def main():
    saving_password()
    encrypt()
    save_csv()

main()