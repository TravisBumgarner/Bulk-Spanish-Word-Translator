import requests, bs4

'''
Spanishdict.com search for "palabra" returns:
http://www.spanishdict.com/translate/palabras

Results in:
<h1 class="source-text">palabra</h1>

<div class="el">
    <a href="http://www.spanishdict.com/translate/word">word</a>
</div>


res = requests.get('http://www.spanishdict.com/translate/palabras')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
result =  noStarchSoup.select('.source-text')


result returns [<h1 class="source-text">palabra</h1>]
result[0].getText() returns 'palabra'
'''

def intro():
    print('--Created by Travis Bumgarner (TravisBumgarner.com--')
    print('------Translations powered by SpanishDict.com-------')

def settings():
    settingsCheck = ''
    print('Settings are:')
    #Grab Settings file and print settings.
    settingsCheck = input('Make save any changes to settings.py before continuing. Press u to update settings or c to continue.\n').lower()    
    #if(settingsCheck == 'c'):
    #    #Contunue
    #elif(settingsCheck == 'u'):
    #    #Update settings




################################################
########## Methods for inputting words #########
def inputWordList():
    print("Enter each word followed by pressing enter.")
    print("Once you're done entering words type 'AllDone'")
    wordsList = []
    word = ''
    while(word != "AllDone"):
        word = input()
        if(word!="AllDone"):
            wordsList.append(word)
    return wordsList

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

def findWords(wordListToSearch):
    if(type(wordListToSearch) == str):
        #If wordList is single string, convert to list
        wordListToSearch = [wordListToSearch]

    if(not check_connectivity('http://74.125.224.72/')):
        #URL For Google to see if internet is working
        print('Please check internet connection and try again')
    else:
        for word in wordListToSearch:
            spanishDictSearch(word)
    searchTerms = input("Input words as either a single string or a list: ")

def spanishDictSearch(word):
    res = requests.get('http://www.spanishdict.com/translate/' + word)
    noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
    result = noStarchSoup.select('.lang .el a')
    print(result)
    
def check_connectivity(reference):
    import urllib
    try:
        urllib.request.urlopen(reference, timeout=1)
        return True
    except urllib.request.URLError:
        return False




#Code Execution
'''
intro()
settings()
'''
