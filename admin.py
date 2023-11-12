def dminFile(filename,IDNumber,ICNUmber,fullName,contactNumber,gender,birthday)

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
            print("Menu:\n1.Register\n2.Fill Income\n3.Admin Profile")
            choice = int(input("1.Register\n2.Fill Income\n3.Admin Profile\nChoice:"))
            if choice == 1:
                print("Register:\n1.Receptionist\n2.Tutor")
                choiceRegister = int(input("1.Receptionist\n2.Tutor\nChoice:"))
                if choiceRegister == 1:
                    email = input("Email:")
                    password = input("Password:")

