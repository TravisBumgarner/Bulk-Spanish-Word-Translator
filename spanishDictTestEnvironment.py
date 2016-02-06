import os

def importFromTXT():
    #Reads wordlist form txt
    #requires os module
    wordListLocation = ''
    while(not os.path.isfile(wordListLocation)):
        try:
            wordListLocation = input('Specify txt file to import:\n')
            wordListLocationOpen = open(wordListLocation)
            wordListLocationRead = wordListLocationOpen.read()
            #wordList = wordListLocation.read()
        except FileNotFoundError:
            print("Enter a valid file location")
        except PermissionError:
            print("Make sure to specify the file name and file path.")
        return wordListLocationRead.split('\n')
