from abc import ABC, abstractmethod

# Крок 2: Визначення абстрактного класу IActt
class IActt(ABC):
    @abstractmethod
    def attach_customer(self, customer):
        pass

    @abstractmethod
    def detach_customer(self, customer):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

# Крок 1: Клас AccountProxy
class AccountProxy(IActt):
    def __init__(self, acct):
        self.balance = 0
        self.customer = None

    def attach_customer(self, customer):
        self.customer = customer

    def detach_customer(self, customer):
        self.customer = None

    def notify(self):
        if self.customer:
            self.customer.notify(self)

    def deposit(self, amount):
        self.balance += amount
        self.notify()

    def withdraw(self, amount):
        self.balance -= amount
        self.notify()

# Крок 3: Клас Customer
class Customer:
    def __init__(self, name):
        self.name = name

    def notify(self, account_proxy):
        print(f"{self.name}, у вас новий баланс: ${account_proxy.balance}")

    def withdraw(self, amount):
        print(f"Зняття ${amount} з рахунку.")

# Крок 4: Клас ATMController
class ATMController:
    def withdraw_cash(self, customer, amount):
        customer.withdraw(amount)

# Крок 5: Декоратор
class IActtDecorator(IActt):
    def __init__(self, wrapped_account):
        self._wrapped_account = wrapped_account

    def attach_customer(self, customer):
        self._wrapped_account.attach_customer(customer)

    def detach_customer(self, customer):
        self._wrapped_account.detach_customer(customer)

    def notify(self):
        self._wrapped_account.notify()

    def deposit(self, amount):
        self._wrapped_account.deposit(amount)

    def withdraw(self, amount):
        self._wrapped_account.withdraw(amount)

class AutomaticWithdrawalDecorator(IActtDecorator):
    def withdraw(self, amount):
        # Додаткова логіка для автоматичного зняття
        print(f"Автоматичне зняття ${amount} з рахунку.")
        self._wrapped_account.withdraw(amount)

# Приклад використання:
base_account_proxy = AccountProxy(...)
decorated_account_proxy = AutomaticWithdrawalDecorator(base_account_proxy)

customer = Customer("Іван")
decorated_account_proxy.attach_customer(customer)

# Симуляція нового доходу з автоматичним зняттям
decorated_account_proxy.deposit(1000)
