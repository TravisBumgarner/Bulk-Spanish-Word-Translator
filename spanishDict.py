import requests, bs4, os, urllib, io
from dictTools import dt #My created tools for working with dictionaries

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
    print('Created by Travis Bumgarner www.TravisBumgarner.com')
    print('------Translations powered by SpanishDict.com------')
    print('----To modify search settings open settings.py-----')

################################################
########## Methods for inputting words #########
class add:
    def fromText():
        print("Enter each word followed by pressing enter.")
        print("Once you're done entering words type 'AllDone'")
        wordsList = []
        word = ''
        while(word != "AllDone"):
            word = input()
            if(word!="AllDone"):
                wordsList.append(word)
        if len(wordsList) != 0:
            return wordsList
        else:
            print("No words provided. Returning None.")
            return None
        
    def fromFile(fileName):
        #Reads wordlist form txt
        #requires os, io module
        try:
            with io.open(fileName,'r',encoding='utf8') as f:
                return f.read().replace('\ufeff', '').split("\n")
        except FileNotFoundError:
            print("Enter a valid file location")
        except PermissionError:
            print("Make sure to specify the file name and file path.")

###################################
### Translate Class will go Here###
###################################

def englishWordConcat(englishBits):
    englishWordParts = []
    for index in range(len(englishBits)):
        englishWordParts.append(englishBits[index].getText())
    englishBitsCombined = " ".join(englishWordParts)
    return englishBitsCombined

def spanishDictSearch(word):
    #requires bs4, requests
    print("Searching for " + word + "...")
    res = requests.get('http://www.spanishdict.com/translate/' + word)
    resultEnglish = []
    resultSpanish = []
    noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
    if noStarchSoup.select('.lang .el') != []:
        #This deals with layout when SpanishDict puts exact translation
        #Directly underneath the spanish word, such as in gato.
        resultEnglish = englishWordConcat(noStarchSoup.select('.lang .el'))
    
        resultSpanish = noStarchSoup.select('h1[class="source-text"]')
        resultSpanish = resultSpanish[0].getText()
    elif noStarchSoup.select('.lang .el') == []:
        #Deals with word being more nested in the document.
        resultSpanish = noStarchSoup.select('h1[class="source-text"]')
        resultSpanish = resultSpanish[0].getText()
        resultEnglish = englishWordConcat(noStarchSoup.select('.dictionary-neoharrap-translation-translation'))
    return([word,resultSpanish,resultEnglish])
def spanishToEnglish(wordListToSearch):
    def validWordCheck(word):
        while True:
            try:
                spanishDictSearch(word)
            except IndexError:
                word = input(word + " not found. Enter word again or type 'skipWord' to continue.\n")
                if(word == "skipWord"):
                    return False
                else:
                    continue
    if(type(wordListToSearch) == str):
        #If wordList is single string, convert to list
        wordListToSearch = [wordListToSearch]
            
    if(not check_connectivity('http://74.125.224.72/')):
        #URL For Google to see if internet is working
        print('Please check internet connection and try again')
    else:
        searchResults = []
        for word in wordListToSearch:
            if validWordCheck(word) != False:
                searchResults.append(validWordCheck(word))

    

    return searchResults
    
def check_connectivity(reference):
    #requires urllib
    try:
        urllib.request.urlopen(reference, timeout=1)
        return True
    except urllib.request.URLError:
        return False

def searchAndSave(fileName = "newDict.p"):
    intro()
    #seenSpanish = add.fromText()
    seenSpanish = add.fromFile("myWordsToday.txt")
    results = spanishToEnglish(seenSpanish)
    #print(results)
    tempD = dt()
    # If file exists, open, else, create.
    if(tempD.openD(fileName) == True):
        tempD.openD(fileName)
    elif(tempD.openD(fileName) == False):
        tempD.newD(fileName)
    else:
        return "Not successfully opened."
    for eachResult in results:
        #Simplify results from abstract list values to what they actually are
        seenWord = eachResult[0]
        spanishWord = eachResult[1]
        englishWord = eachResult[2]
        print(spanishWord)
        if tempD.existsD(spanishWord) == False:
            #If Word isn't found, run new word function
            tempD.newEntryD(seenWord,spanishWord,englishWord)
        elif tempD.existsD(spanishWord) == True:
            tempD.modifyEntryD(spanishWord, seenWord)       
    tempD.printD()
    #tempD.ankiExportD(fileName)
    #tempD.backupD(fileName)
    tempD.saveD(fileName)

