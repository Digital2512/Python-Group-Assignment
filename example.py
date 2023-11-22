import UniqueIDCreation
import database
import generalUtils
import time


def updateProfile(fileToCheck, IDNumber, role, password, ICNumber, fullName, email, phoneNumber, birthday, gender):
    updatedProfile = False
    capitalizedRole = role.upper()
    updated_data = gi[]  # To store updated data
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


def registerReceptionist(userID, password):
    userProfile = f"RECEPTIONIST;{userID};{password}\n"
    return database.writeToFile("UserDetails.txt", userProfile)

def registerTutor(userID, password, subject):
    userProfile = f"TUTOR;{userID};{password};{subject}\n"
    return database.writeToFile("UserDetails.txt", userProfile)


def readSubjectCode(fileName, indexOfSubjectCode):
    subjectCode = []
    with open(fileName, "r") as file:
        for line in file:
            values = line.strip().split(";")
            subjectCode.append(values[indexOfSubjectCode])
    return subjectCode

def pgAdmin(userID):
    subjectCode = readSubjectCode("SubjectInfo.txt", 0)
    while True:
        generalUtils.clearConsole()
        generalUtils.createNewLine()
        with open("UserDetails.txt", "+r") as file:
            for line in file:
                values = line.strip().split(";")
                if values[1] == userID:
                    splittedName = values[4].replace("_", " ")
                    print(f"Welcome, {splittedName} ({values[0]})")
            generalUtils.createNewLine()
            while True:
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("1.Register\n2.View Income\n3.View Admin Profile\n4.Update Admin Profile\n5.Log Out")
                generalUtils.createNewLine()
                choice = int(input("Choice:"))
                if choice == 1:
                    existingIDs = UniqueIDCreation.readIDFromExistingFile("UserDetails.txt",0)
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("Register:\n1.Receptionist\n2.Tutor")
                    generalUtils.createNewLine()
                    choiceRegister = int(input("Choice:"))
                    if choiceRegister == 1:
                        generalUtils.createNewLine()
                        print("Register Receptonist")
                        generalUtils.createNewLine()
                        userID = UniqueIDCreation.generateReceptionistID(existingIDs)
                        password = input("Password:")
                        registerReceptionist(userID,password)
                    elif choiceRegister == 2:
                        listOfSubject = []
                        generalUtils.clearConsole()
                        generalUtils.createNewLine()
                        print("Register Tutor")
                        generalUtils.createNewLine()
                        userID = UniqueIDCreation.generateTutorID(existingIDs)
                        password = input("Password:")
                        numberOfSubjects = int(input("Number of Subjects: "))
                        while len(listOfSubject) != numberOfSubjects: 
                            while True:
                                subject = input("Subject Code:").upper()
                                if subject in subjectCode:
                                    listOfSubject.append(subject)
                                    break
                                else:
                                    print("Subject code not found")
                                    continue
                        registerTutor(userID,password,listOfSubject)
                    else:
                        continue
                elif choice == 2:
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("View Monthly Income")
                    generalUtils.createNewLine()
                    print("Form 1")
                    form1Chinese = database.readListValue("CHF1",0,2,"subjectsInfo.txt")
                    form1English = database.readListValue("ENG1",0,2,"subjectsInfo.txt")
                    form1Malay = database.readListValue("MAF1",0,2,"subjectsInfo.txt")
                    form1Mathemathics = database.readListValue("MATHF1",0,2,"subjectsInfo.txt")
                    form1AdditionalMathemathics = database.readListValue("AMTHF1",0,2,"subjectsInfo.txt")
                    form1GeneralCommerce = database.readListValue("GCF1",0,2,"subjectsInfo.txt")
                    form1GeneralScience = database.readListValue("GSF1",0,2,"subjectsInfo.txt")
                    print(f"Chinese: {form1Chinese}\nEnglish: {form1English}\nMalay: {form1Malay}\nMathemathics: {form1Mathemathics}\nAdditional Mathemathics: {form1AdditionalMathemathics}\nGeneral Commerce: {form1GeneralCommerce}\nGeneral Science: {form1GeneralScience}")
                    generalUtils.createNewLine()
                    print("Form 2")
                    form2Chinese = database.readListValue("CHF2",0,2,"subjectsInfo.txt")
                    form2English = database.readListValue("ENG2",0,2,"subjectsInfo.txt")
                    form2Malay = database.readListValue("MAF2",0,2,"subjectsInfo.txt")
                    form2Mathemathics = database.readListValue("MATHF2",0,2,"subjectsInfo.txt")
                    form2AdditionalMathemathics = database.readListValue("AMTHF2",0,2,"subjectsInfo.txt")
                    form2GeneralCommerce = database.readListValue("GCF2",0,2,"subjectsInfo.txt")
                    form2GeneralScience = database.readListValue("GSF2",0,2,"subjectsInfo.txt")
                    print(f"Chinese: {form2Chinese}\nEnglish: {form2English}\nMalay: {form2Malay}\nMathemathics: {form2Mathemathics}\nAdditional Mathemathics: {form2AdditionalMathemathics}\nGeneral Commerce: {form2GeneralCommerce}\nGeneral Science: {form2GeneralScience}")
                    generalUtils.createNewLine()
                    print("Form 3")
                    form3Chinese = database.readListValue("CHF3",0,2,"subjectsInfo.txt")
                    form3English = database.readListValue("ENG3",0,2,"subjectsInfo.txt")
                    form3Malay = database.readListValue("MAF3",0,2,"subjectsInfo.txt")
                    form3Mathemathics = database.readListValue("MATHF3",0,2,"subjectsInfo.txt")
                    form3AdditionalMathemathics = database.readListValue("AMTHF3",0,2,"subjectsInfo.txt")
                    form3GeneralCommerce = database.readListValue("GCF3",0,2,"subjectsInfo.txt")
                    form3GeneralScience = database.readListValue("GSF3",0,2,"subjectsInfo.txt")
                    print(f"Chinese: {form3Chinese}\nEnglish: {form3English}\nMalay: {form3Malay}\nMathemathics: {form3Mathemathics}\nAdditional Mathemathics: {form3AdditionalMathemathics}\nGeneral Commerce: {form3GeneralCommerce}\nGeneral Science: {form3GeneralScience}")
                    generalUtils.createNewLine()
                    print("Form 4")
                    form4Chinese = database.readListValue("CHF4",0,2,"subjectsInfo.txt")
                    form4English = database.readListValue("ENG4",0,2,"subjectsInfo.txt")
                    form4Malay = database.readListValue("MAF4",0,2,"subjectsInfo.txt")
                    form4Mathemathics = database.readListValue("MATHF4",0,2,"subjectsInfo.txt")
                    form4AdditionalMathemathics = database.readListValue("AMTHF4",0,2,"subjectsInfo.txt")
                    form4Accounting = database.readListValue("ACF4",0,2,"subjectsInfo.txt")
                    form4Economics = database.readListValue("ECF4",0,2,"subjectsInfo.txt")
                    form4BusinessStudies = database.readListValue("BSF4",0,2,"subjectsInfo.txt")
                    form4Physics = database.readListValue("PHF4",0,2,"subjectsInfo.txt")
                    form4Chemistry = database.readListValue("CHMF4",0,2,"subjectsInfo.txt")
                    form4Biology = database.readListValue("BIOF4",0,2,"subjectsInfo.txt")
                    print(f"Chinese: {form4Chinese}\nEnglish: {form4English}\nMalay: {form4Malay}\nMathemathics: {form4Mathemathics}\nAdditional Mathemathics: {form4AdditionalMathemathics}\nAccounting: {form4Accounting}\nEconomics: {form4Economics}\nBusiness Studies: {form4BusinessStudies}\nPhysics: {form4Physics}\nChemistry: {form4Chemistry}\nBiology: {form4Biology}")
                    generalUtils.createNewLine()
                    print("Form 5")
                    form5Chinese = database.readListValue("CHF5",0,2,"subjectsInfo.txt")
                    form5English = database.readListValue("ENG5",0,2,"subjectsInfo.txt")
                    form5Malay = database.readListValue("MAF5",0,2,"subjectsInfo.txt")
                    form5Mathemathics = database.readListValue("MATHF5",0,2,"subjectsInfo.txt")
                    form5AdditionalMathemathics = database.readListValue("AMTHF5",0,2,"subjectsInfo.txt")
                    form5Accounting = database.readListValue("ACF5",0,2,"subjectsInfo.txt")
                    form5Economics = database.readListValue("ECF5",0,2,"subjectsInfo.txt")
                    form5BusinessStudies = database.readListValue("BSF5",0,2,"subjectsInfo.txt")
                    form5Physics = database.readListValue("PHF5",0,2,"subjectsInfo.txt")
                    form5Chemistry = database.readListValue("CHMF5",0,2,"subjectsInfo.txt")
                    form5Biology = database.readListValue("BIOF5",0,2,"subjectsInfo.txt")
                    print(f"Chinese: {form5Chinese}\nEnglish: {form5English}\nMalay: {form5Malay}\nMathemathics: {form5Mathemathics}\nAdditional Mathemathics: {form5AdditionalMathemathics}\nAccounting: {form5Accounting}\nEconomics: {form5Economics}\nBusiness Studies: {form5BusinessStudies}\nPhysics: {form5Physics}\nChemistry: {form5Chemistry}\nBiology: {form5Biology}")
                    generalUtils.createNewLine()
                elif choice == 3:
                    generalUtils.clearConsole()
                    print("Viewing Admin Profile")
                    generalUtils.createNewLine()
                    ICNumber = database.readListValue(userID,1,3,"UserDetails.txt")
                    fullName = database.readListValue(userID,1,4,"UserDetails.txt")
                    email = database.readListValue(userID,1,5,"UserDetails.txt")
                    phoneNumber = database.readListValue(userID,1,6,"UserDetails.txt")
                    gender = database.readListValue(userID,1,7,"UserDetails.txt")
                    birthday = database.readListValue(userID,1,8,"UserDetails.txt")
                    print(f"User ID:{userID}\nIC Number:{ICNumber}\nFull name:{fullName}\nEmail:{email}\nPhone Number:{phoneNumber}\nGender:{gender}\nBirthday:{birthday}")
                    generalUtils.createNewLine()
                    while True:
                        print("Are you done viewing?")
                        generalUtils.createNewLine()
                        doneViewing = input("If done viewing, please enter Y.\nAnswer:").upper()
                        if doneViewing == "Y":
                            break
                        else:
                            continue
                elif choice == 4:
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("Update Admin Profile")
                    generalUtils.createNewLine()
                    password = input("Password:")
                    email = input("Email:")
                    fullName = input("Full Name:")
                    formattedFullName = fullName.replace("","_")
                    ICNumber = int(input("IC Number:"))
                    phoneNumber = int(input("Phone Number:"))
                    generalUtils.createNewLine()
                    while True:
                        gender = input("Gender:\n1.Male\n2.Female\n3.N/A\nChoice:").upper()
                        generalUtils.createNewLine()
                        if gender == "MALE" or gender == "FEMALE" or gender == "N/A":
                            break
                        else:
                            continue
                    while True:
                        birthday = input("Birthday:(DD/MM/YYYY):").replace("/","-")
                        generalUtils.createNewLine()
                        if len(str(birthday)) == 10:
                            break
                        else:
                            continue
                    print(f"User ID:{userID}\nIC Number:{ICNumber}\nFull name:{fullName}\nEmail:{email}\nPhone Number:{phoneNumber}\nGender:{gender}\nBirthday:{birthday}")
                    while True:
                        print("Confirm to make change? Y/N")
                        choiceToMakeChange = input("Choice:").upper()
                        if choiceToMakeChange == "Y":
                            updateProfileAdmin("UserDetails.txt",userID,"ADMIN",password,ICNumber,formattedFullName,email,phoneNumber,birthday,gender)
                            print("Profile Updated")
                            break
                        elif choiceToMakeChange == "N":
                            print("Profile not updated")
                            break
                        else:
                            print("Invalid Input.Please try again.\n")
                        time.sleep(5)
                elif choice == 5:
                    print("Log Out")
                    return "LOGOUT"
                else:
                    continue






















