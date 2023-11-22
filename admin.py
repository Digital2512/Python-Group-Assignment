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
                        print("Register Receptonist")
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
                    print("View Monthly Income")
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










