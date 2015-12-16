import wx
import csvViewer
import __version__

class MyApp(wx.App):

    def OnInit(self):
       frame = MyFrame("Organizer", (50, 60), (720, 480))
       frame.Show()
       self.SetTopWindow(frame)
       return True

class MyFrame(wx.Frame):
    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        menuFile = wx.Menu()
        menuFile.Append(1, "Import Contacts...")
        menuFile.AppendSeparator()
        menuFile.Append(2, "E&xit")
        menuHelp = wx.Menu()
        menuHelp.Append(3, "&About...")
        menuHelp.Append(4, "&Version")
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&File")
        menuBar.Append(menuHelp, "&Help")
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Welcome your personal Organizer!")
        self.Bind(wx.EVT_MENU, self.OnImportContacts, id=1)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=2)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=3)
        self.Bind(wx.EVT_MENU, self.OnVersion, id=4)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox("An organizer app made with Python 2.7.8 and wxPython", "wxPython", wx.OK | wx.ICON_INFORMATION, self)

    def OnImportContacts(self, event):
        csvViewer.makeContactsTextFromCsv()

    def OnVersion(self, event):
        wx.MessageBox("The current version of this program is: "+__version__.VERSION_STRING, "Version of Organizer", wx.OK | wx.ICON_INFORMATION, self)

def run_main():
    app = MyApp(False)
    app.MainLoop()

if __name__ == "__main__":
    run_main()
