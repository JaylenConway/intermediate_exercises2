class BankAccount:
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdrawl(self, amount):
        self.balance -= amount

    def get_balance(self):
        return f'{self.account_name} has a balnce of {self.balance}'
        