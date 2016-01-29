import datetime
import calendar

def calendarText():
    now = datetime.datetime.now()
    x="%d" %now.year
    y="%d" %now.month

    yy=int(x)
    mm=int(y)
    return (calendar.month(yy,mm))

print calendarText()

