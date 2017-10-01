from datetime import datetime
import pytz


class Account(object):
    @staticmethod
    def __current_time():
        return datetime.utcnow().isoformat()

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account.__current_time(),balance)]
        # self.transaction_list.append((Account.__current_time(), balance)) # or you can edit the show transction list above this line from []
        print 'Account created for {}'.format(self.name)


    def show_bal(self):
        print ' the balance is {}'.format(self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_list.append((Account.__current_time(), amount))
        else:
            print ' ERROR: The Ammount must be positive'
        print ' The ammount deposited is {} and the balance is {}'.format(amount, self.balance)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account.__current_time(), -amount))
        else:
            print 'ERROR:The ammount is greater then the current Balance'
        print ' The ammount withdraw is {} and the balance is {} '.format(amount, self.balance)

    def transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                trans_type = 'deposite'
            else:
                trans_type = "withdraw"
                amount *= -1
            print '{:2} was {} on {}  '.format(amount, trans_type, date)


if __name__ == '__main__':
    jack = Account('jack', 3000)
    jack.deposit(4000)
    jack.withdraw(2000)
    jack.transaction()
    jack.show_bal()
    print 
    stephen  = Account('Stephen',2000)
    stephen.deposit(4400)
    stephen.withdraw(200)
    stephen.transaction()
    stephen.show_bal()
