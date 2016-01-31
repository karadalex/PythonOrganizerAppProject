import wx
import textFileOperations

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example', size=(720, 480), style=wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.CAPTION)

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
        notes = open("mediaFilesPackage/notesFile.txt", "w")
        notes = textFileOperations.textFileToString("mediaFilesPackage/notesFile.txt")
        self.multiText = wx.TextCtrl(panel, -1,notes,size=(550, 480), style=wx.TE_MULTILINE)
        self.multiText.SetInsertionPoint(0)

        #load MyNotes picture
        image = wx.Image('mediaFilesPackage/MyNotes.jpg', wx.BITMAP_TYPE_ANY)
        self.imageBitmap = wx.StaticBitmap(panel, wx.ID_ANY, wx.BitmapFromImage(image))

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([self.multiText, self.imageBitmap])
        panel.SetSizer(sizer)

        #Set background colour
        self.SetBackgroundColour('#1485CC')

    def OnNotesQuit(self, event):
        self.Close()

    def OnSaveNotes(self, event):
        newFile = open("mediaFilesPackage/notesFile.txt", "w")
        newFile.write(self.multiText.GetValue())

    def OnAboutMyNotes(self, event):
        wx.MessageBox("An app where you can quickly store and edit various notes!!!", "MyNotes", wx.OK | wx.ICON_INFORMATION, self)

def notesTextEdit():
    app = wx.App()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()