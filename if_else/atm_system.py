
# Question : Write a Program to simulate ATM withdrawal.

balance = int(input("enter account balance :- "))
ammount = int(input("enter Withdrawal Ammount:- "))

if balance < 1000:
    print("Minimum balance required does not met")

elif ammount > balance:
     print("Insufficient balance")

else:
     if ammount > 2000:
          charge = ammount * 0.02 
          deduction = ammount + charge
          remaining_balance = balance - deduction

          print("Withdraw Successful") 
          print(f"Chared applied - {charge}")
          print(f"Remaining balance - {remaining_balance}")

     else:
          remaining_balance = balance - ammount

          print("Withdraw Successful") 
          print("no charged applied")
          print(f"Remaining balance - {remaining_balance}")
    

    

