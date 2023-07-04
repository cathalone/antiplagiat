class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. New balance: {self.balance} units.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount} units. New balance: {self.balance} units.")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: {self.balance} units.")


# Пример использования класса BankAccount
account = BankAccount("123456789", "John Doe", 1000)
account.display_balance()  # Вывод информации о счете

account.deposit(500)  # Внесение средств на счет
account.withdraw(200)  # Снятие средств со счета
account.withdraw(1500)  # Попытка снятия суммы, превышающей баланс

account.display_balance()  # Вывод обновленной информации о счете