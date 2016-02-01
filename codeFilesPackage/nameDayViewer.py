import gotoMainFolderDirectory
import textFileOperations
import greeklish


def nameDayDictionaryCreation():
    gotoMainFolderDirectory.go()
    dataString = textFileOperations.textFileToString("mediaFilesPackage/eortes.dat")
    dataList = dataString.split('\n\n')

    nameDayDictionary = {}
    for day in dataList:
        dayList = day.split("\n")
        date = dayList[0]
        date = date.split(" ")
        date = date[0]
        dayList.pop(0)
        dayString = ""
        for name in dayList:
            name = name.strip()
            name = name.replace("(", "")
            name = name.replace(")", "")
            namesList = name.split(",")
            name = ""
            if len(namesList) > 1:
                name += "("
            for i in range(len(namesList)):
                namesList[i] = greeklish.greekStringToGreeklishString(namesList[i])
                name += namesList[i]+","
            if len(namesList) > 1:
                name += ")"
            dayString  += name+"\n"
        # put date and names in dictionary
        # dictionary key: date, format: "day/month"
        # dictionary value: names, type:String
        nameDayDictionary.update({date:dayString})
    return nameDayDictionary


# Uncomment to check function nameDayDictionaryCreation()
#print nameDayDictionaryCreation()