import generalUtils
import database
import UniqueIDCreation
import time

def updateStudentProfile(fileToCheck, IDNumber, role, password, ICNumber, fullName, email, phoneNumber, birthday, gender, subjectAssigned, numberOfSubjects, studentForm):
    updatedProfile = False
    capitalizedRole = role.upper()
    updated_data = []  # To store updated data
    with open(fileToCheck, "+r") as file:
        for line in file:
            values = line.strip().split(";")
            if values[1] == str(IDNumber):
                # Skip the line to delete it
                updatedProfile = True
                continue
            updated_data.append(line)

    # Add the updated line at the end
    if updatedProfile == True: 
        updated_data.append(f"{capitalizedRole};{IDNumber};{password};{ICNumber};{fullName};{email};{phoneNumber};{gender};{birthday};{studentForm};{numberOfSubjects};{subjectAssigned};\n")

    # Write the updated data back to the file
        with open(fileToCheck, "+w") as file:
            file.writelines(updated_data)
    return updatedProfile

def writeSubjectRequest(requestID, userID, fullName, currentSubject, requestedSubject, fileName):
    with open (fileName,"+a") as file:
        requestString = f"{requestID};{userID};{fullName};{currentSubject};{requestedSubject};PENDING;\n"
        file.write(requestString)
        return True
    
def writePaymentRequest(requestID, userID, fullName, subjectCode, amount, fileName):
    with open (fileName,"+a") as file:
        requestString = f"{requestID};{userID};{fullName};{subjectCode};{amount};PENDING;\n"
        file.write(requestString)
        return True

def deleteIfStatus(fileName, requestID, status):
    updatedLines = []
    deleted = False
    capitalizedStatus = str(status).upper()
    with open(fileName, "+r") as file:
        lines = file.readlines()

    for line in lines:
        values = line.strip().split(";")
        if values[0] == requestID and values[5] == capitalizedStatus:
            deleted = True
            continue
        else:
            updatedLines.append(line)

    with open(fileName,"w+") as file:
        file.writelines(updatedLines)

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
        with open("UserDetails.txt", "+r") as file:
            for line in file:
                values = line.strip().split(";")
                if values[1] == userID:
                    subjectAssigned = eval(values[11])
        # Print subjectCodeList after the loop
        print(f"Classes assigned: {subjectAssigned}")
        generalUtils.createNewLine()
        print("1. View Class Schedule\n2. Subject Requests\n3. Payment Request\n4. Update Profile\n5. View profile\n6. Log Out")
        generalUtils.createNewLine()
        choice = input("Choice: ")
        if choice == "1":
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("View Class Schedule")
            generalUtils.createNewLine()
            for subject in subjectAssigned:
                with open("ClassInfo.txt", "+r") as file:
                    lines = file.readlines()
                for line in lines:
                    values = line.strip().split(";")
                    subjectForm = values[2].replace("_"," ")
                    if values[0] == subject:
                        print(f"Subject Code: {subject}\nSubject Name: {values[1]}\nSubject Form: {subjectForm}\nDay: {values[3]}\nTime: {values[4]}\nLocation: {values[5]}")
                        generalUtils.createNewLine()
            while True:
                classScheduleView = input("Are you done with viewing(Y/N)? ").upper()
                if classScheduleView == "Y":
                    break
                else:
                    continue
        elif choice == "2":
            while True:
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Subject change request")
                generalUtils.createNewLine()
                print("1. Send a request\n2. Delete a request\n3. View a request\n4. Exit")
                generalUtils.createNewLine()
                choiceRequest = input("Choice: ")
                if choiceRequest == "1":
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("Send a request")
                    generalUtils.createNewLine()
                    # requestID
                    existingIDs = UniqueIDCreation.readIDFromExistingFile("StudentRequest.txt",0)
                    requestID = UniqueIDCreation.generateRequestID(existingIDs)
                    with open("UserDetails.txt", "+r") as file:
                        for line in file:
                            values = line.strip().split(";")
                            if values[1] == userID:
                                fullName = values[4]
                                formattedName = fullName.replace("_", " ")
                    print(f"Current Subjects: {subjectAssigned}")
                    generalUtils.createNewLine()
                    while True:
                        currentSubject = input("Current Subject: ")
                        if currentSubject in subjectAssigned:
                            break
                        else:
                            print("\nYou are currently not taking the subject")
                            time.sleep(2)
                            print("\n")
                            continue
                    while True:
                        requestedSubject = input("\nRequested Subject: ")
                        if requestedSubject in subjectAssigned:
                            print("\nYou are already taking the subject")
                            time.sleep(2)
                            print("\n")
                            continue
                        else:
                            break
                    generalUtils.createNewLine()
                    print(f"Request ID: {requestID}\nStudent ID: {userID}\nFull Name: {formattedName}\nCurrent Subject: {currentSubject}\nReuqested Subject: {requestedSubject}")
                    generalUtils.createNewLine()
                    while True:
                        confirmationChoice = input("Is this correct (Y/N)?").upper()
                        if confirmationChoice == "Y":
                            writeSubjectRequest(requestID,userID,fullName,currentSubject,requestedSubject,"StudentRequest.txt")
                            print("\nSubject Request Sent")
                            time.sleep(3)
                            break
                        elif confirmationChoice == "N":
                            print("\nSubject Request Not Sent")
                            time.sleep(3)
                            break
                        else: 
                            continue
                    generalUtils.createNewLine()
                    generalUtils.clearConsole()
                    break
                elif choiceRequest == "2":
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("Delete a subject change request")
                    generalUtils.createNewLine()
                    with open("StudentRequest.txt","r+") as file:
                        requestList = []
                        lines = file.readlines()

                        for line in lines:
                            values = line.strip().split(";")
                            if values[1] == userID:
                                requestList.append(values[0])
                            else:
                                continue
                    print(f"Request List: {requestList}")
                    generalUtils.createNewLine()
                    while True:
                        print("1. Delete request\n2. Exit")
                        generalUtils.createNewLine()
                        deleteSubjectRequestChoice = input("Choice")
                        if deleteSubjectRequestChoice == "1":
                            while True:
                                deleteRequestID = input("Request ID: ")
                                if deleteRequestID in requestList:
                                    break
                                else:
                                    print("\nError: Payment Request ID not found")
                                    time.sleep(2)
                                    continue
                            generalUtils.createNewLine()
                            while True:
                                confirmationChoice = input("Confirm(Y/N)? ").upper()
                                if confirmationChoice == "Y":
                                    if deleteIfStatus("StudentRequest.txt", deleteRequestID,"PENDING") == True:
                                        print("\nSubject change request has been deleted")
                                        time.sleep(3)
                                    else: 
                                        print("Subject Request has not deleted (Subject Request has either been approved or rejected)")
                                        time.sleep(3)
                                elif confirmationChoice == "N":
                                    print("\nSubject change request not deleted")
                                    break
                                generalUtils.createNewLine()
                                generalUtils.clearConsole()
                                break
                            break
                        elif deleteSubjectRequestChoice == "2":
                            break
                        else:
                            continue
                elif choiceRequest == "3":
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("View Student Request")
                    generalUtils.createNewLine()
                    with open("StudentRequest.txt","r+") as file:
                        requestList = []
                        lines = file.readlines()

                        for line in lines:
                            values = line.strip().split(";")
                            if values[1] == userID:
                                requestList.append(values[0])
                            else:
                                continue
                    print(f"Request List: {requestList}")
                    generalUtils.createNewLine()
                    while True:
                        print("1. View Request\n2. Exit")
                        generalUtils.createNewLine()
                        viewStudentRequest = input("Choice: ")
                        if viewStudentRequest == "1":
                            while True:
                                viewRequestID = input("Request ID: ").upper()
                                if viewRequestID in requestList:
                                    break
                                if viewRequestID == "EXIT":
                                    break
                                else:
                                    print("\nError: Payment Request ID not found")
                                    time.sleep(2)
                                    continue
                            with open ("StudentRequest.txt", "+r") as file:
                                lines = file.readlines()
                            for line in lines:
                                values = line.strip().split(";")
                                if values[0] == viewRequestID:
                                    generalUtils.createNewLine()
                                    print(f"Request ID: {viewRequestID}\nStudent ID: {values[1]}\nStudent Name: {values[2].replace('_',' ')}\nCurrent Subject: {values[3]}\nRequested Subject: {values[4]}\nStatus: {values[5]}")
                                    if values[5] == "APPROVED":
                                        deleteIfStatus("StudentRequest.txt", viewRequestID, "APPROVED")
                                    elif values[5] == "REJECTED":
                                        deleteIfStatus("StudentRequest.txt", viewRequestID, "REJECTED")
                                    generalUtils.createNewLine()
                                    while True:
                                        doneViewingChoice = input("Done Viewing(Y/N)?").upper()
                                        if doneViewingChoice == "Y":
                                            break
                                        else:
                                            continue
                            generalUtils.createNewLine()
                            break
                        elif viewStudentRequest == "2":
                            break
                        else:
                            continue
                elif choiceRequest == "4":
                    break
                else: 
                    continue       
        elif choice == "3":
            while True:
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Payment request")
                generalUtils.createNewLine()
                print("1. Send a request\n2. Delete a request\n3. View a request\n4. Exit")
                generalUtils.createNewLine()
                choiceRequest = input("Choice: ")
                if choiceRequest == "1":
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("Send a request")
                    generalUtils.createNewLine()
                    existingIDs = UniqueIDCreation.readIDFromExistingFile("PaymentRequest.txt",0)
                    paymentID = UniqueIDCreation.generatePaymentID(existingIDs)
                    print(f"Subject Enrolled: {subjectAssigned}")
                    generalUtils.createNewLine()
                    while True:
                        subjectCode = input("Subject Code: ")
                        if subjectCode in subjectAssigned:
                            break
                        else:
                            print("\nInvalid subject code")
                            print("\n")
                            continue
                    subjectFee = database.readListValue(subjectCode, 0, 2, "SubjectsInfo.txt").replace("_"," ")
                    print(f"Amount that should be paid: {subjectFee}")
                    # might want to optimize this part
                    amount = int(input("Amount paid: "))
                    generalUtils.createNewLine()
                    print(f"Payment ID: {paymentID}\nAmount of payment: {amount}")
                    generalUtils.createNewLine()
                    while True:
                        paymentChoice = input("Is this correct(Y/N)? ").upper()
                        if paymentChoice == "Y":
                            formattedName = database.readListValue(userID, 1, 4, "UserDetails.txt")
                            if writePaymentRequest(paymentID, userID, formattedName, subjectCode, amount, "PaymentRequest.txt") == True:
                                print("\nPayment Request submitted")
                                time.sleep(3)
                                break
                            else:
                                print("\nPayment Request not submitted")
                                time.sleep(3)
                                break
                        elif paymentChoice == "N":
                            print("Payment request not sent")
                            time.sleep(3)
                            break
                        else:
                            continue
                elif choiceRequest == "2":
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("Delete a payment request")
                    generalUtils.createNewLine()
                    with open("PaymentRequest.txt","r+") as file:
                        requestList = []
                        lines = file.readlines()

                        for line in lines:
                            values = line.strip().split(";")
                            if values[1] == userID:
                                requestList.append(values[0])
                            else:
                                continue
                    print(f"Request List: {requestList}")
                    generalUtils.createNewLine()
                    while True:
                        print("1. Delete Request\n2. Exit")
                        deletePaymentChoice = input("Choice: ")
                        if deletePaymentChoice == "1":
                            while True:
                                deleteRequestID = input("Payment ID: ")
                                if deleteRequestID in requestList:
                                    break
                                else:
                                    print("\nError: Payment Request ID not found")
                                    time.sleep(2)
                                    continue
                            generalUtils.createNewLine()
                            paymentChoice = input("\nConfirm(Y/N)? ").upper()
                            if paymentChoice == "Y":    
                                if deleteIfStatus("PaymentRequest.txt", deleteRequestID,"PENDING") == True:
                                        print("\nPayment request has been deleted")
                                        time.sleep(3)
                                else: 
                                    print("\nPayment request is not deleted (Payment request have either been approved or rejected)")
                                    time.sleep(3)
                            elif paymentChoice == "N":
                                print("\nPayment request not deleted")
                                break
                            else:
                                continue
                            break
                        elif deletePaymentChoice == "2":
                            break
                        else:
                            continue
                elif choiceRequest == "3":
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    requestIDNotFound = True
                    print("View a Payment Request")
                    generalUtils.createNewLine()
                    with open("PaymentRequest.txt","r+") as file:
                        requestList = []
                        lines = file.readlines()

                        for line in lines:
                            values = line.strip().split(";")
                            if values[1] == userID:
                                requestList.append(values[0])
                            else:
                                continue
                    print(f"Request List: {requestList}")
                    generalUtils.createNewLine()
                    while True:
                        print("1. View Payment Request\n2. Exit")
                        generalUtils.createNewLine()
                        viewPaymentRequestChoice = input("Choice: ")
                        if viewPaymentRequestChoice == "1":
                            while True:
                                viewRequestID = input("Request ID: ").upper()
                                if viewRequestID in requestList:
                                    break
                                else:
                                    print("\nError: Payment Request ID not found")
                                    time.sleep(2)
                                    continue
                            with open ("PaymentRequest.txt", "+r") as file:
                                lines = file.readlines()
                            for line in lines:
                                values = line.strip().split(";")
                                if values[0] == viewRequestID:
                                    requestIDNotFound = False
                                    generalUtils.clearConsole()
                                    generalUtils.createNewLine()
                                    print(f"Request ID: {viewRequestID}\nStudent ID: {values[1]}\nStudent Name: {values[2].replace('_',' ')}\nSubject Code: {values[3]}\nAmount Paid: {values[4]}\nStatus: {values[5]}")
                                    generalUtils.createNewLine()
                                    if values[5] == "APPROVED":
                                        viewReceipt = input("View Receipt(Y/N)? ").upper()
                                        if viewReceipt == "Y":
                                            generalUtils.createNewLine()
                                            receiptID = database.readListValue(viewRequestID, 0, 6, "PaymentRequest.txt")
                                            studentIDReceipt = database.readListValue(receiptID, 0, 1, "ReceiptCollection.txt")
                                            studentNameReceipt = database.readListValue(receiptID, 0, 2, "ReceiptCollection.txt")
                                            subjectCodeReceipt = database.readListValue(receiptID, 0, 3, "ReceiptCollection.txt")
                                            amountReceipt = database.readListValue(receiptID, 0, 4, "ReceiptCollection.txt")
                                            print(f"Receipt ID: {receiptID}\nStudent ID: {studentIDReceipt}\nStudent Name: {studentNameReceipt.replace('_',' ')}\nSubject Code: {subjectCodeReceipt}\nAmount: {amountReceipt}")
                                            generalUtils.createNewLine()
                                            doneViewReceipt = input("Are you done with viewing(Y/N)? ").upper()
                                            if doneViewReceipt == "Y":
                                                deleteIfStatus("PaymentRequest.txt", viewRequestID, "APPROVED")
                                                print("\nReceipt received")
                                                time.sleep(3)
                                                break
                                            else:
                                                continue
                                    elif values[5] == "REJECTED":
                                        doneViewingChoice = input("Are you done with viewing(Y/N)? ").upper()
                                        if doneViewingChoice == "Y":
                                            deleteIfStatus("PaymentRequest.txt", viewRequestID, "REJECTED")
                                            break
                                        else:
                                            continue
                                    while True:
                                        doneViewingChoice = input("Are you done with viewing(Y/N)? ").upper()
                                        if doneViewingChoice == "Y":
                                            break
                                        else:
                                            continue
                            if requestIDNotFound:
                                print("\nRequest ID Not Found")
                                break
                            break
                        elif viewPaymentRequestChoice == "2":
                            break
                        else:
                            continue
                elif choiceRequest == "4":
                    break
                else: 
                    continue
        elif choice == "4":
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("Update Profile")
            generalUtils.createNewLine()
            print("1. Update Profile\n2. Exit")
            generalUtils.createNewLine()
            updateChoice = input("Choice: ")
            if updateChoice == "1":
                password = input("Password: ")
                ICNumber = int(input("\nIC Number: "))
                fullName = input("\nFull name: ")
                formattedName = fullName.replace(" ","_")
                email = input("\nEmail: ")
                phoneNumber = int(input("\nPhone Number: "))
                generalUtils.createNewLine()
                while True: 
                    print("Gender")
                    generalUtils.createNewLine()
                    print("1. Male\n2. Female\n3. N/A")
                    generalUtils.createNewLine()
                    gender = input("Choice: ").upper()
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
                print(f"Profile\n\nID Number: {userID}\nPassword: {password}\nIC Number: {ICNumber}\nFull Name: {fullName}\nEmail: {email}\nPhone Number: {phoneNumber}\nGender: {gender}\nBirthday: {birthday}")
                generalUtils.createNewLine()
                while True:
                    confirmationChoice = input("Is this correct? Y/N ").upper()
                    if confirmationChoice == "Y":
                        subject = subjectAssigned[0]
                        numberOfSubjects = len(subjectAssigned)
                        studentForm = f"Form_{subject[:-1]}"
                        if updateStudentProfile("UserDetails.txt", userID, "STUDENT",password,ICNumber,formattedName,email,phoneNumber,birthday,gender,subjectAssigned, numberOfSubjects, studentForm) == True:
                            print("\nProfile Updated")
                            time.sleep(3)
                            break
                    elif confirmationChoice == "N":
                        print("\nProfile not updated")
                        time.sleep(3)
                        break
                    else:
                        print("Invalid Input!\n")
                    time.sleep(3)
            elif updateChoice == "2":
                break
            else:
                continue
        elif choice == "5":
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("View Profile")
            generalUtils.createNewLine()
            ICNumber = database.readListValue(userID, 1, 3, "UserDetails.txt")
            fullName = database.readListValue(userID, 1, 4, "UserDetails.txt").replace("_"," ")
            email = database.readListValue(userID, 1, 5, "UserDetails.txt")
            phoneNumber = database.readListValue(userID, 1, 6, "UserDetails.txt")
            gender = database.readListValue(userID, 1, 7, "UserDetails.txt")
            birthday = database.readListValue(userID, 1, 8, "UserDetails.txt")
            print(f"User ID: {userID}\nIC Number: {ICNumber}\nFull Name: {fullName}\nEmail: {email}\nPhone Number: {phoneNumber}\nGender: {gender}\nBirthday: {birthday}")
            generalUtils.createNewLine()
            while True:
                print("Done Viewing(Enter Y when you are done)? ")
                generalUtils.createNewLine()
                doneViewing = input("Choice: ").upper()
                if doneViewing == "Y":
                    break
                else:
                    continue
        elif choice == "6":
            print("Log Out")
            return "LOGOUT"
        else:
            continue
