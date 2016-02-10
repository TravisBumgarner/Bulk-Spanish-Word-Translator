import csv, shutil, os

def newD():
    return {}

def openD(fileName):
    #requires csv module
    dictionaryFile = open(fileName)
    dictionaryReader = csv.reader(dictionaryFile)
    dictionaryData = list(dictionaryReader)
    return "Dictionary " + fileName + " was successfully opened. It's contents are " + str(dictionaryData)

def saveD():
    #I have no idea what this will do
    print("Yay!")
    #dictLayout = {'spanishWord':['eng word',['forms','seem','of','word'],'timesSeen']}

def appendListD(dictionary, spanishWordList, englishWordList, seenWordList):
    #adds new entries found to dictionary
    #don't set equation equal to anything. Takes in dictionary and returns 
    def appendD(dictionary,spanishWord,englishWord,seenWord):
        timesSeen = 1
        dictionary[spanishWord] = [englishWord, [seenWord], timesSeen]
        return dictionary
        
    for index in range(len(spanishWordList)):
        appendD(dictionary, spanishWordList[index], englishWordList[index], seenWordList[index])
    
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

def printPrettyD(dictionary):
    for i in dictionary:
        stringOfSeen = ""
        for j in dictionary[i][1]:
            stringOfSeen += " " + j
        print("The word \"" + i + "\" in English is \"" + dictionary[i][0] + "\". It has been seen " + str(dictionary[i][2]) + " times, as" + stringOfSeen + ".")
        
