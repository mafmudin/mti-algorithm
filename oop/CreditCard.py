class CreditCard:
    def __init__(self):
        self._customer = ""
        self._bank = ""
        self._account = ""
        self._balance = 0
        self.limit = 0

    # Getter dan setter untuk customer
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        self._customer = value

    # Getter dan setter untuk bank
    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, value):
        self._bank = value

    # Getter dan setter untuk account
    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    # Getter dan setter untuk balance
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    # Getter dan setter untuk limit
    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value

    def make_payment(self, amount):
        print("Pembayaran sejumlah ", amount)

    def charge(self, price):
        print("Charge ", price)


class PredatoryCreditCard(CreditCard):
    def __init__(self):
        self._apr = ""

    def set_apr(self, apr):
        self._apr = apr

    def get_apr(self):
        return self._apr

    def process_month(self):
        pass

    def charge(self, price):
        print("Charge ", price)


if __name__ == '__main__':
    pcc = PredatoryCreditCard()
    pcc.charge(200)
