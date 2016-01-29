import wx
import textFileOperations
import gotoMainFolderDirectory
import greeklish



class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'MyContacts', size=(720, 480))

        menuFile = wx.Menu()
        menuFile.Append(1, "Save")
        menuFile.Append(2, "E&xit")
        menuAbout = wx.Menu()
        menuAbout.Append(3, "About MyContacts")
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&File")
        menuBar.Append(menuAbout, "&About")
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.Bind(wx.EVT_MENU, self.OnSaveContacts, id=1)
        self.Bind(wx.EVT_MENU, self.OnContactsQuit, id=2)
        self.Bind(wx.EVT_MENU, self.OnAboutMyContacts, id=3)

        panel = wx.Panel(self, -1)
        multiLabel = wx.StaticText(panel, -1)
        gotoMainFolderDirectory.go()
        contacts = textFileOperations.textFileToString("mediaFilesPackage/contactsFile.txt")
        self.multiText = wx.TextCtrl(panel, -1,contacts,size=(700, 480), style=wx.TE_MULTILINE)
        self.multiText.SetInsertionPoint(0)

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([multiLabel, self.multiText])
        panel.SetSizer(sizer)

    def OnContactsQuit(self, event):
        self.Close()

    def OnSaveContacts(self, event):
        newFile = open("mediaFilesPackage/contactsFile.txt", "r+")
        newFile.write(self.multiText.GetValue())

    def OnAboutMyContacts(self, event):
        wx.MessageBox("An app where you can quickly edit & view your contacts! All in one place!!!", "MyContacts", wx.OK | wx.ICON_INFORMATION, self)

def contactsTextEdit():
    #app = wx.PySimpleApp()
    frame = TextFrame()
    frame.Show()
    #app.MainLoop()

#contactsTextEdit()