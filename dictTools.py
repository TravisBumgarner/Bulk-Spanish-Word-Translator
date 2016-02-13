import pickle #used for file handling
import os #used for backing up files

class dt():
    def __init__(self):
        #Starts with a blank dictionary
        self.dictionary = {}
        
    def openD(self,fileName):
        #Use pickle to open file
        try:
            self.dictionary = pickle.load(open(fileName,"rb"))
        except FileNotFoundError:
            print("File does not exist.")
        except pickle.UnpicklingError:
            print("Not valid pickle file.")

    def saveD(self,fileName):
        #Use pickle to save file
        pickle.dump(self.dictionary,open(fileName,"wb"))

    def modifyEntryD(self, spanishWord, seenWord):
        try:
            #Add new
            #Dictionary format:
            # self.dictionary[spanishWord] = [englishWord, [seenWord],timesSeen]
            entry = self.dictionary[spanishWord]
            #If form of word seen isn't in entries, append.
            if seenWord not in entry[1]:
                entry[1].append(seenWord)
            #Update counter.
            entry[2] += 1
        except KeyError:
            print("The word " + spanishWord + " was not found in the dictionary.")
        
    def newEntryD(self,searchResults):
        def appendEachD(seenWord,spanishWord,englishWord):
            timesSeen = 1
            self.dictionary[spanishWord] = [englishWord, [seenWord],timesSeen]
            #return dictionary
            #pretty sure I don't need this anymore
        for result in searchResults:
            appendEachD(result[0],
                        result[1],
                        result[2])

    def genFileName(self,fileName,filePath):
        #Generates unique filenames
        fname, fextension = os.path.splitext(fileName)
        i = 0
        newFileName = fname + str(i) + fextension
        for folderName,subfolders, filenames in os.walk(filePath):
            while newFileName in filenames:
                i += 1
                newFileName = fname + str(i) + fextension
                if newFileName not in filenames:
                    break
            return newFileName

    def backupD(self,fileName):
        backupFolder = ".\\dictBackup"
        #Makes backup folder if it doesn't exist
        if not os.path.exists(backupFolder):
            os.makedirs(backupFolder)
        #Used for creating unique filenames for each time saved
        pickle.dump(self.dictionary,open(backupFolder + "\\" + self.genFileName(fileName,backupFolder),"wb"))

    def searchD(self,word):
        try:
            #Creates list of forms seen of the word.
            formsSeenStr = ', '.join(self.dictionary[word][1])
            print("The word \"" + word
                  + "\" in English is \"" + self.dictionary[word][0]
                  + "\". It has been seen " + str(self.dictionary[word][2])
                  + " times, as "+ formsSeenStr + ".")
        except KeyError:
            print("The word " + word + " was not found in the dictionary.")

    def printD(self):
        print(self.dictionary)
        print("Spanish Word".center(30,"-") + "|" +
              "English Word".center(30,"-") + "|" +
              "Words Seen".center(70,"-") + "|" +
              "Times Seen".center(15,"-"))
        for each in self.dictionary:
            print(each.ljust(30) + "|" +
                  self.dictionary[each][0].ljust(30) + "|" + 
                  str(self.dictionary[each][1]).ljust(70) + "|" +
                  str(self.dictionary[each][2]).ljust(15))
            
    def ankiExportD(self,fileName):
        exportFolder = ".\\ankiExport"
        #Makes export folder if it doesn't exist
        if not os.path.exists(exportFolder):
            os.makedirs(exportFolder)
        #Used for creating unique filenames for each time save
        fileAndDir = exportFolder + "\\" + self.genFileName(fileName,exportFolder)
        writeToFile = open(fileAndDir,'w')
        for each in self.dictionary:
            writeToFile.write(each + "\t" + self.dictionary[each][0] + "\n")
        writeToFile.close()
        print("Files successfully exported.")
