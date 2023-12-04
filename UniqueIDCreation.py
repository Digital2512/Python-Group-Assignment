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
    newReceptionistID = f"R{formattedNewNumber}"
    return newReceptionistID

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
    newStudentID = f"A{formattedNewNumber}"
    return newStudentID

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
    newStudentID = f"S{formattedNewNumber}"
    return newStudentID

def generateRequestID(existingIDs):
    maxNumber = 0
    for ID in existingIDs:
        if ID.startswith("REQ"):
            try:
                number = int(ID[3:])
                maxNumber = max(maxNumber, number)
            except ValueError:
                pass
    newNumber = maxNumber + 1
    formattedNewNumber = f"{newNumber:03d}"
    newRequestID = f"REQ{formattedNewNumber}"
    return newRequestID

def generatePaymentID(existingIDs):
    maxNumber = 0
    for ID in existingIDs:
        if ID.startswith("P"):
            try:
                number = int(ID[1:])
                maxNumber = max(maxNumber, number)
            except ValueError:
                pass
    newNumber = maxNumber + 1
    formattedNewNumber = f"{newNumber:03d}"
    newPaymentID = f"P{formattedNewNumber}"
    return newPaymentID

def generateReceiptID(existingIDs):
    maxNumber = 0
    for ID in existingIDs:
        if ID.startswith("REC"):
            try:
                number = int(ID[3:])
                maxNumber = max(maxNumber, number)
            except ValueError:
                pass
    newNumber = maxNumber + 1
    formattedNewNumber = f"{newNumber:03d}"
    newReceiptID = f"REC{formattedNewNumber}"
    return newReceiptID

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