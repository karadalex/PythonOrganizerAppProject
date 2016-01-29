import wx
import textFileOperations

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example', size=(720, 480))
        menuFile = wx.Menu()
        menuFile.Append(1, "Save")
        menuFile.Append(2, "E&xit")
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&File")
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.Bind(wx.EVT_MENU, self.OnSaveNotes, id=1)
        self.Bind(wx.EVT_MENU, self.OnNotesQuit, id=2)
        panel = wx.Panel(self, -1)
        multiLabel = wx.StaticText(panel, -1)
        notes = text = open("mediaFilesPackage/notesFile.txt", "w")
        notes = textFileOperations.textFileToString("mediaFilesPackage/noteFile.txt")
        self.multiText = wx.TextCtrl(panel, -1,notes,size=(700, 480), style=wx.TE_MULTILINE)
        self.multiText.SetInsertionPoint(0)

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([multiLabel, self.multiText])
        panel.SetSizer(sizer)

    def OnNotesQuit(self, event):
        self.Close()

    def OnSaveNotes(self, event):
        newFile = open("mediaFilesPackage/noteFile.txt", "w")
        newFile.write(self.multiText.GetValue())

def notesTextEdit():
    app = wx.PySimpleApp()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()