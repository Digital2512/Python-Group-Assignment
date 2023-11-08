import os
import sys 
import time
import database
import generalUtils

def pgMain():
    loggedIn = False
    while True: 
        generalUtils.createNewLine()
        print("Welcome to Excellent Tution Centre(ETC)\n1. LOGIN\n2. EXIT")
        generalUtils.createNewLine()
        choice = int(input("Choice: "))
        if choice == 1: 
            #Login 
            print("\nLogin")
            list = database.readFile("UserCredentials.txt")

            #Give 3 tries for username and also password respectively
            for i in range(0 , 3, 1):
                inputUsername = input("\nUsername: ")
                isUsernameFound = database.searchListValue(inputUsername, 2, list)
                if isUsernameFound:
                    break

            if isUsernameFound == False:
                return
            
            for i in range(0,3,1):
                inputPassword = input("\nPassword: ")
                isPasswordFound = database.searchListValue(inputPassword, 3, list)
                if isPasswordFound:
                    break
            
            if isPasswordFound == False:
                return
            
            # Success logged in
            if isUsernameFound and isPasswordFound == True:
                roleFound = database.readListValue(inputPassword, 3, 1,"UserCredentials.txt")
                capitalizedRole = roleFound.upper()
                if capitalizedRole == "ADMIN":
                    print("Admin")
                elif capitalizedRole == "TUTOR":
                    print("Tutor")
                elif capitalizedRole == "STUDENT":
                    print("Student")
                elif capitalizedRole == "RECEPTIONIST":
                    print("Receptionist")
                else: 
                    print("Role Not Found")
                    break

        elif choice == 2:
            print("\nThank you for visiting TEC")
            sys.exit()

        else:
            print("\nInvalid Option")
            continue

print("Welcome to TEC")
pgMain()
