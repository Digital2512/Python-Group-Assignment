import generalUtils
import database
import UniqueIDCreation
import time

def writeRequest(requestID, userID, fullName, currentSubject, requestedSubject, fileName):
    with open (fileName,"+a") as file:
        requestString = f"{requestID};{userID};{fullName};{currentSubject};{requestedSubject}"
        file.write(requestString)
        return True

def deleteRequest(requestID, fileName):
    deleted = False
    with open(fileName,"r") as file:
        lines = file.readlines()
    
    for line in lines:
        values = line .strip().split(";")
        if values[0] == requestID:
            deleted = True
            continue
        else:
            file.write(line)

    return deleted




def pgStudent(userID):
    while True:
        generalUtils.clearConsole()
        generalUtils.createNewLine()
        with open("UserDetails.txt", "+r") as file:
            for line in file:
                values = line.strip().split(";")
                if values[1] == userID:
                    splittedName = values[4].replace("_"," ")
                    print(f"Welcome, {splittedName} ({values[0]})")
        generalUtils.createNewLine()
        while True: 
            print("1. View Class Schedule\n2. Send Subject Change Request\3. Update Profile\n4. View profile\n4. Log Out")
            generalUtils.createNewLine()
            choice = input("Choice\n")
            if choice == "1":
                print("View Class Schedule")
            elif choice == "2":
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Subject change request")
                generalUtils.createNewLine()
                print("1. Send a request\n2. Delete a request")
                generalUtils.createNewLine()
                choiceRequest = input("Choice: ")
                if choiceRequest == "1":
                    print("Send a request")
                    generalUtils.createNewLine()
                    existingIDs = UniqueIDCreation.readIDFromExistingFile("StudentRequest.txt",0)
                    requestID = UniqueIDCreation.generateRequestID(existingIDs)
                    with open("UserDetails.txt", "+r") as file:
                        for line in file:
                            values = line.strip().split(";")
                            if values[1] == userID:
                                fullName = values[4]
                                formattedName = values[4].replace("_", " ")
                    currentSubject = input("Current Subject: ")
                    requestedSubject = input("Requested Subject: ")
                    writeRequest(requestID,userID,fullName,currentSubject,requestedSubject,"StudentRequest.txt")
                elif choiceRequest == "2":
                    print("Delete a request")
                    generalUtils.createNewLine()
                    deleteRequestID = input("Request ID: ")
                    if deleteRequest(deleteRequestID, "StudentRequest.txt") == True:
                        print("Subject change request has been deleted")
                    else: 
                        print("Subject change request is not deleted")
            elif choice == "3":
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Update Profile")
                generalUtils.createNewLine()
                password = input("Password: ")
                ICNumber = int(input("\nIC Number: "))
                fullName = input("\nFull name: ").replace(" ","_")
                email = input("\nEmail: ")
                phoneNumber = int(input("\nPhone Number: "))
                generalUtils.createNewLine()
                while True: 
                    gender = input("Gender: \n1. Male\n2. Female\n3. N/A\nChoice: ").upper()
                    generalUtils.createNewLine()
                    if gender == "MALE" or gender == "FEMALE" or gender == "N/A":
                        break
                    else: 
                        continue
                while True: 
                    birthday = input("Birthday(DD/MM/YYYY): ").replace("/","-")
                    generalUtils.createNewLine()
                    if len(str(birthday)) == 10:
                        break
                    else:
                        continue
                print(f"ID Number: {userID}\nPassword: {password}\nIC Number: {ICNumber}\nFull Name: {fullName}\nEmail: {email}\nPhone Number: {phoneNumber}\nGender: {gender}\nBirthday: {birthday}\n")
                while True:
                    print("Is this correct? Y/N ")
                    confirmationChoice = input("Choice: ").upper()
                    if confirmationChoice == "Y":
                        if updateProfile("UserDetails.txt", userID, "RECEPTIONIST",password,ICNumber,fullName,email,phoneNumber,birthday,gender) == True:
                            print("Profile Updated")
                            break
                    elif confirmationChoice == "N":
                        print("Profile not updated")
                        break
                    else:
                        print("Invalid Input!\n")
                    time.sleep(5)
            elif choice == "4":
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("View Profile")
                generalUtils.createNewLine()
                ICNumber = database.readListValue(userID, 1, 3, "UserDetails.txt")
                fullName = database.readListValue(userID, 1, 4, "UserDetails.txt")
                email = database.readListValue(userID, 1, 5, "UserDetails.txt")
                phoneNumber = database.readListValue(userID, 1, 6, "UserDetails.txt")
                gender = database.readListValue(userID, 1, 7, "UserDetails.txt")
                birthday = database.readListValue(userID, 1, 8, "UserDetails.txt")

                print(f"User ID: {userID}\nIC Number: {fullName}\nEmail: {email}\nPhone Number: {phoneNumber}\nGender: {gender}\nBirthday: {birthday}")
                generalUtils.createNewLine()
                while True:
                    print("Done Viewing(Enter Y when you are done)? ")
                    generalUtils.createNewLine()
                    doneViewing = input("Choice: ").upper()
                    if doneViewing == "Y":
                        break
                    else:
                        continue
            elif choice == "5":
                print("Log Out")
                return "LOGOUT"
            else:
                continue

