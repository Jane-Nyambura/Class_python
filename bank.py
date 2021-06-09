from datetime import datetime, time
class  Account:
      def __init__(self,name,phone, loan_limit):
        self.name=name
        self.phone=phone
        self.balance=0
        self.loan=0
        self.transaction=[]
        self.loan_limit=loan_limit
        self.withdraw=[]
        self.borrow=[]
        self.repay_loan=[]
      def deposit(self,amount):
        if amount<=0:
          return f"the amount must be greater than 0"
        else:
          self.balance+=amount
          transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"deposit"}
          self.transaction.append(transaction)
          return f"Dear {self.name} you have  deposited {amount} your new balance is {self.balance}"
      def show_balance(self):
        return self.balance

      def withdraw(self,amount):
        if amount<=0:
          return f"the amount must be greater than 0"
        elif amount>=self.balance:
          print(f"you can't withdraw")
        else:
          self.balance-=amount
          # self.balance+=amount
          withdraw={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"deposit"}
          self.withdraw.append(withdraw)
          return f"Dear {self.name} you have  withdrawn{amount} your new balance is {self.balance}"

      def borrow(self,amount):
        if amount>self.loan_limit:
           print(f"The amount is above your loan limit")
        elif self.loan>0:
          print(f"please clear your debt")
        else:
          self.loan+=1
          self.balance+=amount
          # self.balance+=amount
          borrow={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"deposit"}
          self.borrow.append(borrow)
          return f"You have successfully borrowed"
      def get_statement(self):
        for transaction in self.transaction:
          narration=transaction["narration"]
          amount=transaction["amount"]
          balance=transaction["balance"]
          time=transaction["time"]
          print(f"The time for transaction{time.strftime('%D')}your statemate{narration} amount {amount}and balance{balance}")

      def repay_loan(self,amount):
        if amount<0:
          return f"Your amount must not be 0"
        elif amount<self.loan:
          self.loan-=amount
          return f"your loan is reduced"
        else:
          extra=amount-self.loan
          self.balance+=extra
          repay_loan={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"deposit"}
          self.repay_loan.append(repay_loan)
          return f"your loan has been successfully paid and your account  balance is {self.balance}"




