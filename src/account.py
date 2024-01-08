'''
@file account.py
@details contains Account class
'''

from numpy import double


class Account:
    def __init__(self, acc_num: int, pin: int, balance: double):
        self.acc_num = acc_num
        self.pin = pin
        self.balance = balance

    def __str__(self):
        return f'Account number: {self.acc_num}\nAccount pin: {self.pin}\nAccount balance: Rs {self.balance:.2f}'

# acc1 = Account(12345678, 1234, 10000.00)
# print(acc1)