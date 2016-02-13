import os
def ankiExportD(fileName):
    exportFolder = ".\ankiExport"
    #Makes export folder if it doesn't exist
    if not os.path.exists(exportFolder):
        os.makedirs(exportFolder)


def backupD(fileName):
    backupFolder = ".\dictBackup"
    #Makes backup folder if it doesn't exist
    if not os.path.exists(backupFolder):
        os.makedirs(backupFolder)

backupD("test2.txt")
ankiExportD("test.txt")

