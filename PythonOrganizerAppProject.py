﻿# -*- coding: utf-8 -*-

import __version__
import wx
from codeFilesPackage import csvConverter
from codeFilesPackage import contactsTextEditor
from codeFilesPackage import icsConverter
from codeFilesPackage import nameDayViewer
from codeFilesPackage import date
import os
from codeFilesPackage import myNotesEditor
from wx.lib.buttons import GenBitmapTextButton
from codeFilesPackage import myFinanceTool


class MyApp(wx.App):

    # Initiate main frame window:
    def OnInit(self):
       frame = MyFrame("Organizer", (50, 60), (720, 480))
       frame.Show(True)
       self.SetTopWindow(frame)
       return True

# Define the class where all widgets are added, this class inherits from wx.Frame class:
class MyFrame(wx.Frame):
    def __init__(self, title, pos, size):
        myFrame = wx.Frame.__init__(self, None, -1, title, pos, size, style=wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.CAPTION)

        #Create the taskbar
        #create menu "File"
        menuFile = wx.Menu()
        menuFile.Append(1, "Import Contacts...")
        menuFile.Append(6, "Import Calendar...")

        menuFile.AppendSeparator()

        exit = wx.MenuItem(menuFile, 2, '&Quit', 'Quit the Application')
        exit.SetBitmap(wx.Image('mediaFilesPackage/exitIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuFile.AppendItem(exit)

        # create menu Help:
        menuHelp = wx.Menu()
        about = wx.MenuItem(menuHelp, 3, '&About...', 'See information about this application')
        about.SetBitmap(wx.Image('mediaFilesPackage/about.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuHelp.AppendItem(about)

        menuHelp.Append(4, "&Version")

        # Create menu Edit:
        menuEdit = wx.Menu()
        editContacts = wx.MenuItem(menuEdit, 5, '&Edit/View MyContacts', 'Edit or view your Contacts')
        editContacts.SetBitmap(wx.Image('mediaFilesPackage/edit.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuEdit.AppendItem(editContacts)

        # Create menu View:
        menuView = wx.Menu()
        viewNameday = wx.MenuItem(menuView, 7, '&View whose Nameday is today...', 'View whose Nameday is today...')
        viewNameday.SetBitmap(wx.Image('mediaFilesPackage/birthday.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuView.AppendItem(viewNameday)

        viewCalendar = wx.MenuItem(menuView, 8, '&Calendar', 'View your Calendar')
        viewCalendar.SetBitmap(wx.Image('mediaFilesPackage/calendar.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuView.AppendItem(viewCalendar)

        # Create menu  Notes:
        menuNotes = wx.Menu()
        editNotes = wx.MenuItem(menuView, 9, '&Edit Notes...', 'Edit your Notes!')
        editNotes.SetBitmap(wx.Image('mediaFilesPackage/edit.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuNotes.AppendItem(editNotes)

        menuTools = wx.Menu()
        myFinance_tool = wx.MenuItem(menuTools, 10, '&MyFinance', 'Track your expenses!')
        myFinance_tool.SetBitmap(wx.Image('mediaFilesPackage/myFinance.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuTools.AppendItem(myFinance_tool)

        # Add all submenus to the main menu:
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&File")
        menuBar.Append(menuEdit, "&Edit")
        menuBar.Append(menuView, "&View")
        menuBar.Append(menuNotes, "&My Notes")
        menuBar.Append(menuTools, "&Tools")
        menuBar.Append(menuHelp, "&Help")

        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to your personal Organizer!")

        # Assign functions to menu events:
        self.Bind(wx.EVT_MENU, self.OnImportContacts, id=1)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=2)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=3)
        self.Bind(wx.EVT_MENU, self.OnVersion, id=4)
        self.Bind(wx.EVT_MENU, self.OnEditViewContacts, id=5)
        self.Bind(wx.EVT_MENU, self.OnImportCalendar, id=6)
        self.Bind(wx.EVT_MENU, self.OnViewNamedayToday, id=7)
        self.Bind(wx.EVT_MENU, self.OnViewCalendar, id=8)
        self.Bind(wx.EVT_MENU, self.OnEditNotes, id=9)
        self.Bind(wx.EVT_MENU, self.OnMyFinanceTool, id=10)

        #load application's icon
        self.icon = wx.Icon('mediaFilesPackage/appIcon32.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        #Set background colour
        self.SetBackgroundColour('#1485CC')

        #load welcome picture
        self.bitmap = wx.Bitmap("mediaFilesPackage/welcomeScreen1.jpg")
        wx.EVT_PAINT(self, self.Paint)
        self.Centre()

        #Create buttons for main screen
        panel = wx.Panel(self, -1)

        editViewContactsButton = GenBitmapTextButton(self, 1, wx.Bitmap('mediaFilesPackage/edit.png'), 'Edit/View MyContacts', (480, 40), (200, 25))
        editViewContactsButton.SetBezelWidth(1)
        editViewContactsButton.SetBackgroundColour('#c2e6f8')
        editViewContactsButton.Bind(wx.EVT_LEFT_DOWN, self.OnEditViewContacts)

        viewNamedayButton = GenBitmapTextButton(self, 2, wx.Bitmap('mediaFilesPackage/birthday.png'), 'View whose nameday is today', (480, 75), (200, 25))
        viewNamedayButton.SetBezelWidth(1)
        viewNamedayButton.SetBackgroundColour('#c2e6f8')
        viewNamedayButton.Bind(wx.EVT_LEFT_DOWN, self.OnViewNamedayToday)

        viewCalendarButton = GenBitmapTextButton(self, 3, wx.Bitmap('mediaFilesPackage/calendar.png'), 'View calendar', (480, 110), (200, 25))
        viewCalendarButton.SetBezelWidth(1)
        viewCalendarButton.SetBackgroundColour('#c2e6f8')
        viewCalendarButton.Bind(wx.EVT_LEFT_DOWN, self.OnViewCalendar)

        editMyNotesButton = GenBitmapTextButton(self, 4, wx.Bitmap('mediaFilesPackage/edit.png'), 'Edit MyNotes', (480, 145), (200, 25))
        editMyNotesButton.SetBezelWidth(1)
        editMyNotesButton.SetBackgroundColour('#c2e6f8')
        editMyNotesButton.Bind(wx.EVT_LEFT_DOWN, self.OnEditNotes)

        myFinanceToolButton = GenBitmapTextButton(self, 5, wx.Bitmap('mediaFilesPackage/myFinance.png'), 'Organize your financial data!', (480, 180), (200, 25))
        myFinanceToolButton.SetBezelWidth(1)
        myFinanceToolButton.SetBackgroundColour('#c2e6f8')
        myFinanceToolButton.Bind(wx.EVT_LEFT_DOWN, self.OnMyFinanceTool)



    # Define the functions which are assigned to the events:

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
        filename=os.getcwd()+"/codeFilesPackage/calendarSimpleText.py"
        print filename
        try:
            # Start in Windows OS
            os.startfile(filename, 'open')
        except AttributeError:
            # Start in Mac OS X, Linux
            os.system('python '+filename)

    def OnEditNotes(self, event):
        myNotesEditor.notesTextEdit()

    def OnMyFinanceTool(selfself, event):
        myFinanceTool.myFinanceTool()




# Start running this python file:

def run_main():
    mainApplication = MyApp(False)
    mainApplication.MainLoop()

if __name__ == "__main__":
    run_main()
