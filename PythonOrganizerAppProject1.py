import wx
import csvViewer

class MyApp(wx.App):

    def OnInit(self):
       frame = MyFrame("Organizer", (50, 60), (450, 340))
       frame.Show()
       self.SetTopWindow(frame)
       return True

class MyFrame(wx.Frame):
    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        menuFile = wx.Menu()
        menuFile.Append(1, "&About...")
        menuFile.Append(2, "Import Contacts...")
        menuFile.AppendSeparator()
        menuFile.Append(3, "E&xit")
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&File")
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")
        self.Bind(wx.EVT_MENU, self.OnAbout, id=1)
        self.Bind(wx.EVT_MENU, self.OnImportContacts, id=2)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=3)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox("An organizer app made with Python 2.7.8 and wxPython", "wxPython", wx.OK | wx.ICON_INFORMATION, self)

    def OnImportContacts(self, event):
        csvViewer.makeContactsTextFromCsv()

def run_main():
    app = MyApp(False)
    app.MainLoop()

if __name__ == "__main__":
    run_main()
