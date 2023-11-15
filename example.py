import UniqueIDCreation
import database
import generalUtils


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


def registerReceptionist(userID, password):
    userProfile = f"RECEPTIONIST;{userID};{password}"
    return database.writeToFile("UserDetails.txt", userProfile)

def registerTutor(userID, password, subject):
    userProfile = f"TUTOR;{userID};{password};{subject}"
    return database.writeToFile("UserDetails.txt", userProfile)


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
                print("Menu:\n1. Register\n2. View Income\n3. View Profile\n4. Update Profile\n5. Log Out")
                choice = int(input("\nChoice:"))
                if choice == 1:
                    print("Register")
                    while True:
                        print("Register:\n1.Receptionist\n2.Tutor")
                        choiceRegister = int(input("1.Receptionist\n2.Tutor\nChoice:"))
                        if choiceRegister == 1:
                            userID = UniqueIDCreation.generateReceptionistID()
                            password = input("Password:")
                            registerReceptionist(userID,password)
                        elif choiceRegister == 2:
                            userID = UniqueIDCreation.generateTutorID()
                            password = input("Password: ")
                            subject = input("Subject: ")
                            registerReceptionist(userID, password, subject)
                        else:
                            continue
                elif choice == 2:
                    print("View Income")
                elif choice == 3:
                    print("View Profile")
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
                elif choice == 4:
                    print("Update Profile")
                    password = input("Password: ")
                    ICNumber = int(input("\nIC Number: "))
                    fullName = input("\nFull name: ")
                    formattedFullName = fullName.replace(" ", "_")
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
                        birthday = input("Birthday(DD/MM/YYYY): ").replace("/", "-")
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
                            updateProfile("UserDetails.txt", userID, "ADMIN", password, ICNumber, formattedFullName, email,phoneNumber, birthday, gender)
                                print("Profile Updated")
                                break
                        elif confirmationChoice == "N":
                            print("Profile not updated")
                            break
                        else:
                            print("Invalid Input!\n")
                        time.sleep(5)
                elif choice == 5:
                    print("Log Out")
                    return "LOGOUT"
                else:
                    continue










