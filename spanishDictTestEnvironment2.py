dictionary = {}
spanishWord = "gato"
englishWord = "cat"
wordSeen = "gata"

def appendD(dictionary,spanishWord,englishWord,wordSeen):
    timesSeen = 1
    dictionary[spanishWord] = [englishWord, [wordSeen], timesSeen]
    #I have no idea what this will do
    print("Yay!")
    return dictionary

appendD(dictionary,spanishWord,englishWord,wordSeen)
