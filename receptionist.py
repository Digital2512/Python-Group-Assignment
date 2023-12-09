import database
import generalUtils  
import time
import UniqueIDCreation
import ast

def updateReceptionistProfile(fileToCheck, IDNumber, role, password, ICNumber, fullName, email, phoneNumber, birthday, gender):
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

def changedSubjects(fileName, studentID, currentSubject, requestedSubject):
    subjectChanged = False
    update_lines = []

    with open(fileName, "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        values = lines[i].strip().split(";")
        if values[1] == studentID:
            subjectList = eval(values[11])
            for j in range(len(subjectList)):
                if subjectList[j] == currentSubject:
                    subjectList[j] = requestedSubject
                    subjectChanged = True
            values[11] = str(subjectList)
            lines[i] = ";".join(values) + "\n"
        update_lines.append(lines[i])

    if subjectChanged:
        with open(fileName, "w") as file:
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
    
def approvePayment(fileName, paymentID, studentID, studentName, subject, amount,receiptID):
    approvedPayment = False
    updatedLines = []
    receiptString = f"{paymentID};{studentID};{studentName};{subject};{amount};APPROVED;{receiptID}\n"
    with open(fileName, "r+") as file:
        lines = file.readlines()
    # {receiptID};{studentID};{studentName};{subject};{amount};{state}
    for line in lines:
        values = line.strip().split(";")
        if values[0] == paymentID:
            approvedPayment = True
            continue
        else:
            updatedLines.append(line)
    
    if approvedPayment:
        updatedLines.append(receiptString)

    with open(fileName, "w+") as file:
        file.writelines(updatedLines)
    return approvedPayment

def rejectPayment(fileName, paymentID, studentID, studentName, subject, amount):
    rejectedPayment = True
    updatedLines = []
    receiptString = f"{paymentID};{studentID};{studentName};{subject};{amount};REJECTED;\n"
    with open(fileName, "r+") as file:
        lines = file.readlines()
    # {receiptID};{studentID};{studentName};{subject};{amount};{state}
    for line in lines:
        values = line.strip().split(";")
        if values[0] == paymentID:
            rejectedPayment = True
            continue
        else:
            updatedLines.append(line)
    
    if rejectedPayment:
        updatedLines.append(receiptString)

    with open(fileName, "w+") as file:
        file.writelines(updatedLines)
    return rejectedPayment


def updateSubjectIncome(fileName, subjectCode, amount):
    updatedLines = []
    incomeUpdated = False
    with open(fileName, "r+") as file:
        lines = file.readlines()
        file.seek(0)  # Move the cursor to the beginning of the file

        for line in lines:
            values = line.strip().split(";")
            if values[0] == subjectCode:
                incomeUpdated = True
                values[3] = str(int(values[3]) + int(amount))
                updatedLines.append(";".join(values) + "\n")
            else:
                updatedLines.append(line)

        file.writelines(updatedLines)
        file.truncate()  # Remove any remaining content after the updated lines

    return incomeUpdated



def approveSubjectChange(fileName, requestID, studentID, studentName, currentSubject, requestedSubject):
    approvedSubjectChanged = False
    updatedLines = []
    receiptString = f"{requestID};{studentID};{studentName};{currentSubject};{requestedSubject};APPROVED;\n"
    with open(fileName, "+r") as file:
        lines = file.readlines()
    # {receiptID};{studentID};{studentName};{subject};{amount};{state}
    for line in lines:
        values = line.strip().split(";")
        if values[0] == requestID:
            approvedSubjectChanged = True
            continue
        else:
            updatedLines.append(line)
    
    if approvedSubjectChanged:
        updatedLines.append(receiptString)

    with open(fileName, "+w") as file:
        file.writelines(updatedLines)
    return approvedSubjectChanged

def rejectSubjectChange(fileName, requestID, studentID, studentName, currentSubject, requestedSubject,):
    rejectedSubjectChange = True
    updatedLines = []
    receiptString = f"{requestID};{studentID};{studentName};{currentSubject};{requestedSubject};REJECTED;\n"
    with open(fileName, "+r") as file:
        lines = file.readlines()
    # {receiptID};{studentID};{studentName};{subject};{amount};{state}
    for line in lines:
        values = line.strip().split(";")
        if values[0] == requestID:
            rejectedSubjectChange = True
            continue
        else:
            updatedLines.append(line)
    
    if rejectedSubjectChange:
        updatedLines.append(receiptString)

    with open(fileName, "+w") as file:
        file.writelines(updatedLines)
    return rejectedSubjectChange

def approveSubjectChange(fileName, requestID, studentID, studentName, currentSubject, requestedSubject):
    approvedSubjectChanged = False
    updatedLines = []
    receiptString = f"{requestID};{studentID};{studentName};{currentSubject};{requestedSubject};APPROVED;\n"
    with open(fileName, "+r") as file:
        lines = file.readlines()
    # {receiptID};{studentID};{studentName};{subject};{amount};{state}
    for line in lines:
        values = line.strip().split(";")
        if values[0] == requestID:
            approvedSubjectChanged = True
            continue
        else:
            updatedLines.append(line)
    
    if approvedSubjectChanged:
        updatedLines.append(receiptString)

    with open(fileName, "+w") as file:
        file.writelines(updatedLines)
    return approvedSubjectChanged

def rejectSubjectChange(fileName, requestID, studentID, studentName, currentSubject, requestedSubject,):
    rejectedSubjectChange = True
    updatedLines = []
    receiptString = f"{requestID};{studentID};{studentName};{currentSubject};{requestedSubject};REJECTED;\n"
    with open(fileName, "+r") as file:
        lines = file.readlines()
    # {receiptID};{studentID};{studentName};{subject};{amount};{state}
    for line in lines:
        values = line.strip().split(";")
        if values[0] == requestID:
            rejectedSubjectChange = True
            continue
        else:
            updatedLines.append(line)
    
    if rejectedSubjectChange:
        updatedLines.append(receiptString)

    with open(fileName, "+w") as file:
        file.writelines(updatedLines)
    return rejectedSubjectChange

def updateStudentList(fileName, subjectCode, studentName):
    updatedStudentList = False
    updatedLines = []

    with open(fileName, "r+") as file:
        lines = file.readlines()

        for line in lines:
            values = line.strip().split(";")
            if values[0] == subjectCode:
                updatedStudentList = True
                studentList = ast.literal_eval(values[4])
                studentList.append(studentName)
                values[4] = studentList
                updatedLines.append(";".join(values[:4] + [str(values[4])] + values[5:]) + "\n")
            else:
                updatedLines.append(line)

        file.seek(0)
        file.truncate()
        file.writelines(updatedLines)

    return updatedStudentList

def deleteStudentList(fileName, subjectCode, studentName):
    updatedStudentList = False
    updatedLines = []

    with open(fileName, "r+") as file:
        lines = file.readlines()

        for line in lines:
            values = line.strip().split(";")
            if values[0] == subjectCode:
                updatedStudentList = True
                studentList = ast.literal_eval(values[4])
                if studentName in studentList:
                    studentList.remove(studentName)
                    values[4] = str(studentList)
                updatedLines.append(";".join(values) + "\n")
            else:
                updatedLines.append(line)

        file.seek(0)
        file.truncate()
        file.writelines(updatedLines)

    return updatedStudentList

def pgReceptionist(userID):
    subjectsF1 = ["ENF1", "CHF1", "MAF1", "MTHF1", "AMTHF1", "GCF1", "GSF1"]
    subjectsF2 = ["ENF2", "CHF2", "MAF2", "MTHF2", "AMTHF2", "GCF2", "GSF2"]
    subjectsF3 = ["ENF3", "CHF3", "MAF3", "MTHF3", "AMTHF3", "GCF3", "GSF3"]
    subjectsF4 = ["ENF4", "CHF4", "MAF4", "MTHF4", "AMTHF4", "ACF4", "ECF4", "BSF4", "PHF4", "CHMF4", "BIOF4"]
    subjectsF5 = ["ENF5", "CHF5", "MAF5", "MTHF5", "AMTHF5", "ACF5", "ECF5", "BSF5", "PHF5", "CHMF5", "BIOF5"]
    while True:
        generalUtils.clearConsole()
        generalUtils.createNewLine()
        with open("UserDetails.txt", "r+") as file:
            for line in file:
                values = line.strip().split(";")
                if values[1] == userID:
                    splittedName = values[4].replace("_"," ")
                    print(f"Welcome, {splittedName} ({values[0]})")
        generalUtils.createNewLine()
        print("1. Register Student\n2. Delete Students\n3. Student Request\n4. Update Profile\n5. View Profile\n6. Log Out")
        generalUtils.createNewLine()
        choice1 = input("Choice: ")
        if choice1 == "1":
            while True:
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                subjectsChosen = []
                print("Register Student")
                generalUtils.createNewLine()
                print("1. Register Student\n2. Exit")
                generalUtils.createNewLine()
                registerStudentChoice = input("Choice: ")
                generalUtils.clearConsole()
                if registerStudentChoice == "1":
                    generalUtils.createNewLine()
                    print("Register Student")
                    generalUtils.createNewLine()
                    existingIDList = UniqueIDCreation.readIDFromExistingFile("UserDetails.txt", 1)
                    studentIDNumber = UniqueIDCreation.generateStudentID(existingIDList)
                    print(f"Student ID: {studentIDNumber}")
                    password = input("\nPassword: ")
                    name = input("\nFull Name: ")
                    connectedName = name.replace(" ","_")
                    while True:
                        generalUtils.createNewLine()
                        print("Students Form")
                        generalUtils.createNewLine()
                        print("1. Form 1\n2. Form 2\n3. Form 3\n4. Form 4\n5. Form 5")
                        generalUtils.createNewLine()
                        formChoice = input("Choice: ")
                        generalUtils.createNewLine()
                        if formChoice == "1":
                            form = "Form 1"
                            formattedForm = "Form_1"
                            while True:
                                while True:
                                    try:
                                        numberOfSubjects = int(input("Number of Subjects: "))
                                        break
                                    except ValueError:
                                        print("\nError: Please input a NUMBER")
                                        continue
                                if numberOfSubjects < 4:
                                    while len(subjectsChosen) != int(numberOfSubjects):
                                        generalUtils.createNewLine()
                                        print("Choose the subjects: \n\nChinese - CHF1\nEnglish - ENF1\nMalay- MAF1\nMathemathics - MTHF1\nAdditional Mathemathics - AMTHF1\nGeneral Commerce - GCF1\nGeneral Science - GSF1")
                                        generalUtils.createNewLine()
                                        subject = input("Choice: ").upper().replace(" ", "_")
                                        if subject in subjectsF1:
                                            if not subject in subjectsChosen:
                                                subjectsChosen.append(subject)
                                            else:
                                                print("Error: Subject has already been chosen")
                                        else: 
                                            print("Error: Invalid Input(Please choose from the availale subject list)")
                                            continue
                                    break
                                else:
                                    print("Number of subjects for a student can only be up to 3 subjects")
                                    continue
                        elif formChoice == "2":
                            form = "Form 2"
                            formattedForm = "Form_2"
                            while True:
                                while True:
                                    try:
                                        numberOfSubjects = int(input("Number of Subjects: "))
                                        break
                                    except ValueError:
                                        print("\nError: Please input a NUMBER")
                                        continue
                                if numberOfSubjects < 4:
                                    while len(subjectsChosen) != int(numberOfSubjects):
                                        generalUtils.createNewLine()
                                        print("Choose the subjects: \n\nChinese - CHF2\nEnglish - ENF2\nMalay- MAF2\nMathemathics - MTHF2\nAdditional Mathemathics - AMTHF2\nGeneral Commerce - GCF2\nGeneral Science - GSF2")
                                        generalUtils.createNewLine()
                                        subject = input("Choice: ").upper().replace(" ", "_")
                                        if subject in subjectsF2:
                                            if not subject in subjectsChosen:
                                                subjectsChosen.append(subject)
                                            else:
                                                print("Error: Subject has already been chosen")
                                        else: 
                                            print("Error: Invalid Input(Please choose from the availale subject list)")
                                            continue
                                    break
                                else:
                                    continue
                        elif formChoice == "3":
                            form = "Form 3"
                            formattedForm = "Form_3"
                            while True:
                                while True:
                                    try:
                                        numberOfSubjects = int(input("Number of Subjects: "))
                                        break
                                    except ValueError:
                                        print("\nError: Please input a NUMBER")
                                        continue
                                if numberOfSubjects < 4:
                                    while len(subjectsChosen) != numberOfSubjects:
                                        generalUtils.createNewLine()
                                        print("Choose the subjects: \n\nChinese - CHF3\nEnglish - ENF3\nMalay- MAF3\nMathemathics - MTHF3\nAdditional Mathemathics - AMTHF3\nGeneral Commerce - GCF3\nGeneral Science - GSF3")
                                        generalUtils.createNewLine()
                                        subject = input("Choice: ").upper().replace(" ", "_")
                                        if subject in subjectsF3:
                                            if not subject in subjectsChosen:
                                                subjectsChosen.append(subject)
                                            else:
                                                print("Error: Subject has already been chosen")
                                        else: 
                                            print("Error: Invalid Input(Please choose from the availale subject list)")
                                            continue
                                    break
                                else:
                                    continue
                        elif formChoice == "4":
                            form = "Form 4"
                            formattedForm = "Form_4"
                            while True:
                                while True:
                                    try:
                                        numberOfSubjects = int(input("Number of Subjects: "))
                                        break
                                    except ValueError:
                                        print("\nError: Please input a NUMBER")
                                        continue
                                if numberOfSubjects < 4:
                                    while len(subjectsChosen) != numberOfSubjects:
                                        generalUtils.createNewLine()
                                        print("Choose the subjects: \n\nChinese - CHF4\nEnglish - ENF4\nMalay - MAF4\nMathemathics - MTHF4\nAdditional Mathemathics - AMTHF4\nAccounting - ACF4\nEconomics - ECF4\nBusiness Studies - BSF4\nPhysics - PHF4\nChemistry - CHMF4\nBiology - BIOF4")
                                        generalUtils.createNewLine()
                                        subject = input("Choice: ").upper().replace(" ", "_")
                                        if subject in subjectsF4:
                                            if not subject in subjectsChosen:
                                                subjectsChosen.append(subject)
                                            else:
                                                print("Error: Subject has already been chosen")
                                        else: 
                                            print("Error: Invalid Input(Please choose from the availale subject list)")
                                            continue
                                    break
                                else:
                                    continue
                        elif formChoice == "5":
                            form = "Form 5"
                            formattedForm = "Form_5"
                            while True:
                                while True:
                                    try:
                                        numberOfSubjects = int(input("Number of Subjects: "))
                                        break
                                    except ValueError:
                                        print("\nError: Please input a NUMBER")
                                        continue
                                if numberOfSubjects < 4:
                                    while len(subjectsChosen) != numberOfSubjects:
                                        generalUtils.createNewLine()
                                        print("Choose the subjects: \n\nChinese - CHF5\nEnglish - ENF5\nMalay - MAF5\nMathemathics - MTHF5\nAdditional Mathemathics - AMTHF5\nAccounting - ACF5\nEconomics - ECF5\nBusiness Studies - BSF5\nPhysics - PHF5\nChemistry - CHMF5\nBiology - BIOF5")
                                        generalUtils.createNewLine()
                                        subject = input("Choice: ").upper().replace(" ", "_")
                                        if subject in subjectsF5:
                                            if not subject in subjectsChosen:
                                                subjectsChosen.append(subject)
                                            else:
                                                print("Error: Subject has already been chosen")
                                        else: 
                                            print("Error: Invalid Input(Please choose from the availale subject list)")
                                            time.sleep(2)
                                            continue
                                    break
                                else:
                                    continue
                        else: 
                            continue
                        generalUtils.clearConsole()
                        generalUtils.createNewLine()
                        print(f"Profile\n\nStudent ID: {studentIDNumber}\nPassword: {password}\nName: {name}\nForm: {form}\nSubjects Enrolled: {subjectsChosen}")
                        generalUtils.createNewLine()
                        while True:
                            choice = input("Is this correct(Y/N)? ").upper()
                            if choice == "Y":
                                studentDetails = f"STUDENT;{studentIDNumber};{password};N/A;{connectedName};N/A;N/A;N/A;N/A;{formattedForm};{numberOfSubjects};{subjectsChosen};\n"
                                database.writeToFile("UserDetails.txt", studentDetails)
                                for subject in subjectsChosen:
                                    updateStudentList("SubjectsInfo.txt", subject, connectedName)           
                                print("\nNew student registered")
                                time.sleep(2)
                                break
                            elif choice == "N":
                                print("\nStudent not registered")
                                time.sleep(2)
                                break
                            else:
                                continue
                        break
                    break
                elif registerStudentChoice == "2":
                    break
                else:
                    continue
        elif choice1 == "2":
            while True:
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Delete Student")
                generalUtils.createNewLine()
                studentList = []
                with open("UserDetails.txt","r+") as file:
                    lines = file.readlines()
                    for line in lines:
                        values = line.strip().split(";")
                        if values[0] == "STUDENT":
                            studentList.append(values[1])
                print(f"Students List: {studentList}")
                generalUtils.createNewLine()
                print("1. Delete Student\n2. Exit")
                generalUtils.createNewLine()
                deleteStudentChoice = input("Choice: ")
                generalUtils.clearConsole()
                if deleteStudentChoice == "1":
                    generalUtils.createNewLine()
                    searchStudentID = input("Search Student's ID: ")
                    generalUtils.createNewLine()
                    studentName = database.readListValue(searchStudentID, 1, 4, "UserDetails.txt")
                    with open("UserDetails.txt", "r+") as file:
                        studentSubjects = []
                        lines = file.readlines()

                        for line in lines:
                            values = line.strip().split(";")
                            if values[1] == searchStudentID:
                                studentSubjects = eval(values[11])

                                for deleteSubject in studentSubjects:
                                    print(deleteSubject)
                                    deleteStudentList("SubjectsInfo.txt", deleteSubject, studentName)
                                values[11] = str([subject for subject in studentSubjects if subject != deleteSubject])
                                line = ";".join(values) + "\n"
                            if deleteProfile("UserDetails.txt", searchStudentID, "STUDENT"):
                                print("Student deleted")
                                time.sleep(3)
                                generalUtils.createNewLine()
                        break
                elif deleteStudentChoice == "2":
                    break
                else: 
                    continue
        elif choice1 == "3":
            while True:
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Student Requests")
                generalUtils.createNewLine()
                print("1. Subject Request \n2. Payment Request\n3. Exit")
                generalUtils.createNewLine()
                requestChoice = input("Choice: ")
                if requestChoice == "1":
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("Subject Request")
                    generalUtils.createNewLine()
                    with open("StudentRequest.txt", "r+") as file:
                        requestList = []
                        lines = file.readlines()

                        for line in lines:
                            values = line.strip().split(";")
                            requestList.append(values[0])
                    print(f"Request List: {requestList}")
                    generalUtils.createNewLine()
                    while True:
                        print("1. Continue\n2. Exit")
                        generalUtils.createNewLine()
                        studentRequestChoice = input("Choice: ")
                        if studentRequestChoice == "1":
                            generalUtils.createNewLine()
                            requestID = input("Request ID: ")
                            if requestID in requestList:
                                if checkForValue("StudentRequest.txt", requestID, 0) == True: 
                                    generalUtils.createNewLine()   
                                    studentID = database.readListValue(requestID, 0, 1, "StudentRequest.txt")
                                    print(f"Student ID: {studentID}\n")
                                    name = database.readListValue(studentID, 1, 2, "StudentRequest.txt")
                                    spacedName = name.replace("_", " ")
                                    print(f"Full Name: {spacedName}")
                                    currentSubject = database.readListValue(requestID, 0, 3, "StudentRequest.txt")
                                    requestedSubject = database.readListValue(requestID, 0, 4, "StudentRequest.txt")
                                    generalUtils.createNewLine()
                                    formattedCurrentSubject = currentSubject.upper().replace("_"," ")
                                    formattedRequestedSubject = requestedSubject.upper().replace("_"," ")
                                    print(f"Current Subject: {currentSubject}\n")
                                    print(f"Requested Subject: {requestedSubject}")
                                    generalUtils.createNewLine()
                                    while True:
                                        approval = input("Approved(Y/N)? ").upper()
                                        if approval == "Y":
                                            if changedSubjects("UserDetails.txt", studentID, formattedCurrentSubject, formattedRequestedSubject) and approveSubjectChange("StudentRequest.txt", requestID, studentID, name, currentSubject, requestedSubject) == True:
                                                studentName = database.readListValue(studentID, 1, 4, "UserDetails.txt")
                                                deleteStudentList("SubjectsInfo.txt", currentSubject, name)
                                                updateStudentList("SubjectsInfo.txt", requestedSubject, name)
                                                print("\nRequest Approved(Subject Changed)")
                                                time.sleep(3)
                                                break
                                            else: 
                                                print("\nError: Subject did not change")
                                                time.sleep(3)
                                                break
                                        elif approval == "N":
                                            if rejectSubjectChange("StudentRequest.txt", requestID, studentID, name, currentSubject, requestedSubject) == True:
                                                print("\nRequest Rejected")
                                                time.sleep(3)
                                                break
                                            generalUtils.createNewLine()
                                            time.sleep(3)
                                            break
                                        else:
                                            continue
                                    break
                            else: 
                                print("Error: No request found")
                                generalUtils.createNewLine()
                                time.sleep(3)
                        elif studentRequestChoice == "2":
                            break
                        else:
                            continue
                elif requestChoice == "2":
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("Payment Request")
                    generalUtils.createNewLine()
                    with open("PaymentRequest.txt", "r+") as file:
                        requestList = []
                        lines = file.readlines()

                        for line in lines:
                            values = line.strip().split(";")
                            requestList.append(values[0])
                    print(f"Request List: {requestList}")
                    generalUtils.createNewLine()
                    while True:
                        print("1. Continue\n2. Exit")
                        generalUtils.createNewLine()
                        paymentRequestChoice = input("Choice: ")
                        if paymentRequestChoice == "1":
                            generalUtils.createNewLine()
                            paymentRequestID = input("Payment ID: ")
                            generalUtils.clearConsole()
                            if paymentRequestID in requestList:
                                if checkForValue("PaymentRequest.txt", paymentRequestID, 0) == True: 
                                    generalUtils.createNewLine()   
                                    studentID = database.readListValue(paymentRequestID, 0, 1, "PaymentRequest.txt")
                                    print(f"Student ID: {studentID}\n")
                                    name = database.readListValue(studentID, 1, 2, "StudentRequest.txt")
                                    spacedName = name.replace("_", " ")
                                    print(f"Full Name: {spacedName}")
                                    subjectCode = database.readListValue(paymentRequestID, 0, 3, "PaymentRequest.txt")
                                    amount = database.readListValue(paymentRequestID, 0, 4, "PaymentRequest.txt")
                                    generalUtils.createNewLine()
                                    print(f"Subject Code: {subjectCode}\n")
                                    print(f"Paid Amount: {amount}")
                                    generalUtils.createNewLine()
                                    while True:
                                        approval = input("Approved(Y/N)? ").upper()
                                        if approval == "Y":
                                            existingIDList = UniqueIDCreation.readIDFromExistingFile("ReceiptCollection.txt", 0)
                                            approvedReceiptID = UniqueIDCreation.generateReceiptID(existingIDList)
                                            if updateSubjectIncome("SubjectsInfo.txt", subjectCode, amount) and approvePayment("PaymentRequest.txt", paymentRequestID, studentID, name, subjectCode, amount, approvedReceiptID) == True:
                                                receiptString = f"{approvedReceiptID};{studentID};{name};{subjectCode};{amount};APPROVED;\n"
                                                database.writeToFile("ReceiptCollection.txt", receiptString)
                                                print("\nPayment Request Approved ")
                                                time.sleep(3)
                                                break
                                            else: 
                                                print("\nError: Payment Not Approved")
                                                time.sleep(3)
                                                break
                                        elif approval == "N":
                                            existingIDList = UniqueIDCreation.readIDFromExistingFile("ReceiptCollection.txt", 0)
                                            deletedReceiptID = UniqueIDCreation.generateReceiptID(existingIDList)
                                            if rejectPayment("PaymentRequest.txt", paymentRequestID, studentID, name, subjectCode, amount) == True:
                                                receiptString = f"{deletedReceiptID};{studentID};{name};{subjectCode};{amount};REJECTED;\n"
                                                database.writeToFile("ReceiptCollection.txt", receiptString)
                                                print("\nPayment Request Rejected")
                                                time.sleep(3)
                                                break
                                            generalUtils.createNewLine()
                                            time.sleep(3)
                                        else:
                                            continue
                                    break
                                else: 
                                    print("Error: No request found")
                                    generalUtils.createNewLine()
                                    time.sleep(3)
                        elif paymentRequestChoice == "2":
                            break
                        else:
                            continue
                elif requestChoice == "3":
                    break
                else:
                    continue
        elif choice1 == "4":
            while True:
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Update Profile")
                generalUtils.createNewLine()
                print("1. Update Profile\n2. Exit")
                generalUtils.createNewLine()
                updateProfileChoice = input("Choice: ")
                if updateProfileChoice == "1":
                    password = input("\nPassword: ")
                    ICNumber = int(input("\nIC Number: "))
                    fullName = input("\nFull name: ")
                    formattedFullName = fullName.replace(" ","_")
                    email = input("\nEmail: ")
                    phoneNumber = int(input("\nPhone Number: "))
                    generalUtils.createNewLine()
                    while True: 
                        print("Gender:")
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
                    print(f"ID Number: {userID}\nPassword: {password}\nIC Number: {ICNumber}\nFull Name: {fullName}\nEmail: {email}\nPhone Number: {phoneNumber}\nGender: {gender}\nBirthday: {birthday}")
                    generalUtils.createNewLine()
                    while True:
                        confirmationChoice = input("Is this correct(Y/N)? ").upper()
                        if confirmationChoice == "Y":
                            if updateReceptionistProfile("UserDetails.txt", userID, "RECEPTIONIST",password,ICNumber,formattedFullName,email,phoneNumber,birthday,gender) == True:
                                print("\nProfile Updated")
                                time.sleep(3)
                                break
                        elif confirmationChoice == "N":
                            print("\nProfile not updated")
                            time.sleep(3)
                            break
                        else:
                            print("Invalid Input!\n")
                            time.sleep(2)
                    break
                elif updateProfileChoice == "2":
                    break
                else:
                    continue
        elif choice1 == "5":
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
        elif choice1 == "6":
            print("Logging out")
            return "LOGOUT"
        else:
            continue