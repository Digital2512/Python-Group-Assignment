#register part
#tutor
print("Admin Page")
registerWho = int(input("1. Register Receptionist \n2. Register Tutor"))
if registerWho == 1:
    print("Register Receptionist")
    receptionistID = int(input("Receptionist ID: "))
    email = input("Email: ")
    username = input("Username: ")
    password = input("Password: ")
    receptionistString = f"{receptionistID};RECEPTIONIST;{email};{username};{password};"
elif registerWho:
    print("Register ")
    tutorID = int(input("Tutor ID: "))
    email = input("Email: ")
    username = input("Username: ")
    password = input("Password: ")
    tutorString = f"{tutorID};TUTOR;{email};{username};{password};"

def inputToFile(filename,string):
    with open (filename,"a"):
        filename.append()


