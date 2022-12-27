class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, withdraw):
        if withdraw > self.balance and self.checking_accounr:
            return ValueError
        self.balance -= withdraw
        return "{} has {}.".format(self.name,self.balance)

    def check(self, name, cash):
        if name.balance >= cash and name.checking_account:
            name.balance -= cash
            self.balance += cash
        else:
            return "Error"
        return "{} has {} and {} has {}.".format(self.name,self.balance,name.name,name.balance)

    def add_cash(self, cash):
        self.balance += int(cash)
        return self.name + ' has ' + str(self.balance) + "."
