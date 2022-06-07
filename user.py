class User:
    def __init__(self, name):
        self.name = name
        # account balance already has a default value, so we do not have to include that as a parameter. If the default wasn't zero, we would have to include it as a parameter.
        self.account_balance = 0
    # deposit method
    def make_deposit(self, amount):
        # takes an argument that is the amount of the deposit
        self.account_balance += amount
        # the specific user's account increases by the amount of the value received
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

# line below: creating an instance of User called sarah.
sarah = User("Sarah Perez")
catherine = User("Catherine Smith")
sally = User("Sally Miller")

# Looking at the parameters in make_deposit and make_withdrawal, we are passing sarah (what sarah is equal to) in as an argument for self and passing the numeric value in parentheses as an argument for amount
sarah.make_deposit(325)
sarah.make_deposit(642)
sarah.make_deposit(122)
sarah.make_withdrawl(236)
sarah.display_user_balance()

catherine.make_deposit(27)
catherine.make_deposit(42)
catherine.make_withdrawl(6)
catherine.make_withdrawl(17)
catherine.display_user_balance()

sally.make_deposit(657)
sally.make_withdrawl(97)
sally.make_withdrawl(46)
sally.make_withdrawl(22)
sally.display_user_balance()