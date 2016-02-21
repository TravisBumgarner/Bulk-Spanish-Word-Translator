import io
def fromFile():
    #Reads wordlist form txt
    #requires os, io module

    with io.open("singleWordSearch.txt",'r',encoding='utf8') as f:
        text = f.read().replace('\ufeff', '').split("\n")
        print(text)

    #text = text
    return text
