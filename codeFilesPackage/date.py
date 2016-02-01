import time

def numberOfDay():
    day = time.strftime("%d")
    if day[0] == '0':
        day = day[1:]
    return day

def numberOfMonth():
    month = time.strftime("%m")
    if month[0] == '0':
        month = month[1:]
    return month

def fullWeekDayName():
    dayName = time.strftime("%A")
    return dayName

def fullMonthName():
    monthName = time.strftime("%B")
    return monthName

def numberOfYear():
    year = time.strftime("%Y")
    return year


class fullDateString():
    """Date format example:
        Thursday 17 December 2015
    """
    def __init__(self):
        self.dayName = fullWeekDayName()
        self.day = numberOfDay()
        self.monthName = fullMonthName()
        self.month = numberOfMonth()
        self.year = numberOfYear()

    # Define output of command "print <fullDateString>" :
    def __str__(self):
        return self.dayName+" "+str(self.day)+" "+self.monthName+" "+str(self.year)

class shortDateString():
    """Date format example:
        17/12
    """
    def __init__(self):
        self.day = numberOfDay()
        self.month = numberOfMonth()

    def __str__(self):
        return str(self.day)+"/"+str(self.month)