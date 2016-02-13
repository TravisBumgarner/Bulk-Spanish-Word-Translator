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
        
    def appendD(self,spanishWordList,englishWordList, seenWordList):
        def appendEachD(spanishWord,englishWord,seenWord):
            timesSeen = 1
            self.dictionary[spanishWord] = [englishWord, [seenWord],timesSeen]
            #return dictionary
            #pretty sure I don't need this anymore
        for index in range(len(spanishWordList)):
            appendEachD(spanishWordList[index],
                        englishWordList[index],
                           seenWordList[index])

    def backupD(self,fileName):
        backupFolder = ".\dictBackup"
        #Makes backup folder if it doesn't exist
        if not os.path.exists(backupFolder):
            os.makedirs(backupFolder)
        #Used for creating unique filenames for each time saved
        def genFileName(fileName):
            fname, fextension = os.path.splitext(fileName)
            i = 0
            newFileName = fname + str(i) + fextension
            for folderName,subfolders, filenames in os.walk(backupFolder):
                while newFileName in filenames:
                    i += 1
                    newFileName = fname + str(i) + fextension
                    if newFileName not in filenames:
                        break
                return newFileName
        pickle.dump(self.dictionary,open(backupFolder + "\\" + genFileName(fileName),"wb"))

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
   


#Run Tests               
new = dt()
test = ["cat","dog"]
new.appendD(test,test,test)
new.searchD("cat")
                                          
        
                                      
