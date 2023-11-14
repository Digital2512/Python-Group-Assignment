import database
import generalUtils


def update_profile(student, name, ID, password, IC_num, birthday, email):
    updated_data = []

    with open(student, "r") as file:
        line = [line.rstrip() for line in file]
        for line in line:
            student_data = line.split(";")
            if student_data and student_data[1] == str(ID):
                updated_data.append(f"{name};{ID};{password};{IC_num};{birthday};{email}\n")
            else:
                updated_data.append(line)

    with open(student, "w") as file:
        file.writelines(updated_data)



ID = input("ID Number: ")
name = input("Please enter your name:")
password = input("Please enter your password:")
IC_num = input("Please enter your IC num:")
email = input("Please enter your email:")
while True:
    birthday = input("Please enter your birthday(DD/MM/YYYY):")
    birthday = birthday.replace("/","-")
    print(len(str(birthday)))
    if len(str(birthday))==10:
        break
    else:
        continue

student_file = "userDetails.txt"
update_profile(student_file, name, ID, password, IC_num, birthday, email)
