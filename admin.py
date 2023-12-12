import UniqueIDCreation
import database
import generalUtils
import time


def updateAdminProfile(fileToCheck, IDNumber, role, password, ICNumber, fullName, email, phoneNumber, birthday, gender):
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

def registerReceptionist(userID, password):
    # {capitalizedRole};{IDNumber};{password};{ICNumber};{fullName};{email};{phoneNumber};{gender};{birthday}
    userProfile = f"RECEPTIONIST;{userID};{password};N/A;N/A;N/A;N/A;N/A;N/A;N/A;\n"
    return database.writeToFile("UserDetails.txt", userProfile)

def registerTutor(userID, password, subject, numberOfSubjects):
    # {capitalizedRole};{IDNumber};{password};{ICNumber};{fullName};{email};{phoneNumber};{gender};{birthday};{numberOfSubjects};{subject}
    userProfile = f"TUTOR;{userID};{password};N/A;N/A;N/A;N/A;N/A;N/A;N/A;{numberOfSubjects};{subject};\n"
    return database.writeToFile("UserDetails.txt", userProfile)


def readSubjectCode(fileName, indexOfSubjectCode):
    subjectCode = []
    with open(fileName, "r") as file:
        for line in file:
            values = line.strip().split(";")
            subjectCode.append(values[indexOfSubjectCode])
    return subjectCode

def pgAdmin(userID):
    subjectCode = readSubjectCode("SubjectsInfo.txt", 0)
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
        print("1.Register\n2.View Income\n3.View Admin Profile\n4.Update Admin Profile\n5.Log Out")
        generalUtils.createNewLine()
        choice = input("Choice:")
        if choice == "1":
            existingIDs = UniqueIDCreation.readIDFromExistingFile("UserDetails.txt",0)
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("Register:")
            generalUtils.createNewLine()
            print("1.Receptionist\n2.Tutor\n3.Exit")
            generalUtils.createNewLine()
            choiceRegister = input("Choice:")
            if choiceRegister == "1":
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Register Receptonist")
                generalUtils.createNewLine()
                existingIDs = UniqueIDCreation.readIDFromExistingFile("UserDetails.txt", 1)
                receptionistUserID = UniqueIDCreation.generateReceptionistID(existingIDs)
                print(f"Receptionist ID: {receptionistUserID}\n")
                password = input("Password:")
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print(f"Profile\n\nUser ID: {receptionistUserID}\nPassword: {password}")
                generalUtils.createNewLine()
                while True: 
                    confirmationChoice = input("Is this correct(Y/N?)").upper()
                    if confirmationChoice == "Y":
                        registerReceptionist(receptionistUserID,password)
                        print("\nReceptionist registered")
                        time.sleep(3)
                        break
                    elif confirmationChoice == "N":
                        print("\nReceptionist not registered")
                        time.sleep(3)
                        break
                    else: 
                        continue
                generalUtils.clearConsole()
            elif choiceRegister == "2":
                listOfSubject = []
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Register Tutor")
                generalUtils.createNewLine()
                existingIDs = UniqueIDCreation.readIDFromExistingFile("UserDetails.txt", 1)
                tutorUserID = UniqueIDCreation.generateTutorID(existingIDs)
                print(f"Tutor ID: {tutorUserID}\n")
                password = input("Password:")
                numberOfSubjects = int(input("\nNumber of Subjects: "))
                generalUtils.createNewLine()
                while len(listOfSubject) != numberOfSubjects: 
                    while True:
                        print("Choose the subjects: ")
                        generalUtils.createNewLine()
                        print("Chinese - CHF1\nEnglish - ENF1\nMalay- MAF1\nMathemathics - MTHF1\nAdditional Mathemathics - AMTHF1\nGeneral Commerce - GCF1\nGeneral Science - GSF1\nnChinese - CHF2\nEnglish - ENF2\nMalay- MAF2\nMathemathics - MTHF2\nAdditional Mathemathics - AMTHF2\nGeneral Commerce - GCF2\nGeneral Science - GSF2\nChinese - CHF3\nEnglish - ENF3\nMalay- MAF3\nMathemathics - MTHF3\nAdditional Mathemathics - AMTHF3\nGeneral Commerce - GCF3\nGeneral Science - GSF3\nChinese - CHF4\nEnglish - ENF4\nMalay - MAF4\nMathemathics - MTHF4\nAdditional Mathemathics - AMTHF4\nAccounting - ACF4\nEconomics - ECF4\nBusiness Studies - BSF4\nPhysics - PHF4\nChemistry - CHMF4\nBiology - BIOF4\nChinese - CHF5\nEnglish - ENF5\nMalay - MAF5\nMathemathics - MTHF5\nAdditional Mathemathics - AMTHF5\nAccounting - ACF5\nEconomics - ECF5\nBusiness Studies - BSF5\nPhysics - PHF5\nChemistry - CHMF5\nBiology - BIOF5")
                        generalUtils.createNewLine()
                        subject = input("Subject Code: ").upper()
                        if subject in subjectCode:
                            if not subject in listOfSubject:
                                listOfSubject.append(subject)
                            else:
                                print("Error: Subject has already been chosen")
                                time.sleep(2)
                            break
                        else:
                            print("\nError: Subject code not found")
                            time.sleep(2)
                            continue
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print(f"Profile\n\nUser ID: {tutorUserID}\nPassword: {password}\nNumber of Subjects: {numberOfSubjects}\nSubjects: {listOfSubject}")
                generalUtils.createNewLine()
                while True: 
                    confirmationChoice = input("Is this correct(Y/N?)").upper()
                    if confirmationChoice == "Y":
                        registerTutor(tutorUserID,password,listOfSubject, numberOfSubjects)
                        print("\nTutor Registered")
                        time.sleep(3)
                        break
                    elif confirmationChoice == "N":
                        print("\nTutor not registered")
                        time.sleep(3)
                        break
                    else: 
                        continue
                generalUtils.clearConsole()
            elif choiceRegister == "3":
                break
            else:
                continue
        elif choice == "2":
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("View Monthly Income")
            generalUtils.createNewLine()
            print("Form 1")
            generalUtils.createNewLine()
            form1Chinese = database.readListValue("CHF1",0,3,"SubjectsInfo.txt")
            form1English = database.readListValue("ENF1",0,3,"SubjectsInfo.txt")
            form1Malay = database.readListValue("MAF1",0,3,"SubjectsInfo.txt")
            form1Mathemathics = database.readListValue("MTHF1",0,3,"SubjectsInfo.txt")
            form1AdditionalMathemathics = database.readListValue("AMTHF1",0,3,"SubjectsInfo.txt")
            form1GeneralCommerce = database.readListValue("GCF1",0,3,"SubjectsInfo.txt")
            form1GeneralScience = database.readListValue("GSF1",0,3,"SubjectsInfo.txt")
            print(f"Chinese: {form1Chinese}\nEnglish: {form1English}\nMalay: {form1Malay}\nMathemathics: {form1Mathemathics}\nAdditional Mathemathics: {form1AdditionalMathemathics}\nGeneral Commerce: {form1GeneralCommerce}\nGeneral Science: {form1GeneralScience}")
            generalUtils.createNewLine()
            print("Form 2")
            generalUtils.createNewLine()
            form2Chinese = database.readListValue("CHF2",0,3,"SubjectsInfo.txt")
            form2English = database.readListValue("ENF2",0,3,"SubjectsInfo.txt")
            form2Malay = database.readListValue("MAF2",0,3,"SubjectsInfo.txt")
            form2Mathemathics = database.readListValue("MTHF2",0,3,"SubjectsInfo.txt")
            form2AdditionalMathemathics = database.readListValue("AMTHF2",0,3,"SubjectsInfo.txt")
            form2GeneralCommerce = database.readListValue("GCF2",0,3,"SubjectsInfo.txt")
            form2GeneralScience = database.readListValue("GSF2",0,3,"SubjectsInfo.txt")
            print(f"Chinese: {form2Chinese}\nEnglish: {form2English}\nMalay: {form2Malay}\nMathemathics: {form2Mathemathics}\nAdditional Mathemathics: {form2AdditionalMathemathics}\nGeneral Commerce: {form2GeneralCommerce}\nGeneral Science: {form2GeneralScience}")
            generalUtils.createNewLine()
            print("Form 3")
            generalUtils.createNewLine()
            form3Chinese = database.readListValue("CHF3",0,3,"SubjectsInfo.txt")
            form3English = database.readListValue("ENF3",0,3,"SubjectsInfo.txt")
            form3Malay = database.readListValue("MAF3",0,3,"SubjectsInfo.txt")
            form3Mathemathics = database.readListValue("MTHF3",0,3,"SubjectsInfo.txt")
            form3AdditionalMathemathics = database.readListValue("AMTHF3",0,3,"SubjectsInfo.txt")
            form3GeneralCommerce = database.readListValue("GCF3",0,3,"SubjectsInfo.txt")
            form3GeneralScience = database.readListValue("GSF3",0,3,"SubjectsInfo.txt")
            print(f"Chinese: {form3Chinese}\nEnglish: {form3English}\nMalay: {form3Malay}\nMathemathics: {form3Mathemathics}\nAdditional Mathemathics: {form3AdditionalMathemathics}\nGeneral Commerce: {form3GeneralCommerce}\nGeneral Science: {form3GeneralScience}")
            generalUtils.createNewLine()
            print("Form 4")
            generalUtils.createNewLine()
            form4Chinese = database.readListValue("CHF4",0,3,"SubjectsInfo.txt")
            form4English = database.readListValue("ENF4",0,3,"SubjectsInfo.txt")
            form4Malay = database.readListValue("MAF4",0,3,"SubjectsInfo.txt")
            form4Mathemathics = database.readListValue("MTHF4",0,3,"SubjectsInfo.txt")
            form4AdditionalMathemathics = database.readListValue("AMTHF4",0,3,"SubjectsInfo.txt")
            form4Accounting = database.readListValue("ACF4",0,3,"SubjectsInfo.txt")
            form4Economics = database.readListValue("ECF4",0,3,"SubjectsInfo.txt")
            form4BusinessStudies = database.readListValue("BSF4",0,3,"SubjectsInfo.txt")
            form4Physics = database.readListValue("PHF4",0,3,"SubjectsInfo.txt")
            form4Chemistry = database.readListValue("CHMF4",0,3,"SubjectsInfo.txt")
            form4Biology = database.readListValue("BIOF4",0,3,"SubjectsInfo.txt")
            print(f"Chinese: {form4Chinese}\nEnglish: {form4English}\nMalay: {form4Malay}\nMathemathics: {form4Mathemathics}\nAdditional Mathemathics: {form4AdditionalMathemathics}\nAccounting: {form4Accounting}\nEconomics: {form4Economics}\nBusiness Studies: {form4BusinessStudies}\nPhysics: {form4Physics}\nChemistry: {form4Chemistry}\nBiology: {form4Biology}")
            generalUtils.createNewLine()
            print("Form 5")
            generalUtils.createNewLine()
            form5Chinese = database.readListValue("CHF5",0,3,"SubjectsInfo.txt")
            form5English = database.readListValue("ENF5",0,3,"SubjectsInfo.txt")
            form5Malay = database.readListValue("MAF5",0,3,"SubjectsInfo.txt")
            form5Mathemathics = database.readListValue("MTHF5",0,3,"SubjectsInfo.txt")
            form5AdditionalMathemathics = database.readListValue("AMTHF5",0,3,"SubjectsInfo.txt")
            form5Accounting = database.readListValue("ACF5",0,3,"SubjectsInfo.txt")
            form5Economics = database.readListValue("ECF5",0,3,"SubjectsInfo.txt")
            form5BusinessStudies = database.readListValue("BSF5",0,3,"SubjectsInfo.txt")
            form5Physics = database.readListValue("PHF5",0,3,"SubjectsInfo.txt")
            form5Chemistry = database.readListValue("CHMF5",0,3,"SubjectsInfo.txt")
            form5Biology = database.readListValue("BIOF5",0,3,"SubjectsInfo.txt")
            print(f"Chinese: {form5Chinese}\nEnglish: {form5English}\nMalay: {form5Malay}\nMathemathics: {form5Mathemathics}\nAdditional Mathemathics: {form5AdditionalMathemathics}\nAccounting: {form5Accounting}\nEconomics: {form5Economics}\nBusiness Studies: {form5BusinessStudies}\nPhysics: {form5Physics}\nChemistry: {form5Chemistry}\nBiology: {form5Biology}")
            generalUtils.createNewLine()
            while True:
                doneViewingChoice = input("Are you done viewing(Y/N)? ").upper()
                if doneViewingChoice == "Y":
                    break
                elif doneViewingChoice == "N":
                    continue
                else:
                    print("\nInvalid Choice")
                    generalUtils.createNewLine()
                    continue
            generalUtils.clearConsole()
        elif choice == "3":
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("View Admin Profile")
            generalUtils.createNewLine()
            ICNumber = database.readListValue(userID,1,3,"UserDetails.txt")
            fullName = database.readListValue(userID,1,4,"UserDetails.txt").replace("_"," ")
            email = database.readListValue(userID,1,5,"UserDetails.txt")
            phoneNumber = database.readListValue(userID,1,6,"UserDetails.txt")
            gender = database.readListValue(userID,1,7,"UserDetails.txt")
            birthday = database.readListValue(userID,1,8,"UserDetails.txt")
            print(f"User ID:{userID}\nIC Number:{ICNumber}\nFull name:{fullName}\nEmail:{email}\nPhone Number:{phoneNumber}\nGender:{gender}\nBirthday:{birthday}")
            generalUtils.createNewLine()
            while True:
                doneViewing = input("Are you done viewing(Y/N)?").upper()
                if doneViewing == "Y":
                    break
                elif doneViewingChoice == "N":
                    continue
                else:
                    print("\nInvalid Choice")
                    generalUtils.createNewLine()
                    continue
            generalUtils.clearConsole()
        elif choice == "4":
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("Update Admin Profile")
            generalUtils.createNewLine()
            print("1. Update Admin Profile\n2. Exit")
            generalUtils.createNewLine()
            updateProfileChoice = input("Choice: ")
            if updateProfileChoice == "1":
                password = input("\nPassword:")
                email = input("\nEmail:")
                fullName = input("\nFull Name:")
                formattedFullName = fullName.replace(" ","_")
                ICNumber = int(input("\nIC Number:"))
                phoneNumber = int(input("\nPhone Number:"))
                generalUtils.createNewLine()
                while True:
                    print("Gender:")
                    generalUtils.createNewLine()
                    print("1. Male\n2. Female\n3. N/A")
                    generalUtils.createNewLine()
                    gender = input("Choice:").upper()
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
                    generalUtils.createNewLine()
                    choiceToMakeChange = input("Is this correct(Y/N)? ").upper()
                    if choiceToMakeChange == "Y":
                        updateAdminProfile("UserDetails.txt",userID,"ADMIN",password,ICNumber,formattedFullName,email,phoneNumber,birthday,gender)
                        print("\nProfile Updated")
                        break
                    elif choiceToMakeChange == "N":
                        print("\nProfile not updated")
                        break
                    else:
                        print("\nInvalid Input. Please try again.\n")
                    time.sleep(5)
                    generalUtils.clearConsole()
            elif updateProfileChoice == "2":
                break
            else:
                continue
        elif choice == "5":
            print("Log Out")
            return "LOGOUT"
        else:
            continue






















