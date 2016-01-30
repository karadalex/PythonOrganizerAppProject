import wx
import textFileOperations

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example', size=(720, 480))

        #load application's icon
        self.icon = wx.Icon('mediaFilesPackage/mynotes.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        menuFile = wx.Menu()
        save = wx.MenuItem(menuFile, 1, '&Save', 'Save your work!')
        save.SetBitmap(wx.Image('mediaFilesPackage/save.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuFile.AppendItem(save)

        exit = wx.MenuItem(menuFile, 2, '&Quit', 'Quit the Application')
        exit.SetBitmap(wx.Image('mediaFilesPackage/exitIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuFile.AppendItem(exit)

        menuAbout = wx.Menu()
        about = wx.MenuItem(menuAbout, 3, '&About MyNotes', 'See information about MyNotes')
        about.SetBitmap(wx.Image('mediaFilesPackage/about.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuAbout.AppendItem(about)

        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&File")
        menuBar.Append(menuAbout, "&About")
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.Bind(wx.EVT_MENU, self.OnSaveNotes, id=1)
        self.Bind(wx.EVT_MENU, self.OnNotesQuit, id=2)
        self.Bind(wx.EVT_MENU, self.OnAboutMyNotes, id=3)

        panel = wx.Panel(self, -1)
        multiLabel = wx.StaticText(panel, -1)
        notes = text = open("mediaFilesPackage/notesFile.txt", "r+")
        notes = textFileOperations.textFileToString("mediaFilesPackage/notesFile.txt")
        self.multiText = wx.TextCtrl(panel, -1,notes,size=(700, 480), style=wx.TE_MULTILINE)
        self.multiText.SetInsertionPoint(0)

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([multiLabel, self.multiText])
        panel.SetSizer(sizer)

    def OnNotesQuit(self, event):
        self.Close()

    def OnSaveNotes(self, event):
        newFile = open("mediaFilesPackage/notesFile.txt", "r+")
        newFile.write(self.multiText.GetValue())

    def OnAboutMyNotes(self, event):
        wx.MessageBox("An app where you can quickly store and edit various notes!!!", "MyNotes", wx.OK | wx.ICON_INFORMATION, self)

def notesTextEdit():
    app = wx.App()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()