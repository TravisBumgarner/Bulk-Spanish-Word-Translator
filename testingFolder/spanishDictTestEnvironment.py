def spanishDictSearch(wordSearched):
    import bs4, requests
    res = requests.get('http://www.spanishdict.com/translate/' + wordSearched)
    noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
    result = noStarchSoup.select('.lang .el')
    wordFound = ""
    if(result[0].getText() == "" || #Check SA to figure out of reslt[0] is empty#):
        wordFound = "notFound"
    else:
        #Following code deals with how SpaishDict presents words such as El Gato nested inside two different link tags.
        for i in range(len(result)):
            wordFound += result[i].getText()
            if(i < len(result)-1):
                #Adds a space between each word unless the last word is reached
                wordFound += " "
    return wordFound
