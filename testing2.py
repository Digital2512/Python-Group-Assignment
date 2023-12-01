import generalUtils
import database
import UniqueIDCreation
import time

def send_request(requestID,studentID,studentName,currentSubject,requestSubject,fileName):
    with open (fileName,"+a") as file:
        file.write(f"{requestID};{studentID};{studentName};{currentSubject};{requestSubject}")
        return True

def delete_request(requestID,fileName):
    deleted = False
    with open (fileName,"+r") as file:
        request = file.readlines()

        for requests in request:
            values= requests.strip().split(";")
            if values[0] == requestID:
                deleted = True
                continue
            else:
                file.write(requests)
        return deleted

def update_profile(fileToCheck,role,studentID,studentName,password,ICnum,birthday,email):
    updateProfile = False
    updated_data =[]
    with open(fileToCheck,"+r") as file:
        data = file.readlines()

        for datas in data:
            values= datas.strip().split(";")
            if values[1] == studentID:
                updateProfile = True
                continue
                updated_data.append(datas)
    if updateProfile == True:
        updated_data.append(f"{role},{studentID},{studentName},{password},{ICnum},{birthday};{email};{birthday}\n")

        with open(fileName,"w") as file:
            file.writelines(updated_data)
    return updateProfile



def studentPage(studentID):
    while True:
        generalUtils.clearConsole()
        generalUtils.createNewLine()
        with open ("UserDetails.txt","+r") as file:
            for line in file:
                values = line.strip().split(";")
                if values[1] == studentID:
                    Name = values[3].replace ("_","")
                    print(f"Hello {Name}, ({values[0]})")
        generalUtils.createNewLine()
        while True:
            print("\nMenu:","\n-----------------")
            print("1. View Schedule","\n2. Request change subject","\n3. Delete request","\n4. View payment","\n5. Update profile", "\n6. Exit")
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
                existingIDs = UniqueIDCreation.readIDFromExistingFile("StudentRequest.txt",0)
                requestID = UniqueIDCreation.generateRequestID(existingIDs)
                with open("UserDetails.txt","+a") as file:
                    for line in file:
                        values = line.strip().split(";")
                        if values[1] == studentID:
                            studentName = values[3].replace ("-","")
                currentSubject = input("Please enter your current subject:")
                requestSubject = input("Please enter your request subject:")
                send_request(requestID,studentID,studentName,currentSubject,requestSubject,"StudentRequest.txt")
            elif option == "3":
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Delete request")
                generalUtils.createNewLine()
                deleteRequestID = input("RequestID:")
                if delete_request(deleteRequestID,"StudentRequest.txt") == True:
                    print("Request deleted.")
                else:
                    print("Request not deleted.")
            elif option == "4":
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("View Payment Status")
                generalUtils.createNewLine()





            elif option == "5":
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Update profile")
                generalUtils.createNewLine()
                studentName = input("Please enter your name:")
                password = input("Please enter your password:")
                ICnum = input("Please enter your IC num:")
                email = input("Please enter your email:")
                while True:
                    birthday = input("Please enter your birthday(DD\MM\YYYY):")
                    birthday = birthday.replace("/","-")
                    print(len(str(birthday)))
                    if len(str(birthday)) == 10:
                        break
                    else:
                        continue
                print(f"Student ID:{studentID}\nStudent Name: {studentName}\nPassword: {password}\nIC num: {ICnum}\nEmail: {email}\nBirthday: {birthday}\n")
                while True:
                    print("Is this profile correct? Y/N ")
                    confirm =  input("Choice:").upper()
                    if confirm == "Y":
                        if update_profile("UserDetails.txt", "Student",studentID,studentName,password,ICnum,email,birthday) == True:
                            print("Profile Updated Successful.")
                            break
                    elif confirm =="N":
                        print("Profile Updated Unsuccessful.")
                        break
                    else:
                        print("Invalid choice")
                    time.sleep(5)
            elif option == "6":
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Exit student page")
                break
            else:
                generalUtils.clearConsole()
                generalUtils.createNewLine()
                print("Invalid option.Please choose again.")










