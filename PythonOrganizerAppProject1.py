# -*- coding: utf-8 -*-

import __version__
from codeFilesPackage import wx
from codeFilesPackage import csvConverter
from codeFilesPackage import contactsTextEditor
from codeFilesPackage import icsConverter
from codeFilesPackage import nameDayViewer
from codeFilesPackage import date
#from codeFilesPackage import calendarSimpleText
import os


class MyApp(wx.App):

    def OnInit(self):
       frame = MyFrame("Organizer", (50, 60), (720, 480))
       frame.Show(True)
       self.SetTopWindow(frame)
       return True

class MyFrame(wx.Frame):
    def __init__(self, title, pos, size):
        myFrame = wx.Frame.__init__(self, None, -1, title, pos, size, style=wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.CAPTION)

        menuFile = wx.Menu()
        menuFile.Append(1, "Import Contacts...")
        menuFile.Append(6, "Import Calendar...")
        menuFile.AppendSeparator()
        menuFile.Append(2, "E&xit")
        menuHelp = wx.Menu()
        menuHelp.Append(3, "&About...")
        menuHelp.Append(4, "&Version")
        menuEdit = wx.Menu()
        menuEdit.Append(5, "&Edit/View your Contacts...")
        menuView = wx.Menu()
        menuView.Append(7, "&View whose Nameday is today...")
        menuView.Append(8, "&Calendar")
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&File")
        menuBar.Append(menuEdit, "&Edit")
        menuBar.Append(menuView, "&View")
        menuBar.Append(menuHelp, "&Help")
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to your personal Organizer!")
        self.Bind(wx.EVT_MENU, self.OnImportContacts, id=1)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=2)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=3)
        self.Bind(wx.EVT_MENU, self.OnVersion, id=4)
        self.Bind(wx.EVT_MENU, self.OnEditViewContacts, id=5)
        self.Bind(wx.EVT_MENU, self.OnImportCalendar, id=6)
        self.Bind(wx.EVT_MENU, self.OnViewNamedayToday, id=7)
        self.Bind(wx.EVT_MENU, self.OnViewCalendar, id=8)


        #load welcome picture
        self.bitmap = wx.Bitmap("mediaFilesPackage/welcomeScreen1.jpg")
        wx.EVT_PAINT(self, self.Paint)
        self.Centre()

        self.SetBackgroundColour('#1485CC')


    def Paint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bitmap, 30, 20)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox("An organizer app made with Python 2.7.8 and wxPython", "wxPython", wx.OK | wx.ICON_INFORMATION, self)

    def OnImportContacts(self, event):
        csvConverter.makeContactsTextFromCsv()

    def OnVersion(self, event):
        wx.MessageBox("The current version of this program is: "+__version__.VERSION_STRING, "Version of Organizer", wx.OK | wx.ICON_INFORMATION, self)

    def OnEditViewContacts(self, event):
        contactsTextEditor.contactsTextEdit()

    def OnImportCalendar(self, event):
        icsConverter.makeCalendarTextFromCsv()

    def OnViewNamedayToday(self, event):
        date1 = str(date.shortDateString())
        date2 = str(date.fullDateString())
        try:
            string = nameDayViewer.nameDayDictionaryCreation()[date1]
        except KeyError:
            string = ""
        if string != "":
            wx.MessageBox("Shmera giortazoyn ta onomata: \n"+string, "Name Celebrations for "+date2, wx.OK, self)
        else:
            wx.MessageBox("Gia shmera den yparxei kapoio onoma poy na exei giorth"+string, "Name Celebrations for "+date2, wx.OK, self)

    def OnViewCalendar(self, event):
        #calendarSimpleText.runCalendar()
        filename=os.getcwd()+"\codeFilesPackage\calendarSimpleText.pyw"
        print filename
        os.startfile(filename, 'open')



def run_main():
    mainApplication = MyApp(False)
    mainApplication.MainLoop()

if __name__ == "__main__":
    run_main()
