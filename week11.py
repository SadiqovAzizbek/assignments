from abc import ABC, abstractmethod

class Basket(ABC):
    def __init__(self, shopper):
        self.shopper = shopper

    @abstractmethod
    def total(self):
        pass

class Mini(Basket):
    def total(self):
        return 25_000

class Family(Basket):
    def total(self):
        return 90_000

class Bulk(Basket):
    def total(self):
        return 250_000

class Bill(ABC):
    @abstractmethod
    def print_bill(self, purchases):
        pass

class PaperBill(Bill):
    def print_bill(self, purchases):
        for basket in purchases:
            print(f"BILL ({basket.shopper}) = {basket.total()}")

class Loyalty(ABC):
    @abstractmethod
    def notify(self, purchases):
        pass

class EmailLoyalty(Loyalty):
    def notify(self, purchases):
        for basket in purchases:
            print(f"[Loyalty → {basket.shopper}] Earned points for {basket.total()} so'm")

class CheckoutSystem:
    def __init__(self):
        self.purchases = []

    def add(self, basket: Basket):
        self.purchases.append(basket)

    def run(self, bill: Bill, loyalty: Loyalty):
        bill.print_bill(self.purchases)
        loyalty.notify(self.purchases)


store = CheckoutSystem()
store.add(Mini("Kakashi"))
store.add(Family("Itachi"))
store.add(Bulk("Hinata"))
store.run(PaperBill(), EmailLoyalty())