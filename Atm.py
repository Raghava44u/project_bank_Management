username="raghava"
password="raghava123"
r_name=input('Enter your name :')
r_password=input('enter your password : ')
if r_name==username and r_password==password:
    print("logined successfully")
    amount=50000
    while 1:
     print('''
          1)deposit
          2)withdrawal
          3)ministatement
          4)exist
          
          ''')
    
     
     option=int(input('Enter your option :'))
     if option==1:
        dep=int(input('Enter your depositing amount :'))
        amount +=dep
        print('========RAGHAVSBANK========')
        print('TOTAL AMOUNT :',amount)
        print('========THANK YOU==========')
     elif option==2:
        withdraw=int(input('Enter your withdrawal amount :'))
        amount +=withdraw
        print('========RAGHAVSBANK========')
        print('TOTAL AMOUNT :',amount)
        print('========THANK YOU==========')
     elif option==3:
        print('TOTAL AMOUNT IN YOUR ACCOUNT :',amount)
     elif option==4:
        print('EXIST....')
        print('========THANK YOU==========')
        break
else:
        print('Entered INCORRET PASSWORD.')
