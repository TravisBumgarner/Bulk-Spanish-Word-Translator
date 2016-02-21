# articulaciones - couldn't find plurarl
#impotenia - spelling errors
#asombrsa - spelling errors
wordList = ["gatas", "perritas","peones"]


def singAndMascWord(word):
    for word in wordList:
        if word[-2:] == "es":
            #If word ends with es, remove es
            word = word[0:-2]

        elif word[-2:] == "as":
            #If word ends with as, remove as and replace with o
            word = word[0:-2] + "o"

        elif word[-1:] == "s":
            #Else if word ends with s, remove s
            word = word[0:-1]
        return word

