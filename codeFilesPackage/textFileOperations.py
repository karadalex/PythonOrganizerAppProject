def textFileToString(textFile):
    text = open(textFile, "r")
    string = ""
    for line in text:
        string += line
    text.close()
    return string

def textFileToListWithStrings(textFile):
    text = open(textFile, "r", encoding="utf8")
    listOfTextLinesStrings = []
    for line in text:
        listOfTextLinesStrings.append(line)
    text.close()
    return listOfTextLinesStrings
