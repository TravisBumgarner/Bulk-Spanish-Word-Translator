import bs4, requests

def englishWordConcat(englishBits):
    englishWordParts = []
    for index in range(len(englishBits)):
        englishWordParts.append(englishBits[index].getText())
    englishBitsCombined = " ".join(englishWordParts)
    return englishBitsCombined


def searchD(word):
    #requires bs4, requests
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
        resultEnglish = englishWordConcat(noStarchSoup.select('.dictionary-neoharrap-translation-translation'))
        print(resultEnglish)

def check_connectivity(reference):
    #requires urllib
    try:
        urllib.request.urlopen(reference, timeout=1)
        return True
    except urllib.request.URLError:
        return False
searchD("fastuoso")

