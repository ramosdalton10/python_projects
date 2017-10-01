import pytz
import datetime


class Account(object):
    ''''
    creating a bank  account
    '''

    @staticmethod
    def _current_time():
        utd_date = datetime.datetime.utcnow()
        return pytz.utc.localize(utd_date)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_balance = []
        print 'Account creat for {0}'.format(self.name)

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_balance.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.show_balance()
            self.transaction_balance.append((Account._current_time(), -amount))
        else:
            print 'amount {} is greater then the your balance'.format(self.balance)

    def show_balance(self):
        print 'The Balance is {}'.format(self.balance)

    def tranaction(self):
        for data, amount in self.transaction_balance:
            if amount > 0:
                trans_type = 'desposited'
            else:
                trans_type = 'withdrawal'
                amount *= -1
            print '{0} was {1} on {2}'.format(amount, trans_type, datetime.datetime.utcnow())
        # print self.transaction_balance


if __name__ == '__main__':
    madvesh = Account('madvesah', 3333)
    print madvesh.deposite(444)
    print madvesh.withdraw(222)
    print madvesh.transaction_balance
    # print madvesh.showBalance()
    print madvesh.tranaction()
