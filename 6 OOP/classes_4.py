from abc import abstractmethod


class Shape():
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}: {self.area()}'


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        from math import pi
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# shapes = [
#     Circle(5),
#     Rectangle(4, 6)
# ]
#
# for shape in shapes:
#     print(shape)  # Выводит строки с типом и площадью

class BankAccount():
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account(owner={self.owner}, balance={self.balance})"

    def __eq__(self, other):
        return self.owner == other.owner and self.balance == other.balance


class PremiumAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, credit_limit: float = 0.0):
        super().__init__(owner, balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount: float):
        if amount > self.balance + 1000:
            raise ValueError("Недостаточно средств")
        else:
            self.balance -= amount

    def apply_cashback(self, percent):
        self.balance += abs(0.1 * self.balance)


acc1 = BankAccount("Alice", 500)
acc2 = PremiumAccount("Bob", 100, credit_limit=1000)

acc1.withdraw(100)
print(acc1)  # Account(owner=Alice, balance=400.0)

acc2.withdraw(900)  # ОК, баланс станет -800
acc2.apply_cashback(10)  # +10% от 800 = +80, баланс станет -720

print(acc2)  # Account(owner=Bob, balance=-720.0)
print(acc1 == BankAccount("Alice", 400))  # True
