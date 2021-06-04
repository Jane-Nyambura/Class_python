class  Account:
      def __init__(self,name,phone, loan_limit):
        self.name=name
        self.phone=phone
        self.balance=0
        self.loan=0
        self.loan_limit=loan_limit
      def deposit(self,amount):
        if amount<=0:
          return f"the amount must be greater than 0"
        else:
          self.balance+=amount
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
          return f"Dear {self.name} you have  withdrawn{amount} your new balance is {self.balance}"


      def borrow(self,amount):
        if amount>self.loan_limit:
           print(f"The amount is above your loan limit")
        elif self.loan>0:
          print(f"please clear your debt")
        else:
          self.loan+=1
          self.balance+=amount
          return f"You have successfully borrowed"

