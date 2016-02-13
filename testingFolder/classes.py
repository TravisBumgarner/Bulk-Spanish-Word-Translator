import pickle #used for file handling
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
            


#Run Tests               
new = dt()
test = ["cat","dog"]
new.appendD(test,test,test)        
                                          
        
                                      
