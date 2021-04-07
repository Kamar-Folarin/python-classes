import random
import datetime

database = {} #dictionary
balance = 0

dt = datetime.datetime.now()
dt_string = dt.strftime("Date: %d/%m/%Y  time: %H:%M:%S")

def init():
    print(dt_string)
    print("Welcome to BankAVIA")
    
    holdAnAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(holdAnAccount == 1):
        login()

    elif(holdAnAccount == 2):
        register()

    else:
        print("You have selected invalid option")
        init()

#Function to perform login operations
def login():
    
    print("********* Login ***********")

    accountNumberFromUser = int(input("Enter your account number? \n"))
    password = input("Enter your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
            else:
                print('Invalid account or password')
                register()

                  
    
    

#Function to perform user registration 
def register():

    print("****** Register *******")
    

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a secure password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has been created")
    print(" ** **** ****** **** **")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" ** **** ****** **** **")

    login()

#Function for performing basic banking operations(deposit, withdrawals)
def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
        depositOperation()

    elif(selectedOption == 2):
        withdrawalOperation()

    elif(selectedOption == 3):
        logout()

    elif(selectedOption == 4):
        exit()
    
    else:
        print("Invalid option selected")
    
#Function to peform another banking operation before login out
def perform_another_operation():
    do_another_operation = int(input("  Would you like to perform another operation? 1. Yes 2. No \n" ))

    if (do_another_operation == 1):
        login()

    elif (do_another_operation == 2):
        exit()
    
    else:
        print("Invalid option selected")


    

def withdrawalOperation():
    amount = float(input("Enter amount to be withdrawn: "))
    global balance
    if balance >= amount:
        balance -= amount
        print("\n You Withdrew:", amount)
    else:
        print("\n Insufficient balance  ")

    perform_another_operation()

def depositOperation():
    amountDeposited = float(input("Enter amount to be deposited: "))
    global balance
    balance += amountDeposited
    print("\n Amount Deposited:", amountDeposited)
    
    perform_another_operation()


#Function to generate a 10 digit random occuring bank account number
def generationAccountNumber():
    return random.randrange(1111111111,9999999999)

def logout():
    login()


init()
