import self as self


class Person:
    def __init__(self, person_id, first_name, last_name):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name
        # customer_id must be unique


class Account:

    def __init__(self, account_number, account_type, owner, balance):
        self.number = account_number
        self.type = account_type
        self.owner = owner
        self.balance = 0

    def decrease_balance(self, amount):
        self.balance -= amount

    def increase_balance(self, amount):
        self.balance += amount


class Bank:
    def __init__(self, new_balance):

    def deposit_money_into_bank(self, amount):
        new_balance = Account.increase_balance(amount)
        return new_balance


    def add_customer_to_bank(self):
    pass


    def add_account_to_bank(self):
    pass


    def remove_account_from_bank(self):
    pass


    def withdraw_money_from_account(self):
    pass


    def balance_inquiry_for_account(self):
    pass
