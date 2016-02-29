# Spanish-Word-Lookup
Tool for looking up and translating words between English and Spanish automatically. Exports results to file for importing to Anki and other flash card programs.

spanishDict.py is the main script to be executed. 
dictTools.py is a collection of tools for opening, exporting, printing, etc. the dictionary.
myWordsToday.txt is the file where you can load words to be looked up. Each word must be seperated by a newline.
/ankiExport is where an exported version of the dictionary is stored.
/dictBackup is a backup of the dictionary each time the program is run.

dictTools methods:
> Use dt() to create a new class
> newD(fileName) - Creates a new dictionary
> openD(fileName) - Opens an already existing dictionary
> saveD(fileName) - Saves dictionary
> modifyEntryD(spanishWord,seenWord) - Used for modifying an existing dictionary entry with new information
> newEntryD(seenWord,spanishWord,englishWord) - Used for adding new dictionary entry
> backupD(fileName) - Makes a backup of the dictionary in the /dictBackup folder
> searchD(word) - Searches dictionary for a specific word - user friendly
> existsD(word) - Searches dictionary for a specific word - computer friendly
> printD() - prints a table version of the dictionary information
> ankiExportD() - Exports dictionary to Anki format

spanishDict tools:
> add.fromText() - lets you enter words in the command line
> add.fromFile(fileName) - lets you specify a filename to read words from
> spanishDictSearch() - searches each word on spanishdict.com
> spanishToEnglish(wordListToSearch) - Returns list of results from input word list
> searchAndSave(fileName) - Automates process. Can customize this to include add.fromText() 
  or add.fromFile(). Specify whether to printD(), saveD(), ankiExportD(), or backupD(). 
