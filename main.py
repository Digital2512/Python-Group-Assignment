import os
import sys 
import time

def listToString(list):
    string = ''
    for i in range(0, len(list), 1):
        if (i == (len(list)-1)):
            string = string + str(list(i)) + "\n"
        else:
            string = string+str(list(i))+";"
    return string

def clearConsole():
        #Function to clear console
        print("\n"*200)
        print("="*50)

def createNewLine():
    #Function to create a new line for the GUI
    print("="*50)

def db_convertFileToString(fileName, list):
    #Fuction to convert any file into a 1D list 
    with open(fileName, "+a") as appendedFile:
        appendedFile.write(listToString(list))
    return appendedFile

def db_writeToFile(fileName, stringVariable):
    #Function to write the string into the file 
    with open(fileName, "+a") as writtenFile: 
        writtenFile.write(stringVariable)

def db_overwriteFile(fileName, stringVariable):
    #Function to overwrite the file with the string variable
    with open(fileName, "+w") as file:
        file.write(stringVariable)

def db_readFile(fileName):
    list=[]
    with open(fileName, "+r") as file:
        for line in file:
            list.append(line.strip().split(";"))
    return list

def searchListValue(inputString,  indexToSearch, listToCheck):
    #check if the input string matches the item in the list at a specific index
    for item in listToCheck:
        if inputString == item[indexToSearch]:
            return True
    return False

def readListValue(valueInput, indexToCheck, indexToRead, listToCheck):
    #read a specific value from the list
    with open(listToCheck, "+r") as file:
        for line in file:
            values = line.strip().split(";")
            if 0 <= indexToRead < len(values): 
                if values[indexToCheck] == valueInput:
                    return values[indexToRead]
            else: 
                return "Index Out Of Bound"

def pgMain():
    loggedIn = False
    while True: 
        createNewLine()
        print("Welcome to Excellent Tution Centre(ETC)\n1. LOGIN\n2. EXIT")
        createNewLine()
        choice = int(input("Choice: "))
        if choice == 1: 
            #Login 
            print("\nLogin")
            list = db_readFile("UserAndPasswordList.txt")

            #Give 3 tries for username and also password respectively
            for i in range(0 , 3, 1):
                inputUsername = input("\nUsername: ")
                isUsernameFound = searchListValue(inputUsername, 1, list)
                if isUsernameFound:
                    break

            if isUsernameFound == False:
                return
            
            for i in range(0,3,1):
                inputPassword = input("\nPassword: ")
                isPasswordFound = searchListValue(inputPassword, 2, list)
                if isPasswordFound:
                    break
            
            if isPasswordFound == False:
                return
            
            # Success logged in
            if isUsernameFound and isPasswordFound == True:
                roleFound = readListValue(inputPassword, 2, 3,"UserAndPasswordList.txt")
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
firstAdminLogin = ("A001;Admin;Admin123;ADMIN")
db_overwriteFile("UserAndPasswordList.txt", firstAdminLogin)
pgMain()
