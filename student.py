import generalUtils
import database
import UniqueIDCreation

def writeRequest(requestID, userID, fullName, currentSubject, requestedSubject, fileName):
    with open (fileName,"+a") as file:
        requestString = f"{requestID};{userID};{fullName};{currentSubject};{requestedSubject}"
        file.write(requestString)
        return True


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
            print("1. View Class Schedule\n2. Send Subject Change Request\3. Update Profile\n4. Log Out")
            generalUtils.createNewLine()
            choice = input("Choice\n")
            if choice == "1":
                print("View Class Schedule")
            elif choice == "2":
                print("Subject change request")
                generalUtils.createNewLine()
                print("1. Send a request\n2. Delete a request")
                generalUtils.createNewLine()
                choiceRequest = input("Choice: ")
                if choiceRequest == "1":
                    print("Send a request")
                    generalUtils.createNewLine()
                    with open("UserDetails.txt", "+r") as file:
                        for line in file:
                            values = line.strip().split(";")
                            if values[1] == userID:
                                fullName = values[4]
                                formattedName = values[4].replace("_", " ")
                    currentSubject = input("Current Subject: ")
                    requestedSubject = input("Requested Subject: ")
                    writeRequest()
                elif choiceRequest == "2":
                    print("Delete a request")
            elif choice == "3":
                print("View Profile")
            elif choice == "4":
                print("Log Out")
                return "LOGOUT"
            else:
                continue

