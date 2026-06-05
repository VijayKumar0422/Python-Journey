balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= balance:
    balance = balance - withdraw
    print("withdrawal successful")
    print("remaining balance = ",balance)
else:
    print("Insufficient balance")