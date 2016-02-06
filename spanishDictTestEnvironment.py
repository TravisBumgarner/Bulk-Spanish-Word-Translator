import csv, shutil, os

#Loop through and print out each of the spanish words
'''
spanishWords = []
for word in exampleData:
    spanishWords.append(word[0])
if "perro" in spanishWords:
    print("found")
'''

def openDictionary(fileName):
    
    #requires csv module
    dictionaryFile = open(fileName)
    dictionaryReader = csv.reader(dictionaryFile)
    dictionaryData = list(dictionaryReader)
    return "Dictionary " + fileName + " was successfully opened."

def backupDictionary(fileToBackup):
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

            
        

            
            
    
    #requires shutil module
'''>>> import os
>>> filename, file_extension = os.path.splitext('/path/to/somefile.ext')
>>> filename
'/path/to/somefile'
>>> file_extension
'.ext'
'''
    

def dictionarySearch(word,dictionary,col):
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
    
