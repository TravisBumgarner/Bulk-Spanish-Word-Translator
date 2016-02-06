import csv, shutil, os

def newD(dict):
    #requires os module
    fileName, fileExtension = os.path.splitext(dict)
    if(os.path.isfile(dict)):
        print(dict + " already exists. Please enter a unique file name")
    elif(fileExtension != ".csv"):
        print(dict + " does not have .csv file extension.")
    else:
        newDict = open(dict,'w')

def openD(fileName):
    #requires csv module
    dictionaryFile = open(fileName)
    dictionaryReader = csv.reader(dictionaryFile)
    dictionaryData = list(dictionaryReader)
    return "Dictionary " + fileName + " was successfully opened. It's contents are " + str(dictionaryData)

def saveD():
    #I have no idea what this will do
    print("Yay!")

def appendD():
    #I have no idea what this will do
    print("Yay!")

def backupD(fileToBackup):
    #requires os
    backupFolder = ".\dictBackup"
    fileName, fileExtension = os.path.splitext(fileToBackup)

    i = 0
    newFileName = fileName + str(i) + fileExtension

    for folderName, subfolders, filenames in os.walk(backupFolder):
        while newFileName in filenames:
            i +=1 
            newFileName = fileName + str(i) + fileExtension
            if newFileName not in filenames:
                break
        return newFileName
   
def searchD(word,dictionary,col):
    #Which word to search for
    #Which dictionary to search in
    # Which column to search through
        # 0 = Spanish
        # 1 = English
        # 2-end to be defnied
    colToSearch = []
    for entry in dictionary:
        colToSearch.append(entry[col])
    if word in colToSearch:
        print("found")
    else:
        print("not found")
    
