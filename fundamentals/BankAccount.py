class BankAccount: 
    accounts = []
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        # self.account = BankAccount(interest_rate=0.02, balance=0)
        BankAccount.accounts.append(self)

    def deposit(self,amount):
        self.balance = amount
        return self

    def withdrawal(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        f"{self.balance}"
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self


    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:


    def __init__(self, name):
        self.name = name
        self.account = {
            "savings" : BankAccount(.05,1000),
            "checking" : BankAccount(.02,5000)
    }

def display_user_balance(self):
    print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
    print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
    return self

def transfer_money(self, amount, user):
    self.amount -= amount
    user.amount += amount
    self.display_user_balance()
    user.display_user_balance()
    return self 

abdul = User("Abdul")

abdul.account['checking'].deposit(100)
abdul.display_user_balance()