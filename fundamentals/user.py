
class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0 

    def make_deposits(self, amount):
        self.amount += amount 
        return self

    def make_withdrawal(self, amount):
        self.amount -= amount 
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


abdul = User("Abdul")
joestar = User("Joestar")
Danny = User("Danny")

abdul.make_deposits(1100520).make_deposits(500245).make_deposits(200301).make_withdrawal(405542).display_user_balance()

joestar.make_deposits(452368).make_deposits(3245).make_withdrawal(10546).make_withdrawal(23589).display_user_balance()

Danny.make_deposits(2103456).make_withdrawal(32568).make_withdrawal(45895).make_withdrawal(102365).display_user_balance()

abdul.transfer_money(200000, Danny)
