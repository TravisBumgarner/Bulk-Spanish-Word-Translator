dictionary = {}
spanishWord = ["gato", "perro"]
englishWord = ["cat", "dog"]
wordSeen = ["gata", "perra"]





def appendListD(dictionary, spanishWordList, englishWordList, seenWordList):
    #adds new entries found to dictionary
    #don't set equation equal to anything. Takes in dictionary and returns 
    def appendD(dictionary,spanishWord,englishWord,seenWord):
        timesSeen = 1
        dictionary[spanishWord] = [englishWord, [seenWord], timesSeen]
        return dictionary
        
    for index in range(len(spanishWordList)):
        appendD(dictionary, spanishWordList[index], englishWordList[index], seenWordList[index])
        


appendListD(dictionary,spanishWord,englishWord,wordSeen)

for i in dictionary:
    stringOfSeen = ""
    for j in dictionary[i][1]:
        stringOfSeen += " " + j
        
    print("The word " + i + " in English is " + dictionary[i][0] + ". It has been seen " + str(dictionary[i][2]) + " times, as" + stringOfSeen)
