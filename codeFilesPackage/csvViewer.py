import wx
import os

def makeContactsTextFromCsv():
    app = wx.PySimpleApp()
    wildcard = "Outlook CSV file (*.csv)|*.csv|" \
               "Gmail CSV file (*.csv)|*.csv|" \
            "All files (*.*)|*.*"
    dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        filePath = dialog.GetPath()
        print "Openning: ", filePath, "..."
        print "_________________________________________________________________________________"
    dialog.Destroy()

    flag=True
    try:
        csvFile = open(filePath, "r")
        newFile = open("contactsFile.txt", "a+")
        os.getcwd()
        csvFileArray = []
        for i in csvFile:
            csvFileArray.append(i.split(","))
        csvFile.close()

        tagsList = csvFileArray[0]
        for i in range(1, len(csvFileArray)):
            for j in range(len(csvFileArray[0])):
                if csvFileArray[i][j] !='' and csvFileArray[i][j] != '\n':
                    newFile.write(csvFileArray[0][j] + ": " + csvFileArray[i][j])
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


#test if file is created
#newFile = makeContactsTextFromCsv()
