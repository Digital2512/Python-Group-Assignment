import database
import UniqueIDCreation
import generalUtils
import time

def addClassSchedule(scheduleFileName, classCode, classTime, classLocation, classDay):
    classScheduleAdded = False
    scheduleList = []
    with open(scheduleFileName, "r") as scheduleFile:
        lines = scheduleFile.readlines()

    for line in lines:
        parts = line.strip().split(";")
        if parts[0] == classLocation and parts[1] == classDay and parts[2] == classTime and parts[4] == "AVAILABLE":
            classScheduleAdded = True
            changedLine = f"{classLocation};{classDay};{classTime};{classCode};UNAVAILABLE;\n"
            scheduleList.append(changedLine)
            continue
        else:
            return classScheduleAdded  # If the loop completes without breaking, class not found in schedule

    with open(scheduleFileName, "w") as scheduleFile:
        scheduleFile.writelines(changedLine)

    return classScheduleAdded  # Class added successfully

def deleteClassSchedule(scheduleFileName, classCode, classTime, classLocation, classDay):
    updatedSchedule = []
    scheduleUpdated = False
    string = f"{classLocation};{classDay};{classTime};{classCode};UNAVAILABLE"
    with open(scheduleFileName, "r") as file:
        lines = file.readlines()
    for line in lines:
        if line == string:
            scheduleUpdated = True
            continue
        else:
            updatedSchedule.append(line)
    if scheduleUpdated == True:
        updatedString = f"{classLocation};{classDay};{classTime};N/A;AVAILABLE"
        updatedSchedule.append(updatedString)
    with open(scheduleFileName, "w") as file:
        file.writelines(updatedSchedule)

    return scheduleUpdated

def addClassInfo(classFileName, classCode, className, classForm, classTime, classLocation, classDay):
    classInfoAdded = False
    with open(classFileName, "a") as classFile:
        classInfo = f"{classCode};{className};{classForm};{classDay};{classTime};{classLocation}\n"
        classFile.write(classInfo)
        classInfoAdded = True
        return classInfoAdded

def deleteClassInfo(classFileName, classCode, className, classForm, classTime, classLocation, classDay):
    deletedClass = False
    classString = f"{classCode};{className};{classForm};{classDay};{classTime};{classLocation};\n"
    updatedClass = []
    with open(classFileName, "r") as classFile:
        lines = classFile.readlines()
    for line in lines:
        if line == classString:
            deletedClass = True
            continue
        else:
            updatedClass.append(line)

    with open(classFileName, "w") as classFile:
        classFile.writelines(updatedClass)
    return deletedClass

def updateClassInfo(fileToCheck, classCode, time, location, date, className, classForm):
    updatedClass = False
    updated_data = []  # To store updated data
    with open(fileToCheck, "r") as file:
        for line in file:
            values = line.strip().split(";")
            if values[1] == str(classCode):
                # Skip the line to delete it
                updatedClass = True
                continue
            updated_data.append(line)

    # Add the updated line at the end
    if updatedClass == True:
        updated_data.append(f"{classCode};{className};{classForm}{location};{date};{time};")

        # Write the updated data back to the file
        with open(fileToCheck, "w") as file:
            file.writelines(updated_data)
    return updatedClass

def readClassAssigned(fileName, indexOfClassCode, numberOfSubjects):
    classCodeAssigned = []
    for i in range(indexOfClassCode, numberOfSubjects, 1):
        with open(fileName, "r") as file:
            for line in file:
                values = line.strip().split(";")
                classCodeAssigned.append(values[indexOfClassCode])
    return classCodeAssigned

def updateProfile(fileToCheck, IDNumber, role, password, ICNumber, fullName, email, phoneNumber, birthday, gender):
    updatedProfile = False
    capitalizedRole = role.upper()
    updated_data = []  # To store updated data
    with open(fileToCheck, "r") as file:
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
        with open(fileToCheck, "w") as file:
            file.writelines(updated_data)
    return updatedProfile
          
def pgTutor(userID):
    subjectCodeList = []
    classrooms = ["C01", "C02","C03","C04","C05"]
    forms = ["FORM 1", "FORM 2", "FORM 3", "FORM 4", "FORM 5"]
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    while True:
        generalUtils.clearConsole()
        generalUtils.createNewLine()
        with open("UserDetails.txt", "r") as file:
            for line in file:
                values = line.strip().split(";")
                if values[1] == userID:
                    splittedName = values[4].replace("_"," ")
                    print(f"Welcome, {splittedName} ({values[0]})")
        generalUtils.createNewLine()
        with open("UserDetails.txt", "r") as file:
            for line in file:
                values = line.strip().split(";")
                if values[1] == userID:
                    subjects = values[3].replace("[","").replace("]","").replace("'","").strip("N/A").split(",")
                    for subject in subjects:
                        if subject.strip() != "N/A":
                            subjectCodeList.append(subject.strip())
        # Print subjectCodeList after the loop
        subjectAssigned = subjectCodeList.pop()
        print(f"Classes assigned: {subjectAssigned}")
        print("1. Change classes\n2. Update class information\n3. View class information\n4. Update Profile\n5. View Profile\n6. View Students Enrolled \n7.Log Out")
        generalUtils.createNewLine()
        choice = input("Choice: ")
        if choice == "1":
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("Change classes")
            generalUtils.createNewLine()
            print("1. Add classes \n2. Delete Classes")
            choiceClass = input("Choice: ")
            if choiceClass == "1":
                while True:
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("Add classes")
                    while True: 
                        classCode = input("Class Code: ").upper()
                        if classCode in subjectCodeList:
                            break
                        else:
                            continue
                    className = input("Class Name: ")
                    formattedClassName = className.replace(" ","_")
                    classForm = f"Form {classCode[-1:]}"
                    formattedClassForm = classForm.upper().replace(" ","_")
                    while True: 
                        classDay = input("Day: ").upper()
                        if classDay in days:
                            break
                        else: 
                            continue
                    while True:
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
                    print(f"Class code: {classCode}\nClass name: {formattedClassName}\nClass Form: {formattedClassForm}\nClass Day: {classDay.capitalize()}\nClass Time: {classTime}\nClass Location: {classLocation}")
                    while True:
                        doneView = input("Is this correct? (Press Y/N)?")
                        if doneView == "Y":
                            if addClassInfo("ClassInfo.txt", classCode, formattedClassName, classForm, classTime, classLocation, classDay) and addClassSchedule("ClassSchedule.txt", classCode, classTime, classLocation, classDay) == True:
                                print("Classroom added")
                                time.sleep(3)
                                break
                            else:
                                print("Error: Classroom taken")
                        elif doneView == "N":
                            print("Class not added")
                            time.sleep(3)
                            break
                        else:
                            continue
                        break
                    break
            elif choiceClass == "2":
                while True:
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("Delete classes")
                    generalUtils.createNewLine()
                    while True: 
                        classCode = input("Class Code: ").upper()
                        if classCode in subjectCodeList:
                            break
                        else:
                            continue
                    className = input("Class Name: ")
                    formattedClassName = className.replace(" ","_")
                    # classForm = input("Form: ").upper()
                    classForm = f"Form {classCode[-1:]}"
                    formattedClassForm = classForm.upper().replace(" ","_")
                    while True: 
                        classDay = input("Day: ").upper()
                        if classDay in days:
                            break
                        else: 
                            continue
                    while True:
                        print("Timing")
                        generalUtils.createNewLine()
                        print("1. 12.00 - 14.00\n2. 14.00 - 16.00\n3. 16.00 - 18.00\n4. 18.00 - 20.00")
                        generalUtils.createNewLine()
                        timeChoice = [1,2,3,4,5]
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
                    print(f"Class code: {classCode}\nClass name: {formattedClassName}\nClass Form: {formattedClassForm}\nClass Day: {classDay}\nClass Time: {classTime}\nClass Location: {classLocation}")
                    while True:
                        doneView = input("Confirm (Press Y/N)?")
                        if doneView == "Y":
                            if deleteClassInfo( "ClassInfo.txt", classCode, formattedClassName, classForm, classTime, classLocation, classDay) and deleteClassSchedule("ClassSchedule.txt", classCode, classTime, classLocation, classDay) == True:
                                print("Error: Class not deleted")
                                time.sleep(3)
                            else:
                                print("Class deleted")
                                time.sleep(3)
                            break
                        elif doneView == "N":
                            print("Class not deleted")
                            time.sleep(3)
                            break
                        else:
                            continue
                    break
                break
        elif choice == "2":
            while True:
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Update class info")
                while True:
                    classCode = input("Class code: ").upper()
                    if classCode in subjectCodeList:
                        break
                    else:
                        continue
                className = input("Class name: ")
                while True:
                    classForm = input("Form: ").upper()
                    if classForm in forms:
                        break
                    else:
                        continue
                while True: 
                    classDate = input("Date(XX-XX-XXXX): ")
                    if len(classDate) == 10:
                        break
                    else: 
                        continue
                while True:
                    classTime = input("Date(XX:XX): ")
                    if len(classTime) == 5:
                        break
                    else: 
                        continue
                while True: 
                    classLocation = input("Location: ")
                    if classLocation in classrooms:
                        break
                    else:
                        continue
                updateClassInfo("ClassInfo.txt", classCode, classTime, classLocation, classDate, className, classForm)
        elif choice == "3":
            print("View class info")
            existingClassCode = readClassAssigned("SubjectInfo.txt", 0,)
            while True:
                classCode = input("Class Code: ").upper()
                if classCode in existingClassCode:
                    break
                else:
                    continue
            className = database.readListValue(classCode, 0, 1,"ClassInfo.txt").capitalize().replace("_", " ")
            classForm = database.readListValue(classCode, 0, 2,"ClassInfo.txt").capitalize().replace("_", " ")
            classDate = database.readListValue(classCode, 0, 3,"ClassInfo.txt")
            classTime = database.readListValue(classCode, 0, 4,"ClassInfo.txt")
            classLocation = database.readListValue(classCode, 0, 5,"ClassInfo.txt")
            print(f"Class Code: {classCode}\nClass Name: {className}\nClass Form: {classForm}\nClass Date: {classDate}\nClass Time: {classTime}\nClass Location: {classLocation}")
        elif choice == "4":
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
                    if updateProfile("UserDetails.txt", userID, "TUTOR",password,ICNumber,fullName,email,phoneNumber,birthday,gender) == True:
                        print("Profile updated")
                        break
                elif confirmationChoice == "N":
                    print("Profile not updated")
                    break
                else:
                    print("Invalid Input!\n")
                time.sleep(5)
        elif choice == "5":
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
            subject = database.readListValue(userID, 1, 9, "UserDetails.txt")

            print(f"User ID: {userID}\nIC Number: {ICNumber}\nFull Name: {fullName}\nEmail: {email}\nPhone Number: {phoneNumber}\nGender: {gender}\nBirthday: {birthday}\nSubject: {subject}")
            generalUtils.createNewLine()
            while True:
                print("Done Viewing(Enter Y when you are done)? ")
                generalUtils.createNewLine()
                doneView = input("Choice: ").upper()
                if doneView == "Y":
                    break
                else:
                    continue
        elif choice == "6":
            print("View students enrolled")

        elif choice == "7":
            print("Log out")
            return "LOGOUT"

pgTutor("T001")