import wx
import os
import gotoMainFolderDirectory


# Convert Calendar to text format (under construction...) :

def makeCalendarTextFromCsv():
    #app = wx.App()
    wildcard = "Google Calendar file (*.ics)|*.ics|" \
               "Apple Calendar (*.ics)|*.ics|" \
            "All files (*.*)|*.*"
    dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        filePath = dialog.GetPath()
        print "Openning: ", filePath, "..."
        print "_________________________________________________________________________________"
    dialog.Destroy()

    flag=True
    try:
        icsFile = open(filePath, "r")
        gotoMainFolderDirectory.go()
        newFile = open("mediaFilesPackage/calendarFile.txt", "a+")
        os.getcwd()
        icsFileArray = []
        for i in icsFile:
            icsFileArray.append(i.split(","))
        icsFile.close()

        tagsList = icsFileArray[0]
        for i in range(1, len(icsFileArray)):
            for j in range(len(icsFileArray[0])):
                if icsFileArray[i][j] !='' and icsFileArray[i][j] != '\n':
                    newFile.write(icsFileArray[0][j] + ": " + icsFileArray[i][j])
                    newFile.write('\n')
            newFile.write("_________________________________________________________________________________")
            newFile.write('\n')

        newFile.close()
    except UnboundLocalError:
        flag=False
        pass

    if flag == True:
        return newFile
    else:
        pass

