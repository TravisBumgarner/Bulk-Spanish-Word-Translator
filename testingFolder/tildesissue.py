import io
def fromFile(fileName):
    #Reads wordlist form txt
    #requires os, io module

    with io.open(fileName,'r',encoding='utf8') as f:
        text = f.read().replace('\ufeff', '').split("\n")
        print(text)
    #text = text
    return text
