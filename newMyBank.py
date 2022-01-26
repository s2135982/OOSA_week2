''' A new class inherited from the class yourBnak from myBank.py'''
''' Add a new method to automatically deposit £1000'''
''' Make this one “evil” by “overloading” the inquiry method overstate your balance by 20%.'''
''' Modify your new method to only have a 50% chance of lying about the balance.'''

from myBank import yourBank

class newYourBank(yourBank):

    def autoDeposit(self):
        self.balance = self.balance + 1000
        return self.balance
    def inquiry(self):
        self.balance = self.balance * 1.2
        return self.balance

if __name__ == "__main__":
    b = newYourBank('Daisy',1200)
    print(b.autoDeposit())
