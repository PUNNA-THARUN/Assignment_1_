## Challenge 1: Square Numbers and Return Their Sum

class Point:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return ((self.x**2)+(self.y**2)+(self.z**2))
obj = Point(1,3,5)
sum_of_Sq = obj.sqSum()
print("Challenge-1 Output:- \n",sum_of_Sq)

##### output:- 35
"""============================================================================================="""

##Challenge 2: Implement a Calculator Class

class Calculator:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        addition = self.num1 + self.num2
        print(addition)
    def sub(self):
        subtract = self.num1 - self.num2
        print(subtract)
    def mul(self):
        multiply = self.num1 * self.num2
        print(multiply)
    def div(self):
        division = self.num1 / self.num2
        print(division)
obj = Calculator(94,10)
print("\nChallenge-2 Output:- ")
obj.add()
obj.sub()
obj.mul()
obj.div()

##### output:- 
# 104
# 84
# 940
# 9.4

"""=========================================================================================================="""

## Challenge 3: Implement the Complete Student Class

class Student:
    def __init__(self,__name,__rollNum):
        self.__name = __name           
        self.__rollNum = __rollNum

    def __str__(self):
        return f"Student: \nname: {self.__name} \nrollNum: {self.__rollNum}"

    def set_name(self,__name):
        self.__name = __name

    def get_name(self):
        return self.__name

    def set_rollNum(self,__rollNum):
        self.brand = __rollNum

    def get_rollNum(self,__rollNum):
        return self.__rollNum

student = Student("raju","12")
print("\nChallenge-3 Output:- \n",student)

##Output :-
# Student:
# name: raju
# rollNum: 12

"""=========================================================================================================="""

## Challenge 4: Implement a Banking Account

class Account:
    
    def __init__(self,title,balance):
        self.title = title
        self.balance = balance
        
    def display(self):
        return f"Name of Account Holder : {self.title} \nAcc Balance : {self.balance}"

class SavingsAccount(Account):

    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate
    def display(self):
        data = super().display()
        return f"Name of Account Holder : {self.title} \nAcc Balance : {self.balance} \nInterest : {self.interestRate}"

obj = SavingsAccount("Arjun", 500, 5)
data = obj.display()
print("\nChallenge-4 Output:- \n", data)

##Output :-
# Name of Account Holder : Arjun
# Acc Balance : 500
# Interest : 5

"""=========================================================================================================="""

## Challenge 5: Handling a Bank Account

class Account:
    
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
    
    def deposit(self, amount):
        self.amount = amount
        self.dep = self.balance + self.amount
        return

    def withdrawl(self,W_amount):
        self.w_amount = W_amount
        self.wd = self.dep - self.w_amount
        return

    def getBalance(self):
        self.bal = self.balance + self.amount - self.w_amount
        return 

class SavingsAccount(Account):

    def __init__(self, title, balance, interestRate):
        self.interestRate = interestRate
        super().__init__(title ,balance)

    def deposit(self):
        super().deposit(amount=2000)
    def withdrawl(self):
        super().withdrawl(W_amount=500)
    def getBalance(self):
        super().getBalance()
        return
    def interestamount(self, intrst_amount):
        self.intrst_amount = intrst_amount 
        return
    def display(self):
        self.intrst_amount = self.bal / 100 * self.interestRate
        print(f"Name of Account Holder : {self.title} \nAfter deposit amount : {self.dep} \nAfter Withdrawl amount : {self.wd} \nAcc Balance : {self.bal} \nInterest : {self.interestRate} \nInterest_amount : {self.intrst_amount}")
        
obj = SavingsAccount("arun", 7000, 5)
print("\nChallenge-5 Output:- ")
obj.deposit()
obj.withdrawl()
obj.getBalance()
obj.display()

##Output:- 
# Name of Account Holder : arun 
# After deposit amount : 9000 
# After Withdrawl amount : 8500 
# Acc Balance : 8500 
# Interest : 5 
# Interest_amount : 425.0
"""=========================================================================================================="""

