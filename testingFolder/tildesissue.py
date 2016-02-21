import io
def fromFile(fileName):
    #Reads wordlist form txt
    #requires os, io module

    with io.open(fileName,'r',encoding='utf8') as f:
        text = f.read()
        print(text)
    return text.split('\n')
