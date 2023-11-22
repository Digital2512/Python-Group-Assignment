import time
import UniqueIDCreation
import database
import generalUtils

#function update profile
def updateProfileAdmin(fileToCheck,IDNumber,role,password,ICNumber,fullName,email,phoneNumber,birthday,gender):
    updateProfileAdmin = False
    capitalizedRole = role.upper()
    update_data = []
    with open(fileToCheck,"+r") as file:
        for line in file:
            values = line.strip().split(";")
            if values[1] == str(IDNumber):
                updateProfileAdmin = True
                continue
            update_data.append(line)
    if updateProfileAdmin == True:
        update_data.append(f"{capitalizedRole};{IDNumber};{password};{ICNumber};{fullName};{email};{phoneNumber};{gender};{birthday}\n")
        with open(fileToCheck,"+r") as file:
            file.writelines(update_data)
    return updateProfileAdmin

#function register part
def registerReceptionist(userID,password):
    userProfile = f"RECEPTIONIST;{userID};{password}"
    return database.writeToFile("UserDetails.txt",userProfile)

def registerTutor(userID,password,subject):
    userProfile = f"TUTOR;{userID};{password};{subject}"
    return database.writeToFile("UserDetails.txt",userProfile)

#main code
def pgAdmin(userID):
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
                    generalUtils.clearConsole()
                    print("Register:\n1.Receptionist\n2.Tutor")
                    generalUtils.createNewLine()
                    choiceRegister = int(input("Choice:"))
                    if choiceRegister == 1:
                        print("Register Receptionist")
                        generalUtils.createNewLine()
                        userID = UniqueIDCreation.generateReceptionistID()
                        password = input("Password:")
                        registerReceptionist(userID,password)
                    elif choiceRegister == 2:
                        print("Register Tutor")
                        generalUtils.createNewLine()
                        userID = UniqueIDCreation.generateTutorID()
                        password = input("Password:")
                        subject = input("Subject:")
                        registerTutor(userID,password,subject)
                    else:
                        continue
                elif choice == 2:
                    generalUtils.clearConsole()
                    generalUtils.createNewLine()
                    print("View Monthly Income")
                    generalUtils.createNewLine()
                    print("Form 1")
                    form1Chinese = database.readListValue("CHF1",0,2,"subjectInfo.txt")
                    form1English = database.readListValue("ENG1",0,2,"subjectInfo.txt")
                    form1Malay = database.readListValue("MAF1",0,2,"subjectInfo.txt")
                    form1Math = database.readListValue("MTHF1",0,2,"subjectInfo.txt")
                    form1Addmath = database.readListValue("AMTHF1",0,2,"subjectInfo.txt")
                    form1GeneralCommerce = database.readListValue("GCF1",0,2,"subjectInfo.txt")
                    form1GeneralScience = database.readListValue("GSF1",0,2,"subjectInfo.txt")
                    print(f"Chinese:{form1Chinese}\nEnglish:{form1English}\nMalay:{form1Malay}\nMath:{form1Math}\nAddmath:{form1Addmath}\nGeneral Commerce:{form1GeneralCommerce}\nGeneral Science:{form1GeneralScience}\n")
                    generalUtils.createNewLine()
                    print("Form 2")
                    form2Chinese = database.readListValue("CHF2",0,2,"subjectInfo.txt")
                    form2English = database.readListValue("ENF2",0,2,"subjectInfo.txt")
                    form2Malay = database.readListValue("MAF2",0,2,"subjectInfo.txt")
                    form2Math = database.readListValue("MTHF2",0,2,"subjectInfo.txt")
                    form2Addmath = database.readListValue("AMTHF2",0,2,"subjectInfo.txt")
                    form2GeneralCommerce = database.readListValue("GCF2",0,2,"subjectInfo.txt")
                    form2GeneralScience = database.readListValue("GSF2",0,2,"subjectInfo.txt")
                    print(f"Chinese:{form2Chinese}\nEnglish:{form2English}\nMalay:{form2Malay}\nMath:{form2Math}\nAddmath:{form2Addmath}\nGeneral Commerce:{form2GeneralCommerce}\nGeneral Science:{form2GeneralScience}\n")
                    generalUtils.createNewLine()
                    print("Form 3")
                    form3Chinese = database.readListValue("CHF3",0,2,"subjectInfo.txt")
                    form3English = database.readListValue("ENF3",0,2,"subjectInfo.txt")
                    form3Malay = database.readListValue("MAF3",0,2,"subjectInfo.txt")
                    form3Math = database.readListValue("MTHF3",0,2,"subjectInfo.txt")
                    form3Addmath = database.readListValue("AMTHF3",0,2,"subjectInfo.txt")
                    form3GeneralCommerce = database.readListValue("GCF3",0,2,"subjectInfo.txt")
                    form3GeneralScience = database.readListValue("GSF3",0,2,"subjectInfo.txt")
                    print(f"Chinese:{form3Chinese}\nEnglish:{form3English}\nMalay:{form3Malay}\nMath:{form3Math}\nAddmath:{form3Addmath}\nGeneral Commerce:{form3GeneralCommerce}\nGeneral Science:{form3GeneralScience}")
                    generalUtils.createNewLine()
                    print("Form 4")
                    form4Chinese = database.readListValue("CHF4",0,2,"subjectInfo.txt")
                    form4English = database.readListValue("ENF4",0,2,"subjectInfo.txt")
                    form4Malay = database.readListValue("MAF4",0,2,"subjectInfo.txt")
                    form4Math = database.readListValue("MTHF4",0,2,"subjectInfo.txt")
                    form4Addmath = database.readListValue("AMTHF4",0,2,"subjectInfo.txt")
                    form4Accounting = database.readListValue("ACF4",0,2,"subjectInfo.txt")
                    form4Economics = database.readListValue("ECF4",0,2,"subjectInfo.txt")
                    form4Business = database.readListValue("BSF4",0,2,"subjectInfo.txt")
                    form4Physics = database.readListValue("PHF4",0,2,"subjectInfo.txt")
                    form4Chemistry = database.readListValue("CHMF4",0,2,"subjectInfo.txt")
                    form4Biology = database.readListValue("BIOF4",0,2,"subjectInfo.txt")
                    print(f"Chinese:{form4Chinese}\nEnglish:{form4English}\nMalay:{form4Malay}\nMath:{form4Math}\nAddmath:{form4Addmath}\nAccounting:{form4Accounting}\nEconomics:{form4Economics}\nBusiness:{form4Business}\nPhysics:{form4Physics}\nChemistry:{form4Chemistry}\nBiology:{form4Biology}\n")
                    generalUtils.createNewLine()
                    print("Form 5")
                    from5Chinese = database.readListValue("CHF5",0,2,"subjectInfo.txt")
                    form5English = database.readListValue("ENF5",0,2,"subjectInfo.txt")
                    form5Malay = database.readListValue("MAF5",0,2,"subjectInfo.txt")
                    form5Math = database.readListValue("MTHF5",0,2,"subjectInfo.txt")
                    form5Addmath = database.readListValue("AMTHF5",0,2,"subjectInfo.txt")
                    form5Accounting = database.readListValue("ACF5",0,2,"subjectInfo.txt")
                    form5Economics = database.readListValue("ECF5",0,2,"subjectInfo.txt")
                    form5Business = database.readListValue("BSF5",0,2,"subjectInfo.txt")
                    form5Physics = database.readListValue("PHF5",0,2,"subjectInfo.txt")
                    form5Chemistry = database.readListValue("CHMF5",0,2,"subjectInfo.txt")
                    form5Biology = database.readListValue("BIOF5",0,2,"subjectInfo.txt")
                    print(f"Chinese:{from5Chinese}\nEnglish:{form5English}\nMalay:{form5Malay}\nMath:{form5Math}\nAddmath:{form5Addmath}\nAccounting:{form5Accounting}\nEconomics:{form5Economics}\nBusiness:{form5Business}\nPhysics:{form5Physics}\nChemistry:{form5Chemistry}\nBiology:{form5Biology}\n")
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










