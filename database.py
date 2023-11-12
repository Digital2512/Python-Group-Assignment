import generalUtils

def convertFileToString(fileName, list):
    #Fuction to convert any file into a 1D list 
    with open(fileName, "+a") as appendedFile:
        appendedFile.write(generalUtils.listToString(list))
    return appendedFile

def writeToFile(fileName, stringVariable):
    #Function to write the string into the file 
    with open(fileName, "+a") as writtenFile: 
        writtenFile.write(stringVariable)

def overwriteFile(fileName, stringVariable):
    #Function to overwrite the file with the string variable
    with open(fileName, "+w") as file:
        file.write(stringVariable)
        
def readFile(fileName):
    list=[]
    with open(fileName, "+r") as file:
        for line in file:
            list.append(line.strip().split(";"))
    return list

def searchListValue(inputString,  indexToSearch, listToCheck):
    #check if the input string matches the item in the list at a specific index
    for item in listToCheck:
        if inputString == item[indexToSearch]:
            return True
    return False

def readListValue(valueInput, indexToCheck, indexToRead, listToCheck):
    #read a specific value from the list
    with open(listToCheck, "+r") as file:
        for line in file:
            values = line.strip().split(";")
            if 0 <= indexToRead < len(values): 
                if values[indexToCheck] == valueInput:
                    return values[indexToRead]
            else: 
                return "Index Out Of Bound"

def checkForDuplicates(filename, stringToCheck,indexToCheck):
    duplicateFound = 0
    with open(filename, "+r") as file:
        for line in file:
            values = line.strip().split(";")
            if values[indexToCheck] == stringToCheck:
                duplicateFound += 1
                if duplicateFound >= 2:
                    return True
            else: 
                continue
    return False
