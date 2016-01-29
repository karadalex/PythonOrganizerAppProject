# -*- coding: utf-8 -*-

def greekToGreeklish(character):
    greekCharactersUpperList1 = "Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ Σ Τ Υ Φ Χ Ψ Ω".split(" ")
    latinCharactersUpperList1 = "A B G D E Z H TH I K L M N KS O P R S T Y F X PS W".split(" ")

    greekCharactersLowerList1 = "α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ σ τ υ φ χ ψ ω".split(" ")
    latinCharactersLowerList1 = "a b g d e z h th i k l m n ks o p r s t u f x ps w".split(" ")

    greekCharactersUpperPrimeList2 = "Ά Έ Ή Ί Ό Ύ Ώ".split(" ")
    latinCharactersUpperList2 = "A E H I O Y W".split(" ")

    greekCharactersLowerPrimeList2 = "ά έ ή ί ό ύ ώ".split(" ")
    latinCharactersLowerList2 = "a e h i o u w".split(" ")

    greekCharactersUpperList3 = "Ϊ Ϋ".split(" ")
    latinCharactersUpperList3 = "I Y".split(" ")

    greekCharactersLowerList3 = "ϊ ϋ".split(" ")
    greekCharactersUpperList4 = "ΐ ΰ".split(" ")
    latinCharactersLowerList3 = "i u".split(" ")

    #conversion
    if character in greekCharactersUpperList1:
        for i in range(len(greekCharactersUpperList1)):
            if character == greekCharactersUpperList1[i]:
                return latinCharactersUpperList1[i]


    elif character in greekCharactersLowerList1:
        for i in range(len(greekCharactersLowerList1)):
            if character == greekCharactersLowerList1[i]:
                return latinCharactersLowerList1[i]


    elif character in greekCharactersUpperPrimeList2:
        for i in range(len(greekCharactersUpperPrimeList2)):
            if character == greekCharactersUpperPrimeList2[i]:
                return latinCharactersUpperList2[i]


    elif character in greekCharactersLowerPrimeList2:
        for i in range(len(greekCharactersLowerPrimeList2)):
            if character == greekCharactersLowerPrimeList2[i]:
                return latinCharactersLowerList2[i]


    elif character in greekCharactersUpperList3:
        for i in range(len(greekCharactersUpperList3)):
            if character == greekCharactersUpperList3[i]:
                return latinCharactersUpperList3[i]


    elif (character in greekCharactersLowerList3) or (character in greekCharactersUpperList4):
        for i in range(len(greekCharactersLowerList3)):
            if (character == greekCharactersLowerList3[i]) or (character == greekCharactersUpperList4[i]):
                return latinCharactersLowerList3[i]


    else:
        return character


def greekStringToGreeklishString(string):
    strList = string.split(" ")
    for i in range(len(strList)):
        j = 0
        convertedWord = ""
        while j < len(strList[i])-1:
            character1 = strList[i][j]
            character2 = strList[i][j+1]
            character = character1 + character2
            character = greekToGreeklish(character)
            convertedWord += character
            j += 2
        strList[i] = ""
        strList[i] += convertedWord
    string = ""
    for word in strList:
        string += word + " "
    return string

# Test cases
#print greekToGreeklish("\xce")
#print greekStringToGreeklishString("Όλα καλά")
#print greekStringToGreeklishString("Εισαγωγή στους Υπολογιστές")