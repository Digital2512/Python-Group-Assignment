import database
import UniqueIDCreation
import generalUtils
import time

def updateTutorProfile(fileToCheck, IDNumber, role, password, ICNumber, fullName, email, phoneNumber, birthday, gender, subjectForm, numberOfSubject, subjectAssigned):
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
        updated_data.append(f"{capitalizedRole};{IDNumber};{password};{ICNumber};{fullName};{email};{phoneNumber};{gender};{birthday};{subjectForm};{numberOfSubject};{subjectAssigned}\n")

    # Write the updated data back to the file
        with open(fileToCheck, "+w") as file:
            file.writelines(updated_data)
    return updatedProfile

def readClassAssigned(fileName, indexOfClassCode, numberOfSubjects):
    classCodeAssigned = []
    for i in range(int(indexOfClassCode), int(numberOfSubjects), 1):
        with open(fileName, "r") as file:
            for line in file:
                values = line.strip().split(";")
                classCodeAssigned.append(values[indexOfClassCode])
    return classCodeAssigned

def addClassInfo(classFileName, classCode, className, classForm, classTime, classLocation, classDay):
    classInfoAdded = False
    updatedLines = []

    with open(classFileName, "+r") as file:
        lines = file.readlines()

    for line in lines:
        values = line.strip().split(";")
        if values[0] == classCode:
            classInfoAdded = True
            continue
        else:
            updatedLines.append(line)

    if classInfoAdded:
        classInfo = f"{classCode};{className};{classForm};{classDay};{classTime};{classLocation};\n"
        updatedLines.append(classInfo)

    with open(classFileName, "+w") as file:
        file.writelines(updatedLines)

    return classInfoAdded

def updateClassSchedule(fileToCheck, classCode, classTime, classLocation, classDay):
    updatedClass = False
    updated_data = []  # To store updated data
    with open(fileToCheck, "+r") as file:
        for line in file:
            values = line.strip().split(";")
            if values[3] == str(classCode):
                # Skip the line to delete it
                updatedClass= True
                continue
            updated_data.append(line)

    # Add the updated line at the end
    if updatedClass: 
        updated_data.append(f"{classLocation};{classDay};{classTime};{classCode};UNAVAILABLE;\n")

    # Write the updated data back to the file
        with open(fileToCheck, "+w") as file:
            file.writelines(updated_data)
    return updatedClass

def updateClassInfo(fileToCheck, classCode, classForm, classTime, classLocation, classDay, className):
    updatedClass = False
    updated_data = []  # To store updated data
    with open(fileToCheck, "+r") as file:
        for line in file:
            values = line.strip().split(";")
            if values[0] == str(classCode):
                # Skip the line to delete it
                updatedClass= True
                continue
            updated_data.append(line)

    # Add the updated line at the end
    if updatedClass: 
        updated_data.append(f"{classCode};{className};{classForm};{classDay};{classTime};{classLocation};\n")

    # Write the updated data back to the file
        with open(fileToCheck, "+w") as file:
            file.writelines(updated_data)
    return updatedClass

def addClassSchedule(scheduleFileName, classCode, classTime, classLocation, classDay):
    classroomScheduled = False
    classroomProfile = f"{classLocation};{classDay};{classTime};{classCode};UNAVAILABLE\n"
    changedLines = []

    with open(scheduleFileName, "r+") as file:
        lines = file.readlines()

        for line in lines:
            parts = line.strip().split(";")
            if parts[0] == classLocation and parts[1] == classDay and parts[2] == classTime and parts[4] == "AVAILABLE":
                classroomScheduled = True
                continue
            else:
                changedLines.append(line)
            
        if classroomScheduled:
            changedLines.append(classroomProfile)

    with open(scheduleFileName, "w+") as file:
        file.writelines(changedLines)  # Write the updated lines

    return classroomScheduled

def deleteClassInfo(classFileName, classCode):
    deletedClass = False
    deletedClassString = f"{classCode};N/A;N/A;N/A;N/A;N/A;\n"  # Include newline character

    updatedClass = []

    with open(classFileName, "r+") as classFile:
        lines = classFile.readlines()
        classFile.seek(0)  # Move the file pointer to the beginning

        for line in lines:
            values = line.strip().split(";")
            if values[0] == classCode:
                deletedClass = True
                continue
            else:
                updatedClass.append(line)

        if deletedClass:
            updatedClass.append(deletedClassString)
    
        classFile.seek(0)  # Move the file pointer to the beginning
        classFile.truncate()  # Clear the file content
        classFile.writelines(updatedClass)  # Write the updated lines

    return deletedClass

def deleteClassSchedule(scheduleFileName, classCode):
    updatedSchedule = []
    scheduleUpdated = False
    with open(scheduleFileName, "+r") as file:
        lines = file.readlines()
        for line in lines:
            values = line.strip().split(";")
            if values[3] == classCode:
                classLocation = values[0]
                classDay = values[1]
                classTime = values[2]
                scheduleUpdated = True
                continue
            else:
                updatedSchedule.append(line)

        if scheduleUpdated:
            deletedScheduleString = f"{classLocation};{classDay};{classTime};N/A;AVAILABLE;\n"
            updatedSchedule.append(deletedScheduleString)

    with open(scheduleFileName, "+w") as file:
        file.writelines(updatedSchedule)

    return scheduleUpdated
          
def pgTutor(userID):
    classrooms = ["C01", "C02","C03","C04","C05"]
    forms = ["FORM 1", "FORM 2", "FORM 3", "FORM 4", "FORM 5"]
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    while True:
        generalUtils.clearConsole()
        generalUtils.createNewLine()
        with open("UserDetails.txt", "+r") as file:
            lines = file.readlines()

        for line in lines:
            values = line.strip().split(";")
            if values[1] == userID:                    
                splittedName = values[4].replace("_"," ")
                print(f"Welcome, {splittedName} ({values[0]})")
        generalUtils.createNewLine()
        with open("UserDetails.txt", "r") as file:
            for line in file:
                values = line.strip().split(";")
                if values[1] == userID:
        # Print subjectCodeList after the loop
                    subjectAssigned = eval(values[11]) 
        print(f"Classes assigned: {subjectAssigned}")
        generalUtils.createNewLine()
        print("1. Add or Delete Classes\n2. Update class info\n3. View class info\n4. Update Profile\n5. View Profile\n6. Log Out")
        generalUtils.createNewLine()
        choice = input("Choice: ")
        if choice == "1":
            while True:
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Classes")
                generalUtils.createNewLine()
                print("1. Add classes \n2. Delete Classes\n3. Exit")
                generalUtils.createNewLine()
                choiceClass = input("Choice: ")
                if choiceClass == "1":
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("Add classes")
                    generalUtils.createNewLine()
                    with open("UserDetails.txt", "r") as file:
                        for line in file:
                            values = line.strip().split(";")
                            if values[1] == userID:
                    # Print subjectCodeList after the loop
                                subjectAssigned = eval(values[11]) 
                    print(f"Classes assigned: {subjectAssigned}")
                    generalUtils.createNewLine()
                    while True: 
                        classCode = input("Class Code: ").upper()
                        if classCode in subjectAssigned:
                            break
                        else:
                            continue
                    className = input("Class Name: ")
                    formattedClassName = className.replace(" ","_")
                    classForm = f"Form {classCode[-1:]}"
                    formattedClassForm = classForm.replace(" ", "_")
                    while True: 
                        classDay = input("Day: ").upper()
                        if classDay in days:
                            break
                        else: 
                            continue
                    while True:
                        generalUtils.createNewLine()
                        print("Timing")
                        generalUtils.createNewLine()
                        print("1. 12.00 - 14.00\n2. 14.00 - 16.00\n3. 16.00 - 18.00\n4. 18.00 - 20.00")
                        generalUtils.createNewLine()
                        timeChoice = [1,2,3,4]
                        choiceTime = int(input("Choice: "))
                        if choiceTime in timeChoice:
                            if choiceTime == 1:
                                classTime = "12.00-14.00"
                                break
                            elif choiceTime == 2:
                                classTime = "14.00-16.00"
                                break
                            elif choiceTime == 3:
                                classTime = "16.00-18.00"
                                break
                            elif choiceTime == 4:
                                classTime = "18.00-20.00"
                                break
                        else: 
                            continue
                    while True: 
                        classLocation = input("Location: ")
                        if classLocation in classrooms:
                            break
                        else:
                            continue
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print(f"Class code: {classCode}\nClass name: {className}\nClass Form: {classForm}\nClass Day: {classDay.capitalize()}\nClass Time: {classTime}\nClass Location: {classLocation}")
                    while True:
                        generalUtils.createNewLine()
                        doneView = input("Is this correct(Y/N)? ").upper()
                        if doneView == "Y":
                            if addClassSchedule("ClassSchedule.txt", classCode, classTime, classLocation, classDay) == True:
                                if addClassInfo("ClassInfo.txt", classCode, formattedClassName, formattedClassForm, classTime, classLocation, classDay) == True:
                                    print("\nClass added")
                                    time.sleep(3)
                            else:
                                print("\nClass not added")
                                time.sleep(3)
                            break
                        elif doneView == "N":
                            print("\nClass not added")
                            time.sleep(3)
                            break
                        else:
                            continue
                    break
                elif choiceClass == "2":
                        generalUtils.clearConsole()
                        generalUtils.createNewLine()
                        print("Delete classes")
                        generalUtils.createNewLine()
                        with open("UserDetails.txt", "r") as file:
                            for line in file:
                                values = line.strip().split(";")
                                if values[1] == userID:
                        # Print subjectCodeList after the loop
                                    subjectAssigned = eval(values[11]) 
                        print(f"Classes assigned: {subjectAssigned}")
                        generalUtils.createNewLine()
                        while True: 
                            classCode = input("Class Code: ").upper()
                            if classCode in subjectAssigned:
                                break
                            else:
                                continue
                        generalUtils.clearConsole()
                        generalUtils.createNewLine()
                        print(f"Class code: {classCode}")
                        while True:
                            generalUtils.createNewLine()
                            deleteConfirmationChoice = input("Confirm (Press Y/N)?").upper()
                            if deleteConfirmationChoice == "Y":
                                if deleteClassSchedule("ClassSchedule.txt", classCode) == True:
                                    if deleteClassInfo("ClassInfo.txt", classCode) == True:
                                        print("\nClass deleted")
                                        time.sleep(3)
                                        break
                                else:
                                    print("Error: Class not deleted")
                                    time.sleep(3)
                                    break
                            elif deleteConfirmationChoice == "N":
                                print("Class not deleted")
                                time.sleep(3)
                                break
                        break
                elif choiceClass == "3":
                    break
                else:
                    continue
        elif choice == "2":
            while True:
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Update class Info")
                generalUtils.createNewLine()
                print("1. Update Class Info\n2. Exit")
                generalUtils.createNewLine()
                updateClassInfoChoice = input("Choice: ")
                if updateClassInfoChoice == "1":
                    with open("UserDetails.txt", "r") as file:
                        for line in file:
                            values = line.strip().split(";")
                            if values[1] == userID:
                    # Print subjectCodeList after the loop
                                subjectAssigned = eval(values[11]) 
                    print(f"Classes assigned: {subjectAssigned}")
                    generalUtils.createNewLine()
                    while True: 
                        classCode = input("Class Code: ").upper()
                        if classCode in subjectAssigned:
                                break
                        else:
                            continue
                    className = input("Class Name: ")
                    formattedClassName = className.replace(" ","_")
                    classForm = f"Form {classCode[-1:]}"
                    formattedClassForm = classForm.replace(" ", "_")
                    while True: 
                        classDay = input("Day: ").upper()
                        if classDay in days:
                            break
                        else: 
                            continue
                    while True:
                        generalUtils.createNewLine()
                        print("Timing")
                        generalUtils.createNewLine()
                        print("1. 12.00 - 14.00\n2. 14.00 - 16.00\n3. 16.00 - 18.00\n4. 18.00 - 20.00")
                        generalUtils.createNewLine()
                        timeChoice = [1,2,3,4]
                        choiceTime = int(input("Choice: "))
                        if choiceTime in timeChoice:
                            if choiceTime == 1:
                                classTime = "12.00-14.00"
                                break
                            elif choiceTime == 2:
                                classTime = "14.00-16.00"
                                break
                            elif choiceTime == 3:
                                classTime = "16.00-18.00"
                                break
                            elif choiceTime == 4:
                                classTime = "18.00-20.00"
                                break
                        else: 
                            continue
                    while True: 
                        classLocation = input("Location: ")
                        if classLocation in classrooms:
                            break
                        else:
                            continue
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print(f"Class code: {classCode}\nClass name: {className}\nClass Form: {classForm}\nClass Day: {classDay.capitalize()}\nClass Time: {classTime}\nClass Location: {classLocation}")
                    generalUtils.createNewLine()
                    formattedClassForm = classForm.replace(" ","_")
                    while True:
                        confirmationChoice = input("Confirm(Y/N)? ").upper()
                        if confirmationChoice == "Y":
                            if updateClassInfo("ClassInfo.txt", classCode, formattedClassForm, classTime, classLocation, classDay, formattedClassName) and updateClassSchedule("ClassSchedule.txt", classCode, classTime, classLocation, classDay): 
                                print("Class updated")
                                time.sleep(3)
                                break
                            else:
                                print("Class not updated")
                                break
                        elif confirmationChoice == "N":
                            print("Class not updated")
                            time.sleep(3)
                            break
                        else:
                            continue
                    break
                elif updateClassInfoChoice == "2":
                    break
        elif choice == "3":
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("View class info")
            generalUtils.createNewLine()
            print(f"Subjects assigned: {subjectAssigned}")
            generalUtils.createNewLine()
            while True:
                classCode = input("Class Code: ").upper()
                if classCode in subjectAssigned:
                    break
                else:
                    continue
            # f"{classCode};{className};{classForm}{location};{date};{time};"
            generalUtils.createNewLine()
            className = database.readListValue(classCode, 0, 1,"ClassInfo.txt").capitalize().replace("_", " ")
            classForm = database.readListValue(classCode, 0, 2,"ClassInfo.txt").capitalize().replace("_", " ")
            classDay = database.readListValue(classCode, 0, 3,"ClassInfo.txt")
            classTime = database.readListValue(classCode, 0, 4,"ClassInfo.txt")
            classLocation = database.readListValue(classCode, 0, 5,"ClassInfo.txt")
            classStudentList = database.readListValue(classCode, 0, 4, "SubjectsInfo.txt")
            print(f"Class Code: {classCode}\nClass Name: {className}\nClass Form: {classForm}\nClass Day: {classDay}\nClass Time: {classTime}\nClass Location: {classLocation}\nClass's students list: {classStudentList}")
            generalUtils.createNewLine()
            while True:
                doneView = input("Are you done with viewing(Y/N)? ").upper()
                if doneView == "Y":
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
            updateProfileChoice = input("Choice: ")
            if updateProfileChoice == "1":
                password = input("\nPassword: ")
                ICNumber = int(input("\nIC Number: "))
                fullName = input("\nFull name: ")
                formattedName = fullName.replace(" ", "_")
                email = input("\nEmail: ")
                phoneNumber = int(input("\nPhone Number: "))
                generalUtils.createNewLine()
                while True: 
                    print("Gender: ")
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
                        subject = subjectAssigned[0]
                        numberOfSubjects = len(subjectAssigned)
                        subjectForm = subject[:-1]
                        if updateTutorProfile("UserDetails.txt", userID, "TUTOR",password,ICNumber,formattedName,email,phoneNumber,birthday,gender,subjectForm,numberOfSubjects,subjectAssigned) == True:
                            print("Profile Updated")
                            break
                    elif confirmationChoice == "N":
                        print("Profile not updated")
                        break
                    else:
                        print("Invalid Input!\n")
                    time.sleep(5)
            elif updateProfileChoice == "2":
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
                print("Are you done with viewing(Y/N)? ")
                generalUtils.createNewLine()
                doneViewing = input("Choice: ").upper()
                if doneViewing == "Y":
                    break
                else:
                    continue
        elif choice == "6":
            print("Log out")
            return "LOGOUT"

        