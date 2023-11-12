import database
import generalUtils
import random

def readIDFromExistingFile(fileName, indexOfID):
    existingIDs = []
    with open(fileName,"r") as file:
        for line in file:
            values = line.strip().split(";")
            existingIDs.append(values[indexOfID])
    return existingIDs

def checkForDuplication(existingIDsList, idToCheck):
    return idToCheck in existingIDsList

def generateReceptionistID(existingIDs):
    maxNumber = 0
    for ID in existingIDs:
        if ID.startswith("R"):
            try:
                number = int(ID[1:])
                maxNumber = max(maxNumber, number)
            except ValueError:
                pass
    newNumber = maxNumber + 1
    formattedNewNumber = f"{newNumber:03d}"
    newTutorID = f"R{formattedNewNumber}"
    return newTutorID

def generateAdminID(existingIDs):
    maxNumber = 0
    for ID in existingIDs:
        if ID.startswith("A"):
            try:
                number = int(ID[1:])
                maxNumber = max(maxNumber, number)
            except ValueError:
                pass
    newNumber = maxNumber + 1
    formattedNewNumber = f"{newNumber:03d}"
    newTutorID = f"A{formattedNewNumber}"
    return newTutorID

def generateStudentID(existingIDs):
    maxNumber = 0
    for ID in existingIDs:
        if ID.startswith("S"):
            try:
                number = int(ID[1:])
                maxNumber = max(maxNumber, number)
            except ValueError:
                pass
    newNumber = maxNumber + 1
    formattedNewNumber = f"{newNumber:03d}"
    newTutorID = f"S{formattedNewNumber}"
    return newTutorID




def generateTutorID(existingIDs):
    maxNumber = 0
    for ID in existingIDs:
        if ID.startswith("T"):
            try:
                number = int(ID[1:])
                maxNumber = max(maxNumber, number)
            except ValueError:
                pass
    newNumber = maxNumber + 1
    formattedNewNumber = f"{newNumber:03d}"
    newTutorID = f"T{formattedNewNumber}"
    return newTutorID

