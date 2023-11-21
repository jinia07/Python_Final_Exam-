class Bank:
    init_bank_balance = 0
    total_loan = 0
    loan_feature_enabled = True

    @staticmethod
    def get_bank_balance():
        return Bank.init_bank_balance

    @staticmethod
    def get_total_loan():
        return Bank.get_total_loan

class User:
    def __init__(self, user_name, user_account, user_balance=0):
        self.user_name = user_name
        self.user_account = user_account
        self.user_balance = user_balance
        self.user_transaction = []

    def deposit(self, amount):
        self.user_balance += amount
        Bank.init_bank_balance += amount
        self.user_transaction.append(f'Deposited amount: {amount}')

    def withdraw(self, amount):
        if self.user_balance >= amount:
            self.user_balance -= amount
            Bank.init_bank_balance -= amount
            self.user_transaction.append(f'Withdrew amount: {amount}')
        else:
            print("Sorry, your account does't have enough funds.")

    def transfer(self, recipient, amount):
        if self.user_balance >= amount:
            self.user_balance -= amount
            recipient.init_bank_balance += amount
            self.user_transaction.append(
                f'Transferred {amount} to account {recipient.user_account}')
            recipient.user_transaction.append(
                f'Received {amount} from account {self.user_account}')
        else:
            print("Does't have enough funds!")

    def check_balance(self):
        return self.user_balance

    def take_loan(self):
        if Bank.loan_feature_enabled:
            loan_limit = self.user_balance * 2
            if Bank.total_loan < loan_limit:
                self.user_balance += self.user_balance
                Bank.init_bank_balance += self.user_balance
                self.user_transaction.append(
                    f'Took a loan of amount: {self.user_balance}')
                Bank.total_loan += self.user_balance
            else:
                print("You have reached the maximum loan amount allowed!")
        else:
            print("Sorry, you can't take a loan right now. Please try again later.")

    def check_transaction_history(self):
        return self.user_transaction

class Admin:
    def create_user_account(self, name, account_number, initial_deposit=0):
        return User(name, account_number, initial_deposit)

    @staticmethod
    def check_bank_balance():
        return Bank.check_bank_balance()

    @staticmethod
    def check_total_loan_amount():
        return Bank.check_total_loan_amount()

    @staticmethod
    def loan_feature_on():
        Bank.loan_feature_enabled = True
        print("Loan feature is now available!")

    @staticmethod
    def loan_feature_off():
        Bank.loan_feature_enabled = False
        print("You can now borrow money.")

admin = Admin()

print('--------- User Information ---------')

user1 = admin.create_user_account("kuddus ali", 125864, initial_deposit=50000)
print(user1.user_name, user1.user_account, user1.user_balance)

user2 = admin.create_user_account("enamul mia", 564689485, initial_deposit=32000)
print(user2.user_name, user2.user_account, user2.user_balance)

user3 = admin.create_user_account("Hasem khan ", 689641, initial_deposit=45000)
print(user3.user_name, user3.user_account, user3.user_balance)

user4 = admin.create_user_account("Jorina begum", 65445, initial_deposit=83000)
print(user4.user_name, user4.user_account, user4.user_balance)