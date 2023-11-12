def listToString(list):
    string = ''
    for i in range(0, len(list), 1):
        if (i == (len(list)-1)):
            string = string + str(list(i)) + "\n"
        else:
            string = string+str(list(i))+";"
    return string

def clearConsole():
        #Function to clear console
        print("\n"*200)

def createNewLine():
    #Function to create a new line for the GUI
    print("="*50)

