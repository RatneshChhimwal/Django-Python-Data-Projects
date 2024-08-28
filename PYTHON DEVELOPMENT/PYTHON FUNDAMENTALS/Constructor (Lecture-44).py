# IMPORTANT TOPIC ******************************************************************************************************

# CONSTRUCTORS

"""
Imagine you are building a banking application. You have a BankAccount class to represent bank accounts. A BankAccount should have the following attributes:

account_number
account_holder
balance

Here's why constructors are valuable in this context:

Initialization: When a BankAccount object is created, it should have an account number, an account holder's name, and an initial balance.
A constructor allows you to set these initial values when the object is instantiated.
Without a constructor, you'd need to set these attributes individually after creating the object.

Consistency: With constructors, you ensure that all BankAccount objects are created with the required attributes,
reducing the chance of missing any crucial information.
This helps maintain the consistency of object states.

"""

# Below is an example using a constructor:

class BankAccount:                                                                  # We created a class 'BankAccount'
    def __init__(self, account_number, account_holder, initial_balance):            # We created a constructor method with takes 4 arguments including 'self'
        self.account_number = account_number                                        # We defined an attribute 'account_number' which is needed during object creation
        self.account_holder = account_holder                                        # We defined an attribute 'account_holder' which is needed during object creation
        self.balance = initial_balance                                              # We defined an attribute 'initial balance' which is needed during object creation

"""
The line 'self.balance = initial_balance' initializes the balance attribute of the object with the 'initial_balance' parameter.
The 'initial_balance' parameter is the initial amount of money in the account when the object is created.
The attribute 'self.balance' will keep track of the account's balance as transactions are made.
"""

# initial_balance will be defined during object creation (Say '1000'), while 'self.balance' will be used to perform further actions with the 'initial_balance'

    def deposit(self, amount):                        # We create a function 'deposit' which takes 2 parameters including self
        self.balance += amount                        # When function 'deposit' is called with any int amount as argument, It will be added to 'self.balance'

    def withdraw(self, amount):                       # We create a function 'withdraw' which takes 2 parameters including self
        if self.balance >= amount:                    # An 'if-else' loop, Here 'if' the self.balance is '>=' then the argument 'amount' then,
            self.balance -= amount                    # Argument 'amount' will be deducted from 'self.balance' which is 'initial_balance' passed during object creation
        else:
            print("Insufficient balance")             # 'else' condition



# Create a BankAccount object with a constructor ---------


account = BankAccount("12345", "Alice", 1000)            # Example object creation with defined 3 attributes & their values


# Perform transactions ----------

account.deposit(500)                                    # Example function 'deposit' called for object 'amount'
account.withdraw(200)                                   # Example function 'withdraw' called for object 'amount'



""" Using constructors in this case ensures that every BankAccount object is created with all required attributes,
and the code becomes more organized and readable.
It's especially valuable in larger programs where numerous attributes need proper initialization. """



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# EXPLAINING THE 'deposit' AND 'withdraw' FUNCTIONS INSIDE THE ABOVE CODE BELOW:

""" 
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")
            
"""

# In the part of the code above, there are two methods defined within the BankAccount class: deposit and withdraw.

""" 

1 --- deposit(self, amount): This method allows you to deposit a certain amount of money into the bank account. Here's how it works:

self - is a reference to the instance of the class (the specific bank account object on which this method is called).
amount - is a parameter that represents the amount of money you want to deposit into the account.

Inside the method:

self.balance += amount: This line adds the amount to the current balance of the bank account.
It updates the account's balance by increasing it with the deposited amount.


2 ---- withdraw(self, amount): This method allows you to withdraw a certain amount of money from the bank account. Here's how it works:

self is again a reference to the instance of the class.
amount is the parameter representing the amount of money you want to withdraw.
Inside the method:

if self.balance >= amount:: This line checks whether the current balance (self.balance) is greater than or equal to the withdrawal amount.
If there's enough money in the account to cover the withdrawal, the code proceeds with the next line.

self.balance -= amount: If there's enough money in the account, this line subtracts the amount from the current balance.
It updates the account's balance by reducing it by the withdrawn amount.

else:: If there's insufficient balance to cover the withdrawal, this part of the code is executed.

print("Insufficient balance"): This line prints a message indicating that the withdrawal is not possible due to insufficient funds.

These methods help manage the balance of the BankAccount object by allowing deposits and withdrawals
while ensuring the account's balance is updated correctly and that insufficient balance situations are handled.

"""




