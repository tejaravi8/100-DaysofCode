import random
class Bank:
    Holder_Details=[{'Holder_Name':"Raviteja",'Aadhar_Number':"123412341234",'Mobile':"9111900012",'IFSCCODE':"IFSC05235",'Account_Number':9948914093,'Suffitient_Balance':500}]
    def create_new_Account(self):
        print('***=========*** Welcome to My Bank ***========***')
        new_Holder={}
        new_Holder['Holder_Name']=input('Enter Holder name:')
        new_Holder['Aadhar_Number']=input('Enter Aadhar number:')
        new_Holder['Mobile']=input('Enter Mobile number:')
        new_Holder['IFSCCODE']='IFSC05235'
        data=random.randint(1111111111,9999999999)     
        new_Holder['Account_Number']=data
        
        Type_of_Acc=input('Select Account Type Saving/ Zero:').lower()
        while True:
            if Type_of_Acc =='saving':
                print('Your Account is saving You have to deposite 500 rupees:')
                s_acc=int(input('Deposite 500 rupees:'))
                if s_acc==500:
                    new_Holder['Suffitient_Balance']=s_acc
                    break
                else:
                    print('==== please Deposite 500 rupees then only your Account Created! ===')
            if Type_of_Acc=='zero':
                print('Your Account is zero You have to deposite 100 rupees:')
                s_acc=int(input('Deposite 100 rupees:'))
                if s_acc==100:
                    new_Holder['Suffitient_Balance']=s_acc
                    break
                  
                else:
                    print('please Deposite 100 rupees then only your Account Created!***')
        Bank.Holder_Details.append(new_Holder)
        print(Bank.Holder_Details)
        
    def Deposit(self):
        print('======welcome to Deposit option =======')
        
        n1=input('Enter Holder name:')
        n2=int(input('Enter Account Number:'))
        n3=int(input('Enter Deposit money:'))
        for x in Bank.Holder_Details:
            if x['Holder_Name']==n1 and x['Account_Number']==n2:
                data1=x.get('Suffitient_Balance')
                x['Suffitient_Balance']=data1+n3
            else:
                print('Account not found')
        print(Bank.Holder_Details)
    def with_Draw(self):
        print('======welcome to Withdraw option =======')
        
        p1 = input('Enter Holder name: ')
        p2 = int(input('Enter Account Number: '))
        p3 = int(input('Enter amount to withdraw: '))
        
        for x in Bank.Holder_Details:
            if x['Holder_Name'] == p1 and x['Account_Number'] == p2:
                if x['Suffitient_Balance'] >= p3:
                    x['Suffitient_Balance'] -= p3
                    print(f"Withdrawal successful. Remaining Balance:{x['Suffitient_Balance']}")
                    break
                else:
                    print('Insufficient balance. Please check your balance once.')
                    break
            else:
                print(' Account not found.')
        print(Bank.Holder_Details)
        
    def Details(self):
        t1=input('Enter Holder name:')
        t2=int(input('Enter Account Number:'))
        for x in Bank.Holder_Details:
            if x['Holder_Name']==t1 and x['Account_Number']==t2:
                for a,b in x.items():
                    print(a,'==>',b)
            else:
                print('Account Not Found')
                    
    def Check_Balance(self):
        t10=input('Enter Holder name:')
        t20=int(input('Enter Account Number:'))
        for x in Bank.Holder_Details:
            if x['Holder_Name']==t10 and x['Account_Number']==t20:
                print('Balance==>:',x['Suffitient_Balance'])
            else:
                print('Account not found')
        


obj=Bank()
while True:
    print('''\n----- Bank Menu -----
1) Create New Account
2) Deposit
3) Withdraw
4) Account Details
5) Check Balance
6) Exit''')
    
    choice = input('Choose an option (1-6): ')
    
    if choice == '1':
        obj.create_new_Account()
    elif choice == '2':
        obj.Deposit()
    elif choice == '3':
        obj.with_Draw()
    elif choice == '4':
        obj.Details()
    elif choice == '5':
        obj.Check_Balance()
    elif choice == '6':
        print('Thank you for using the banking system.')
        break
    else:
        print('Invalid option. Please choose between 1 to 6.')
                   

