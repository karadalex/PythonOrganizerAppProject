import wx
import textFileOperations

# Names of columns for financial Data:
columnsNames = "Category, Payment Type, Account, Currency, Amount, Expense, Date, Time, Warranty (months)".split(", ")

# Finance record options stored in lists:
category = "Car, Groceries, Eating out, Salary/Income, Sport, Transport, Entertainment/culture, Wardrobe, Personal, Kids, Pets, Household/utilities, Phone/Internet, Electronics, Mortgage/Rent, Loans/Insurance, Vacation, Others".split(", ")
paymentType = "Cash, Debit card, Credit card, Bank transfer, Voucher, Mobile payment, Web payment".split(", ")
account = "My account, Family account, Debit card".split(", ")
currency = "EUR (Euro), USD (United States Dollar), GBP (British Pound Sterling)".split(", ")



class FinanceFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'MyFinance', size=(1200, 600))

        # Set background colour
        self.SetBackgroundColour('#1485CC')

        #load application's icon
        self.icon = wx.Icon('mediaFilesPackage/myFinance.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        # Create Finance Data and:
        self.initializeFinancialDataFile()

        #Create Menus
        menuFile = wx.Menu()
        exit = wx.MenuItem(menuFile, 5, '&Quit', 'Quit the Application')
        exit.SetBitmap(wx.Image('mediaFilesPackage/exitIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuFile.AppendItem(exit)

        menuAbout = wx.Menu()
        about = wx.MenuItem(menuAbout, 6, '&About MyFinance', 'See information about MyFinance')
        about.SetBitmap(wx.Image('mediaFilesPackage/about.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        menuAbout.AppendItem(about)

        #Create the Menu Bar which contains all of the above Menus
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&File")
        menuBar.Append(menuAbout, "&About")
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()

        #Assign to each menu option an event which will be assigned to a function
        self.Bind(wx.EVT_MENU, self.OnClose, id=5)
        self.Bind(wx.EVT_MENU, self.OnAboutMyFinance, id=6)

        # first create an horizontal box
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # Add to the horizontal box some inner vertical boxes with different proportions(?)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        hbox.Add(vbox1, 3, wx.EXPAND)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        hbox.Add(vbox2, 1, wx.EXPAND)

        # Create and add panels to the first (left) box
        panel1 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        vbox1.Add(panel1, len(columnsNames), wx.EXPAND, 5)
        panel2 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        vbox1.Add(panel2, 1, wx.EXPAND, 5)

        # Add wx.ListCtrl object to the second (right) box and make it available to the whole
        # class with self. notation
        self.lc = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        vbox2.Add(self.lc, 1, wx.EXPAND | wx.ALL, 5)
        # Add columns to ListCtrl object
        for i in range(len(columnsNames)):
            self.lc.InsertColumn(i, columnsNames[i])
            self.lc.SetColumnWidth(i, len(columnsNames[i]*10))

        # Load data to ListCtrl object from csv file if existing:
        self.loadDataFromCsvFile()

        # Add to upper-left corner panel (panel1) input controls (all controls are stored in list)
        self.inControls = range(len(columnsNames))
        self.inControls[0] = wx.ComboBox(panel1, -1, size=wx.DefaultSize, choices=category, style=wx.CB_READONLY)
        self.inControls[1] = wx.ComboBox(panel1, -1, size=wx.DefaultSize, choices=paymentType, style=wx.CB_READONLY)
        self.inControls[2] = wx.ComboBox(panel1, -1, size=wx.DefaultSize, choices=account, style=wx.CB_READONLY)
        self.inControls[3] = wx.ComboBox(panel1, -1, size=wx.DefaultSize, choices=currency, style=wx.CB_READONLY)
        for i in range(4, len(columnsNames)):
            self.inControls[i] = wx.TextCtrl(panel1, -1)

        # Create one grid and one box for left box
        vbox3 = wx.GridSizer(len(columnsNames), 2, 0, 0)
        vbox4 = wx.BoxSizer(wx.VERTICAL)

        # Create static texts for input controls:
        staticTextWidgets = []
        for i in range(len(columnsNames)):
            staticTextWidgets.append(wx.StaticText(panel1, -1, columnsNames[i]))

        # Add the input controls in vbox3:
        widgetsReadyToAddList = []
        for i in range(len(columnsNames)):
            vbox3.Add(staticTextWidgets[i], 1, wx.EXPAND | wx.ALL, 3)
            vbox3.Add(self.inControls[i], 1, wx.EXPAND | wx.ALL, 3)
        vbox3.AddMany(widgetsReadyToAddList)
        panel1.SetSizer(vbox3)

        # Add buttons to organize content of ListCtrl
        vbox4.Add(wx.Button(panel2, 1, 'Add'), 0, wx.ALIGN_CENTER | wx.TOP, 15)
        vbox4.Add(wx.Button(panel2, 2, 'Remove'), 0, wx.ALIGN_CENTER | wx.TOP, 15)
        vbox4.Add(wx.Button(panel2, 3, 'Clear'), 0, wx.ALIGN_CENTER | wx.TOP, 15)
        vbox4.Add(wx.Button(panel2, 4, 'Close'), 0, wx.ALIGN_CENTER | wx.TOP, 15)
        panel2.SetSizer(vbox4)

        # Assign functions to buttons' events:
        self.Bind(wx.EVT_BUTTON, self.OnAdd, id=1)
        self.Bind(wx.EVT_BUTTON, self.OnRemove, id=2)
        self.Bind(wx.EVT_BUTTON, self.OnClear, id=3)
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=4)

        self.SetSizer(hbox)


    def initializeFinancialDataFile(self):
        # Store all financial data in a .csv file:
        self.financialDataStore = open("mediaFilesPackage/FinancialData.csv", "a")
        #financialDataRead = open("mediaFilesPackage/FinancialData.csv", "r")
        firstLineString = "Category;Payment Type;Account;Currency;Amount;Expense;Date;Time;Warranty (months)"
        firstCsvLine = textFileOperations.textFileToString("mediaFilesPackage/FinancialData.csv").split('\n', 1)[0]
        if firstCsvLine != firstLineString:
            # Specify content of csv file with first line:
            self.financialDataStore.write(firstLineString+"\n")

    def loadDataFromCsvFile(self):
        # First Load data from csv file (if existing):
            dataFile = textFileOperations.textFileToListWithStrings("mediaFilesPackage/FinancialData.csv")
            if (len(dataFile) > 1 and len(dataFile[1]) > 1):
                numOfItems = len(dataFile)-1
                for i in range(1, numOfItems+1):
                    dataLine = dataFile[i].split(";")
                    self.lc.InsertStringItem(i-1, dataLine[0])
                    for j in range(2, len(dataLine)):
                        self.lc.SetStringItem(i-1, j, dataLine[j])

    # Define Buttons'functions:
    def OnAdd(self, event):
        # Adds data from the input fields to the List and collects the data to store them in the csv file:

        # If there isnt at least one field with a value then pass
        if not any([ self.inControls[i].GetValue() for i in range(len(columnsNames)) ]):
            pass

        # count number of preexisting list items
        numOfItems = self.lc.GetItemCount()
        # insert data to ListCtrl
        self.lc.InsertStringItem(numOfItems, self.inControls[0].GetValue())
        # store data line as string:
        dataLineString = ""
        dataLineString += self.inControls[0].GetValue() + ";"
        for i in range(1, 4):
            self.lc.SetStringItem(numOfItems, i, self.inControls[i].GetValue())
            dataLineString += self.inControls[i].GetValue() + ";"
        for i in range(5, len(columnsNames)):
            self.lc.SetStringItem(numOfItems, i, self.inControls[i].GetValue())
            dataLineString += self.inControls[i].GetValue() + ";"
            self.inControls[i].Clear()

        # erase last comma from line and add to csv file:
        dataLineString = dataLineString[:-1]
        print dataLineString
        self.financialDataStore.write(dataLineString+"\n")


    def OnRemove(self, event):
        index = self.lc.GetFocusedItem()
        self.lc.DeleteItem(index)

    def OnClose(self, event):
        self.Close()

    def OnClear(self, event):
        self.lc.DeleteAllItems()

    def OnAboutMyFinance(self, event):
        wx.MessageBox("An app where you can keep track of your financial data!!!\n Keep track of your expenses or accounts with this simple tool!", "MyFinance", wx.OK | wx.ICON_INFORMATION, self)



def myFinanceTool():
    app = wx.App()
    frame = FinanceFrame()
    frame.Show()
    app.MainLoop()

#Uncomment to test running of this python file
#myFinanceTool()
