import wx
import textFileOperations
import gotoMainFolderDirectory



class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'MyContacts', size=(720, 480), style=wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.CAPTION)

        #load application's icon
        self.icon = wx.Icon('mediaFilesPackage/contacts.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        #Create Menus
        menuFile = wx.Menu()
        save = wx.MenuItem(menuFile, 1, '&Save', 'Save your work!')
        save.SetBitmap(wx.Image('mediaFilesPackage/save.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuFile.AppendItem(save)

        exit = wx.MenuItem(menuFile, 2, '&Quit', 'Quit the Application')
        exit.SetBitmap(wx.Image('mediaFilesPackage/exitIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuFile.AppendItem(exit)

        menuAbout = wx.Menu()
        about = wx.MenuItem(menuAbout, 3, '&About MyContacts', 'See information about MyContacts')
        about.SetBitmap(wx.Image('mediaFilesPackage/about.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuAbout.AppendItem(about)

        #Create the Menu Bar which contains all of the above Menus
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&File")
        menuBar.Append(menuAbout, "&About")
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()

        #Assign to each menu option an event which will be assigned to a function
        self.Bind(wx.EVT_MENU, self.OnSaveContacts, id=1)
        self.Bind(wx.EVT_MENU, self.OnContactsQuit, id=2)
        self.Bind(wx.EVT_MENU, self.OnAboutMyContacts, id=3)

        panel = wx.Panel(self, -1)
        multiLabel = wx.StaticText(panel, -1)
        gotoMainFolderDirectory.go()
        contacts = textFileOperations.textFileToString("mediaFilesPackage/contactsFile.txt")
        self.multiText = wx.TextCtrl(panel, -1,contacts,size=(435, 410), style=wx.TE_MULTILINE)
        self.multiText.SetInsertionPoint(0)

        #load MyContacts picture
        image = wx.Image('mediaFilesPackage/MyContacts.jpg', wx.BITMAP_TYPE_ANY)
        self.imageBitmap = wx.StaticBitmap(panel, wx.ID_ANY, wx.BitmapFromImage(image))

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([self.multiText, self.imageBitmap])
        panel.SetSizer(sizer)

        #Set background colour
        self.SetBackgroundColour('#1485CC')


    def OnContactsQuit(self, event):
        self.Close()

    def OnSaveContacts(self, event):
        newFile = open("mediaFilesPackage/contactsFile.txt", "w")
        newFile.write(self.multiText.GetValue())

    def OnAboutMyContacts(self, event):
        wx.MessageBox("An app where you can quickly edit & view your contacts! All in one place!!!", "MyContacts", wx.OK | wx.ICON_INFORMATION, self)

    def Paint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bitmap, 500, 500)

def contactsTextEdit():
    app = wx.App()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()

#contactsTextEdit()