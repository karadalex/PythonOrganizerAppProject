import datetime
import calendar
import wx
import wx.grid


def calendarText():
    """example return:

             January 2016
     Mo Tu We Th Fr Sa Su
                  1  2  3
      4  5  6  7  8  9 10
     11 12 13 14 15 16 17
     18 19 20 21 22 23 24
     25 26 27 28 29 30 31
     """

    now = datetime.datetime.now()
    x="%d" %now.year
    y="%d" %now.month

    yy=int(x)
    mm=int(y)
    return (calendar.month(yy,mm))

def calendarTextToListForGrid(text):
    """example return:
    ['    January 2016',
     ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'],
     ['  ', '   ', '   ', '   ', '  1', '  2', '  3'],
     [' 4', '  5', '  6', '  7', '  8', '  9', ' 10'],
     ['11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17'],
     ['18', ' 19', ' 20', ' 21', ' 22', ' 23', ' 24'],
     ['25', ' 26', ' 27', ' 28', ' 29', ' 30', ' 31'],
     ['']]

    """
    array = text.split("\n")
    output = []
    output.append(array[0])
    output.append(array[1].split(" "))
    for i in range(2, len(array)):
        listHelp = []
        string = array[i]
        listHelp.append(string[0:2])
        for j in range(2, len(string), 3):
            listHelp.append(string[j:j+3])
        output.append(listHelp)
    return output

# uncomment these to test code:
#test calendarTextToListForGrid(text)
#print calendarTextToListForGrid(calendarText())



calendarList = calendarTextToListForGrid(calendarText())
class SimpleCalendarGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)

        self.CreateGrid(5, 7)
        for j in range(7):
            self.SetColLabelValue(j, calendarList[1][j])
        for i in range(5):
            week = "week "+str(i+1)
            self.SetRowLabelValue(i, week)
            for j in range(7):
                cellValue = calendarList[i+2][j]
                self.SetCellValue(i, j, cellValue)

class TestFrame(wx.Frame):
    def __init__(self, parent):
        frameTitle = calendarList[0]
        testFrame = wx.Frame.__init__(self, parent, -1, frameTitle, size=(650, 160), style=wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.CAPTION)

        #load application's icon
        self.icon = wx.Icon('mediaFilesPackage/calendar.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        grid = SimpleCalendarGrid(self)


appCalendar = wx.App()
frame = TestFrame(None)
frame.Show(True)
appCalendar.MainLoop()
