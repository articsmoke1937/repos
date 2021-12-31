class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    type="checking"
    
    def __init__(self, filepath,fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance = self.balance-amount-self.fee


checking=Checking("balance.txt",1)
print(checking.balance)
checking.transfer(10)
print(checking.balance)


'''

checking=Checking("balance.txt")
checking.deposit(10)
checking.commit()
print(checking.balance)


account=Account("balance.txt")
print(account.balance)
account.withdraw(100)
account.deposit(1000)
print(account.balance)
account.commit()
'''
