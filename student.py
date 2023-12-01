import generalUtils
import database
import UniqueIDCreation
import time

def send_request(requestID, studentID, studentName, currentSubject, requestSubject,fileName):
    f = open (fileName,"a")
    f.write(f"{requestID};{studentID};{studentName};{currentSubject};{requestSubject}")
    return True
    f.close()

def delete_request (requestID, fileName):
    deleted = False
    f = open(fileName,"r")
    request = f.readlines()

    for requests in request:
        values = requests.strip().split(",")
        if values[0] == requestID:
            deleted = True
            continue
        else:
            f.write(requests)
    return deleted
    f.close()


def studentpage(studentID):
    while True:
        generalUtils.clearConsole()
        generalUtils.createNewLine()
        with open("UserDetails.txt", "+r") as file:
            for line in file:
                values = line.strip().split(",")
                if values[1] == studentID:
                    Name = values[3].replace("_", "")
                    print(f"Hello {Name},({values[0]})")
        generalUtils.createNewLine()
        while True:
            print("\nMenu:","\n-------------")
            print("1. View Schedule","\n2. Request change subject","\n3. Delete request","\n4. Update profile", "\n5. Exit")
            option = input("Enter your option:")
            if option == "1":
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("View Class Schedule")
            elif option == "2":
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Send request to change subject")
                generalUtils.createNewLine()
                existingIDs = UniqueIDCreation.readIDFromExistingFile("StudentRequest.txt", 0)
                requestID = UniqueIDCreation.generateRequestID(existingIDs)
                with open("UserDetails.txt","a") as file:
                    for line in file:
                        values = line.strip().split(",")
                        if values[1] == studentID:
                            studentName = values[4]
                currentSubject = input("Please enter your current subject:")
                requestSubject = input("Please enter your request subject:")
                send_request(requestID, studentID, studentName, currentSubject, requestSubject,"StudentRequest.txt")

            elif option == "3":
                print("Delete request")


            elif option == "4":
                print("Update profile")
                ID = input("ID Number: ")
                name = input("Please enter your name:")
                password = input("Please enter your password:")
                IC_num = input("Please enter your IC num:")
                email = input("Please enter your email:")
                while True:
                    birthday = input("Please enter your birthday(DD/MM/YYYY):")
                    birthday = birthday.replace("/", "-")
                    print(len(str(birthday)))
                    if len(str(birthday)) == 10:
                        break
                    else:
                        continue
                print(f"ID: {ID}\nName: {name}\nPassword:{password}\nIC number:{IC_num}\nEmail:{email}")




            elif option == "5":
                print("Exit student page")
                break
            else:
                print("Invalid option. Please choose again.")

studentpage("S003")




