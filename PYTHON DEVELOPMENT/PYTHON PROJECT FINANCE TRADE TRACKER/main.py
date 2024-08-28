import pandas as pd
import csv
from datetime import datetime
from data_entry import *
import matplotlib.pyplot as plt

class CSV():
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["Date","Amount","Category","Description"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)


    @classmethod
    def new_entry(cls, Date, Amount, Category, Description):
        new_entry = {
            "Date":Date,
            "Amount":Amount,
            "Category":Category,
            "Description":Description
        }

        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("entry added successfully")


    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        if df.empty:
            print("No transactions found in the file.")
            return df
        else:
            df["Date"] = pd.to_datetime(df["Date"], format=date_format)
            start_date = datetime.strptime(start_date, date_format)
            end_date = datetime.strptime(end_date, date_format)

            mask = (df["Date"]>= start_date) & (df["Date"]<= end_date)
            filtered_df = df.loc[mask]
            
            if filtered_df.empty:
                print("No transactions found in the given date range")
            else:
                print(f"Transactions from {start_date.strftime(date_format)} to {end_date.strftime(date_format)}")
                print(filtered_df.to_string(index=False, formatters={"Date": lambda x: x.strftime(date_format)}))

                total_income = filtered_df[filtered_df["Category"]== "Income"]["Amount"].sum()
                total_expense = filtered_df[filtered_df["Category"]== "Expense"]["Amount"].sum()
                print("\nSummary:")
                print(f"Total Income : {total_income:.2f}")
                print(f"Total Expense : {total_expense:.2f}")
                print(f"Net Savings: {(total_income-total_expense):.2f}")

            return filtered_df
    


def add_entry():
    CSV.initialize_csv()
    Date = get_date("Enter the date of the transaction or press 'Enter' for today's date: ", allow_default=True)
    Amount = get_amount()
    Category = get_category()
    Description = get_description()

    CSV.new_entry(Date, Amount, Category, Description)



def plot_transactions(df):
    df.set_index('Date', inplace=True)

    income_df = df[df["Category"]=="Income"].resample("D").sum().reindex(df.index, fill_value=0)
    expense_df = df[df["Category"]=="Expense"].resample("D").sum().reindex(df.index, fill_value=0)

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["Amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["Amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expense over time")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("\n1. Add new transaction entry")
        print("2. Get transactions & Summary within date range")
        print("3. EXIT")

        choice = input("Enter the option number (1-3): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot? (y/n) ").lower() == "y":
                plot_transactions(df)
            else:
                break
        elif choice == "3":
            print("Exiting the program ...")
            break
        else:
            print("Invalid option number, kindly choose between 1,2 or 3.")

if __name__ == "__main__":
    main()
    