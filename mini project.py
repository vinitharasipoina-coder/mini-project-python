balance=10000
def check_balance():
    print("Available balance:Rs",balance)
def deposite():
    global balance
    amount = int(input("Enter deposite amount: Rs"))
    if amount <= 0:
       print("please enter a postive amount:")
    else:
        balance += amount
        print("Amount deposited sucessfully!")
        print("updated balance:Rs",balance)
def withdraw():
    global balance
    amount=int(input("enter withdraw amount:Rs"))
    if amount <=0:
        print("enter a positive amount")
    elif amount>balance:
        print("insuficient balance!")
    else:
        balance -= amount
        print("withdrawal suceesful!")
        print("remaining balance: Rs",balance)
def show_menu():
      print("\n==== ATM ====")
      print("1.check balance")
      print("2.deposite")
      print("3.withdraw")
      print("4.exit")
while True:
    show_menu()
    choice = input("enter your choice:")
    if choice == "1":
        check_balance()
    elif choice =="2":
        deposite()
    elif choice =="3":
         withdraw()
    elif choice =="4":
         print("thank you for using the atm!")
         break
    else:
        print("invalid choice!please select 1 to 4.")
                 
    
                
                     









    






    
