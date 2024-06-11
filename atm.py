contacts = []

def createAccount(firstName,lastName,pin,phoneNumber):
    accountNumber = phoneNumber[1:]
    balance = 0.0
    contact = [firstName,lastName,pin,balance,phoneNumber,accountNumber]
    contacts.append(contact)
    main()

def checkBalance():
    count = 1
    for contact in contacts:
        print("account", count)
        count+=1
        for element in contact:
            print(element)
def deposit_amount(accountNumber, amount, pin):
        for contact in contacts:
            if accountNumber == contact[5] and pin == contact[2]:
                contact[3] += amount
            return contact[3]
        main()







def main():
    menu = """ 
    1  create_account
    2  check_balance 
    3  deposit_amount
    4  validation
    5  withdraw 
    6  transfer
    """
    print(menu)
    main_menu = int(input("Select any option "))
    match(main_menu):
        case 1:
            firstName = input("Enter your firstName: ")
            lastName = input("Enter your lastName: ")
            pin = input("Enter your pin: ")
            phoneNumber = input("Enter your phoneNumber: ")
            createAccount(firstName,lastName,pin,phoneNumber)
        case 2:
            checkBalance()
        case 3:
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount: "))
            pin = input("Enter pin: ")
            deposit_amount(account_number,amount,pin)

    main()



























