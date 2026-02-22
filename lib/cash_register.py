#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount =None,total = 0 ):
        self._discount = 0
        self.total = total
        self.items = []
        self.previous_transactions = []

        if discount is None:
            user_input = input('Enter discount percentage (0-100) :').strip()
            if user_input == '':
                self.discount = 0
            else:
                try:
                    self.discount = int(user_input)
                except ValueError:
                    print('Not valid discount')
        else:
            self.discount = discount

    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) and value not in range(0, 100):
            print('Not valid discount')
        else:
            self._discount = value

    def add_item(self, item, price, quantity):
        item_total = price * quantity
        self.total += item_total
        new_item = {'item' : item,
                    'price': price,
                    'quantity': quantity}
        self.items.append(item)
        self.previous_transactions.append(new_item)

        print(f'\n{item} added to the list with a total price of {self.total}')

    def apply_discount(self):
        if not self.previous_transactions:
            print('There is no discount to apply')
            return
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount


        last_transaction = self.previous_transactions.pop()

        if self.items:
            self.items.pop()

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        item_total = last_transaction["price"] * last_transaction["quantity"]

        self.total -= item_total

        if self.items:
            self.items.pop()
        





register = CashRegister()
register.add_item('Pencil', 76, 90)
register.add_item('Rubber', 67, 30)

print(register.previous_transactions)
print(register.total)

register = CashRegister(20)

register.add_item("Apple", 10, 2)   # total = 20
register.add_item("Banana", 5, 1)   # total = 25

print(register.total)   # 25

register.apply_discount()
print(register.total)   # 20.0 (20% off 25)

register.void_last_transaction()
print(register.total)