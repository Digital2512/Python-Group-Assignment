import database
import generalUtils  
import time
import random
import UniqueIDCreation

def changeSubjectIncome(subjectCode, indexToCheck, indexToChange, changedAmount, fileToCheck):

    # Read the content of the file
    with open(fileToCheck, 'r') as file:
        lines = file.readlines()

    # Find the line with the specified subject code and update the value
    for i, line in enumerate(lines):
        if line.startswith(subjectCode):
            parts = line.split(';')
            # Check if the value is not None before converting to int
            if parts[2] is not None:
                parts[2] = str(changedAmount)
            else:
                # Handle the case where the value is None, for example, set it to 0
                parts[2] = '0'
            lines[i] = ';'.join(parts)
            break

    # Write the modified content back to the file
    with open(fileToCheck, 'w') as file:
        file.writelines(lines)

def updateProfile(fileToCheck, IDNumber, role, password, ICNumber, fullName, email, phoneNumber, birthday, gender):
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
        updated_data.append(f"{capitalizedRole};{IDNumber};{password};{ICNumber};{fullName};{email};{phoneNumber};{gender};{birthday}\n")

    # Write the updated data back to the file
        with open(fileToCheck, "+w") as file:
            file.writelines(updated_data)
    return updatedProfile

def deleteProfile(fileToCheck, IDNumber, role):
    deleted = False
    capitalizedRole = role.upper()
    with open(fileToCheck,"r") as file:
        lines = file.readlines()
    with open(fileToCheck,"w") as file:
        for line in lines:
            values = line.strip().split(";") 
            if values[1] == IDNumber and values[0] == capitalizedRole:
                deleted = True
                continue
            file.write(line)
    return deleted

def deleteRequest(fileToCheck, requestID):
    deleted = False
    with open(fileToCheck, "r") as file:
        lines = file.readlines()
    with open(fileToCheck,"w") as file:
        for line in lines:
            values = line.strip().split(";")
            if values[0] == requestID:
                deleted = True
                continue
            file.write(line)
        return deleted

def changedSubjects(fileName, studentID, currentSubject,requestedSubject):
    subjectChanged = False
    update_lines = []
    
    with open(fileName, "+r") as file:
        lines = file.readlines()
    
    for i in range(len(lines)): 
        values = lines[i].strip().split(";")
        if values[1] == studentID:
            for j in range(len(values)):
                if values[j] == currentSubject:
                    values[j] = requestedSubject
                    subjectChanged = True
            lines[i] = ";".join(values)+"\n"
        update_lines.append(lines[i])
    
    if subjectChanged:
        with open(fileName,"+w") as file:
            file.writelines(update_lines)
            return True
    else:
        return "Error: Student ID Not Found"            

def checkForValue(fileName, valueInput, indexToCheck):
    with open(fileName, "+r") as file:
        for line in file:
            values = line.strip().split(";")
            if values[indexToCheck] == valueInput:
                return True
        return False

def pgReceptionist(userID):
    duplicateFound = False
    subjectsChosen = []
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
        print("1. Register Student\n2. Delete Students\n3. Update Profile\n4. Student Request\n5. Payments Requests\n6. View Profile\n7. Log Out")
        generalUtils.createNewLine()
        choice1 = int(input("Choice: "))
        if choice1 == 1:
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            subjectsChosen = []
            print("Register Student")
            generalUtils.createNewLine()
            while True:
                existingIDList = UniqueIDCreation.readIDFromExistingFile("UserDetails.txt", 1)
                studentIDNumber = UniqueIDCreation.generateStudentID(existingIDList)
                duplicateFound = UniqueIDCreation.checkForDuplication(existingIDList, studentIDNumber)
                if duplicateFound:
                    continue
                else:
                    break
            print(f"Student ID: {studentIDNumber}")
            password = input("\nPassword: ")
            name = input("\nFull Name: ")
            connectedName = name.replace(" ","_")
            while True:
                formChoice = int(input("Students Form \n1. Form 1\n2. Form 2\n3. Form 3\n4. Form 4\n5. Form 5\nChoice: "))
                generalUtils.createNewLine()
                if formChoice == 1:
                    form = "Form 1"
                    while len(subjectsChosen) < 3:
                        generalUtils.createNewLine()
                        print("Choose the subjects: \n\nChinese\nEnglish\nMalay\nMathemathics\nAdditional Mathemathics\nGeneral Commerce\nGeneral Science")
                        generalUtils.createNewLine()
                        subject = input("Choice: ").upper().replace(" ", "_")
                        if subject in ["CHINESE", "ENGLISH", "MALAY", "MATHEMATHICS", "ADDITONAL_MATHEMATHICS", "GENERAL_COMMERCE", "GENERAL_SCIENCE"]:
                            subjectsChosen.append(subject)
                        else: 
                            print("Error: Invalid Input(Please choose from the availale subject list)")
                            continue
                    print(subjectsChosen)
                elif formChoice == 2:
                    form = "Form 2"
                    subjectsChosen = []
                    while len(subjectsChosen) < 3:
                        generalUtils.createNewLine()
                        print("Choose the subjects: \n\nChinese\nEnglish\nMalay\nMathemathics\nAdditional Mathemathics\nGeneral Commerce\nGeneral Science")
                        generalUtils.createNewLine()
                        subject = input("Choice: ").upper().replace(" ", "_")
                        if subject in ["CHINESE", "ENGLISH", "MALAY", "MATHEMATHICS", "ADDITONAL_MATHEMATHICS", "GENERAL_COMMERCE", "GENERAL_SCIENCE"]:
                            subjectsChosen.append(subject)
                        else: 
                            print("Error: Invalid Input(Please choose from the availale subject list)")
                            continue
                        print(subjectsChosen)
                elif formChoice == 3:
                    form = "Form 3"
                    subjectsChosen = []
                    while len(subjectsChosen) < 3:
                        generalUtils.createNewLine()
                        print("Choose the subjects: \n\nChinese\nEnglish\nMalay\nMathemathics\nAdditional Mathemathics\nGeneral Commerce\nGeneral Science")
                        generalUtils.createNewLine()
                        subject = input("Choice: ").upper().replace(" ", "_")
                        if subject in ["CHINESE", "ENGLISH", "MALAY", "MATHEMATHICS", "ADDITONAL_MATHEMATHICS", "GENERAL COMMERCE", "GENERAL SCIENCE"]:
                            subjectsChosen.append(subject)
                        else: 
                            print("Error: Invalid Input(Please choose from the availale subject list)")
                            continue
                        print(subjectsChosen)
                elif formChoice == 4:
                    form = "Form 4"
                    while len(subjectsChosen) < 3:
                        generalUtils.createNewLine()
                        print("Choose the subjects: \n\nChinese\nEnglish\nMalay\nMathemathics\nAdditional Mathemathics\nAccounting\nEconomics\nBusiness Studies\nPhysics\nChemistry\nBiology")
                        generalUtils.createNewLine()
                        subject = input("Choice: ").upper().replace(" ", "_")
                        if subject in ["CHINESE", "ENGLISH", "MALAY", "MATHEMATHICS", "ADDITONAL_MATHEMATHICS", "ACCOUNTING", "ECONOMICS", "BUSINESS STUDIES", "PHYSICS", "CHEMISTRY", "BIOLOGY"]:
                            subjectsChosen.append(subject)
                        else: 
                            print("Error: Invalid Input(Please choose from the availale subject list)")
                            continue
                        print(subjectsChosen)
                elif formChoice == 5:
                    form = "Form 5"
                    subjectChosen = 0
                    while len(subjectsChosen) < 3:
                        generalUtils.createNewLine()
                        print("Choose the subjects: \n\nChinese\nEnglish\nMalay\nMathemathics\nAdditional Mathemathics\nAccounting\nEconomics\nBusiness Studies\nPhysics\nChemistry\nBiology")
                        generalUtils.createNewLine()
                        subject = input("Choice: ").upper().replace(" ", "_")
                        if subject in ["CHINESE", "ENGLISH", "MALAY", "MATHEMATHICS", "ADDITONAL_MATHEMATHICS", "ACCOUNTING", "ECONOMICS", "BUSINESS STUDIES", "PHYSICS", "CHEMISTRY", "BIOLOGY"]:
                            subjectsChosen.append(subject)
                        else: 
                            print("Error: Invalid Input(Please choose from the availale subject list)")
                            continue
                        print(subjectsChosen)
                else: 
                    continue

                subject1 = subjectsChosen[0]
                subject2 = subjectsChosen[1]
                subject3 = subjectsChosen[2]

                subjectsChosen = []
                studentDetails = f"STUDENT;{studentIDNumber};{password};{connectedName};{form};{subject1};{subject2};{subject3}\n"
                database.writeToFile("UserDetails.txt", studentDetails)
                print("New student registered")
                time.sleep(2)
                break
        elif choice1 == 2:
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("Delete Student")
            generalUtils.createNewLine()
            searchStudentID = input("Search Student's ID: ")
            generalUtils.createNewLine()
            if deleteProfile("UserDetails.txt", searchStudentID, "STUDENT") == True:
                print("Student has been deleted")
                time.sleep(2)
            else:
                print("Error: Student has not been deleted or wrong ID")
                time.sleep(2)
        elif choice1 == 3:
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
        elif choice1 == 4:
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("Student Request")
            generalUtils.createNewLine()
            requestID = input("Request ID: ")
            generalUtils.createNewLine()
            if checkForValue("StudentRequest.txt", requestID, 0) == True: 
                generalUtils.createNewLine()   
                studentID = database.readListValue(requestID, 0, 1, "StudentRequest.txt")
                print(f"Student ID: {studentID}\n")
                name = database.readListValue(studentID, 1, 2, "StudentRequest.txt")
                spacedName = name.replace("_", " ")
                print(f"Full Name: {spacedName}")
                currentSubject = database.readListValue(requestID, 0, 3, "StudentRequest.txt")
                requestedSubject = database.readListValue(requestID, 0, 4, "StudentRequest.txt")
                deleteRequest("StudentRequest.txt", requestID)
                generalUtils.createNewLine()
                formattedCurrentSubject = currentSubject.upper().replace("_"," ")
                formattedRequestedSubject = requestedSubject.upper().replace("_"," ")
                print(f"Current Subject: {currentSubject}\n")
                print(f"Requested Subject: {requestedSubject}")
                generalUtils.createNewLine()
                while True:
                    approval = input("Y/N? ").upper()
                    if approval == "Y":
                        if changedSubjects("UserDetails.txt", studentID, formattedCurrentSubject, formattedRequestedSubject) == True:
                            print("Request Approved(Subject Changed)")
                            generalUtils.createNewLine()
                            time.sleep(3)
                            break
                        else: 
                            print("Error: Subject did not change")
                            generalUtils.createNewLine()
                            time.sleep(3)
                            break
                    elif approval == "N":
                        print("Request Rejected")
                        generalUtils.createNewLine()
                        time.sleep(3)
                        break
                    else:
                        continue
            else: 
                print("Error: No request found")
                generalUtils.createNewLine()
                time.sleep(3)
        elif choice1 == 5:
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("Payment Request")
            generalUtils.createNewLine()
            paymentID = input("Payment ID: ")
            generalUtils.createNewLine()
            if checkForValue("PaymentRequest.txt", paymentID, 0) == True:
                userID = database.readListValue(paymentID, 0, 1, "PaymentRequest.txt")
                fullName = database.readListValue(paymentID, 0, 2, "PaymentRequest.txt")
                amount = database.readListValue(paymentID, 0, 3, "PaymentRequest.txt")
                subjectCode = database.readListValue(paymentID, 0, 4, "PaymentRequest.txt")
                subject = database.readListValue(paymentID, 0, 5, "PaymentRequest.txt")
                form = database.readListValue(paymentID, 0, 6, "PaymentRequest.txt")
                print(f"User ID: {userID}\nFull name: {fullName}\nAmount: {amount}\nSubject Code: {subjectCode}\nSubject: {subject}\nForm: {form}")
                generalUtils.createNewLine()
                print("Print Receipt? Y/N")
                receiptConfimation = input("Choice: ").upper()
                while True:
                    if receiptConfimation == "Y":
                        existingIDs = UniqueIDCreation.readIDFromExistingFile("ReceiptCollection.txt",0)
                        receiptID = random.randint(1,1000000000)
                        while UniqueIDCreation.checkForDuplication(existingIDs, receiptID):
                            receiptID = random.randint(1,1000000000)
                        generalUtils.clearConsole()
                        formatedID = f"{receiptID:09d}"
                        status = "APPROVED"
                        generalUtils.createNewLine()
                        receiptString = f"Receipt ID: {formatedID}\nUser ID: {userID}\nFull name: {fullName}\nAmount: {amount}\nSubject: {subject}\nStatus: {status}"
                        print(receiptString)
                        generalUtils.createNewLine()
                        beforeAmount = database.readListValue(subjectCode, 0, 2, "SubjectInfo.txt")
                        if beforeAmount == None: 
                            beforeAmount = 0
                        addedAmount = database.readListValue(paymentID,0,3,"PaymentRequest.txt")
                        afterAmount = int(beforeAmount) + int(addedAmount)
                        print(subjectCode)
            
                        print(afterAmount)
                        changeSubjectIncome(subjectCode,0,2,afterAmount,"SubjectInfo.txt")
                        fileReceiptString = f"{formatedID};{userID};{fullName};{amount};{subject};{status}\n"
                        database.writeToFile("ReceiptCollection.txt", fileReceiptString)
                        while True: 
                            receiptDone = input("Done(Only enter Y when you are done)? ")
                            if receiptDone == "Y":
                                break
                            else:
                                continue
                        deleteRequest("PaymentRequest.txt", paymentID)
                        break
                    elif receiptConfimation == "N": 
                        print("Receipt Rejected")
                        status = "REJECTED"
                        fileReceiptString = f"{formatedID};{userID};{fullName};{amount};{subject};{status}\n"
                        database.writeToFile("ReceiptCollection.txt", fileReceiptString)

                        deleteRequest("PaymentRequest.txt", paymentID)
                        time.sleep(3)
                        break
                    else:
                        continue
        elif choice1 == 6:
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
                    

        elif choice1 == 7:
            print("Logging out")
            return "LOGOUT"
        else:
            continue