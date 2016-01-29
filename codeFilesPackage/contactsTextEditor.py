import wx
import textFileOperations
import gotoMainFolderDirectory
import greeklish



class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example', size=(720, 480))
        panel = wx.Panel(self, -1)
        multiLabel = wx.StaticText(panel, -1)
        gotoMainFolderDirectory.go()
        contacts = textFileOperations.textFileToString("mediaFilesPackage/contactsFile.txt")
        multiText = wx.TextCtrl(panel, -1,contacts,size=(700, 480), style=wx.TE_MULTILINE)
        multiText.SetInsertionPoint(0)

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([multiLabel, multiText])
        panel.SetSizer(sizer)

def contactsTextEdit():
    app = wx.PySimpleApp()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()

#contactsTextEdit()