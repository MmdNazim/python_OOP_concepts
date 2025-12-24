"""
Docstring for encapsulation:
----------------------------
Here is the links that's helps us to understand the details:
------------------------------------------------------------
1.https://www.geeksforgeeks.org/python/encapsulation-in-python/
2.https://www.w3schools.com/python/python_encapsulation.asp
3.https://www.scaler.com/topics/python/encapsulation-in-python/
"""

class BankAccount:

    __balance = 0  


    #Deposit:
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("your deposit success")

        else:
            print("Invalid Amount")


    #Balance withdraw:
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("withdraw successful")

        else:
            print("insufficient balance")


    #Check Balance:
    def CheckBalance(self):
        return self.__balance
    
obj = BankAccount()

obj.deposit(1000)

print(obj.CheckBalance())

obj.withdraw(500)

print(obj.CheckBalance())
