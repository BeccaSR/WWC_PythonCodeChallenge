# Day 60 Challenge:
# Create a class representing a simple bank account with deposit and withdraw methods.

class bank_account:

    def __init__(self, balance):
        '''
        Argument is starting balance of account.
        Initialises account with starting balance.
        '''
        self.balance =balance
        
    def get_balance(self):
        '''
        Does not take an argument.
        Returns current balance of account.
        '''
        print(f'Your balance is £{self.balance}')

    def deposit(self, amount):
        '''
        Argument is amount to deposit.
        Returns new balance.
        '''
        self.balance += amount
        print(f'Your new balance is £{self.balance}')
    
    def withdraw(self, amount):
        '''
        Argument is amount to withdraw.
        If amount to withdraw is greater than the current balance,
        the user is advised of insufficient funds.
        Otherwise, amount is withdrawn and new balance is returned.
        '''
        if amount > self.balance:
            print(f'Insufficient funds. Your balance is £{self.balance}')
        else:
            self.balance -= amount
            print(f'Your new balance is £{self.balance}')

# initialise account, with starting balance
account1 = bank_account(500)

# deposit £60
print('\nDeposit £60:')
account1.deposit(60)

# withdraw £200
print('\nWithdraw £200:')
account1.withdraw(200)

# withdraw £400
print('\nWithdraw £400:')
account1.withdraw(400)

# check balance
print('\nCheck balance:')
account1.get_balance()