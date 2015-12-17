import gotoMainFolderDirectory
import textFileOperations


def nameDayDictionaryCreation():
    gotoMainFolderDirectory.go()
    dataString = textFileOperations.textFileToString("mediaFilesPackage/eortes.dat")
    dataList = dataString.split('\n\n')

    nameDayDictionary = {}
    for day in dataList:
        stringNames = ""
        dayList = day.split("\n")
        date = dayList[0]
        date = date.split(" ")
        date = date[0]
        dayList.pop(0)
        dayString = ""
        for name in dayList:
            name = name.strip()
            dayString  += name+"\n"
        # put date and names in dictionary
        # dictionary key: date, format: "day/month"
        # dictionary value: names, type:String
        nameDayDictionary.update({date:dayString})
    return nameDayDictionary

#print nameDayDictionaryCreation()