import os
import sys 
import time
import database
import generalUtils
import receptionist
import student
import admin
import tutor

def pgMain():
    while True: 
        generalUtils.clearConsole()
        generalUtils.createNewLine()
        print("Welcome to Excellent Tution Centre(ETC)")
        generalUtils.createNewLine()
        print("1. LOGIN\n2. EXIT")
        generalUtils.createNewLine()
        choice = input("Choice: ")
        if choice == "1": 
            #Login 
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("Login")
            generalUtils.createNewLine()
            list = database.readFile("UserDetails.txt")

            #Give 3 tries for username and also password respectively
            for i in range(0 , 3, 1):
                inputUsername = input("Username: ")
                isUsernameFound = database.searchListValue(inputUsername, 1, "UserDetails.txt")
                if isUsernameFound:
                    break

            if isUsernameFound == False:
                return
            
            for i in range(0,3,1):
                inputPassword = input("\nPassword: ")
                isPasswordFound = database.searchListValueBasedOnValue(inputUsername, 1, 2, inputPassword, "UserDetails.txt")
                if isPasswordFound:
                    break
            
            if isPasswordFound == False:
                return
            
            # Success logged in
            if isUsernameFound and isPasswordFound == True:
                roleFound = database.readListValue(inputUsername, 1, 0,"UserDetails.txt")
                capitalizedRole = roleFound.upper()
                if capitalizedRole == "ADMIN":
                    print("Admin")
                    result = admin.pgAdmin(inputUsername)
                    if result == "LOGOUT":
                        continue
                    else: 
                        print("Role Not Found")
                        break
                    # Add code to navigate to the admin's page here
                elif capitalizedRole == "TUTOR":
                    print("Tutor")
                    result = tutor.pgTutor(inputUsername)
                    if result == "LOGOUT":
                        continue
                    else: 
                        print("Role Not Found")
                        break
                    # Add code to navigate to the tutor's page here
                elif capitalizedRole == "STUDENT":
                    print("Student")
                    result = student.pgStudent(inputUsername)
                    if result == "LOGOUT":
                        continue
                    else: 
                        print("Role Not Found")
                        break
                    # Add code to navigate to the student's page here
                elif capitalizedRole == "RECEPTIONIST":
                    print("Receptionist")
                    result = receptionist.pgReceptionist(inputUsername)
                    if result == "LOGOUT":
                        continue
                    else: 
                        print("Role Not Found")
                        break
                    # Add code to navigate to the receptionist's page here
            else: 
                print("Your account could not be accessed (If you think this is a mistake, please contact the Admin)")
                break

        elif choice == "2":
            print("\nThank you for visiting TEC")
            sys.exit()

        else:
            print("\nInvalid Option")
            continue


pgMain()
