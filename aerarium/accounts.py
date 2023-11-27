import uuid
from aerarium.utils import append_to_json, update_config

class Accounts:
    def __init__(self, account_name, account_balance):
        self.account_name = account_name
        self.account_balance = account_balance

    def deposit(self, amount, desc, category):
        self.account_balance += amount
        
        transaction = {
            "transaction_id": str(uuid.uuid4()),
            "amount" : amount,
            "desc" : desc,
            "category" : category,
            "type": "deposit"
        }
        
        append_to_json(transaction)
        update_config(self.account_balance)

        return self.account_balance
    
    def withdraw(self, amount, desc, category):
        self.account_balance -= amount
        
        transaction = {
            "transaction_id": str(uuid.uuid4()),
            "amount" : amount,
            "desc" : desc,
            "category" : category,
            "type": "withdraw"
        }
        
        append_to_json(transaction)
        update_config(self.account_balance)
        
        return self.account_balance
    
    def check_balance(self):
        return self.account_balance
    
if __name__ == '__main__':
    a = Accounts("viraj", 3000) 
    print(a.check_balance())
    print(a.withdraw(2000, "salary", "income"))
    print(a.deposit(5000, "salary", "income"))
    