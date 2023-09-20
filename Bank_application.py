class Bank():
    
    def __init__(self,firstname,lastname,aadharnumber):
        self.firstname=firstname
        self.lastname=lastname
        self.aadharnumber=aadharnumber
        self.balance=0.0

  #deposit
    def deposit(self,amount):
            self.balance=self.balance+amount 
            print(f'{amount} deposited successfully')

#withdrawal
    def withdraw(self,amount):
         if (amount<self.balance):
          
          self.balance=self.balance-amount
         print(f'{amount} withdrwan successfully.')


#account creation
firstname =input('Enetr your firstname:')
lastname =input('Enter your lastname:')
aadharnumber =int(input('Enter your adhar number :'))
print(f'Hello your account created successfully.')
print('YOUR ACCOUNT BALANCE IS ZERO.')
b=Bank(firstname,lastname,aadharnumber)
while (1):
 print('please select below options')
 print('print 1 for deposit.')
 print('print 2 for withdrawal.')
 print('print 3 for ministatement.')
 print('print 4 for stop.')
 option =int(input('enter number :'))
 if option==1:
    amount=float(input('Enter your depositing amount :'))
    
    b.deposit(amount)
 if option==2:
         
         amount=float(input('Enter your withdrawal amount :'))
         b.withdraw(amount)
 if option==3:
       print(f'you have {amount}')
       print('==========RAGHAVSBANK============')
       print(f'TOTAL AMOUNT :{amount}')
       print('==========THANK YOU============')
if option==4:
     print('THANK YOU....')

