import database
import generalUtils

def update_profile(student,name,ID,password,IC_num,birthday,email):
    updated_data= []

    with open(student,"r") as file:
        line= [line.rstrip() for line in file]
        for line in line:
            student_data = line.split(";")
            if student_data and student_data[1] ==str(ID):
                updated_data.append(f"{name};{ID};{password};{IC_num};{birthday};{email}\n")
            else:
                updated_data.append(line)


    with open(student,"w") as file:
        file.writelines(updated_data)
        name = input("Please enter your name:")
        password = input("Please enter your password:")
        IC_num = input("Please enter your IC num:")
        birthday= input("Please enter your birthday:")
        email=input("Please enter your email:")
        file.writelines(updated_data)

student_file= "User.Details.txt"
update_profile(student_file, name, ID, password, IC_num,birthday,email)

