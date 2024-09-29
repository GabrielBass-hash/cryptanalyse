import caesar
import frequencyList

numberLetter = 26

def vigenereEncrypt(messageToEncrypt,key):

    encryptedMessage=""

    key = key.upper()

    for i in range (len(messageToEncrypt)):

        if messageToEncrypt[i].isupper() or messageToEncrypt[i].islower():

            gap=ord(key[i % len(key)]) - ord('A')

            encryptedMessage += caesar.caesarCypherEncrypt(messageToEncrypt[i],gap)

        else:

            encryptedMessage+=messageToEncrypt[i]

    return encryptedMessage


def vigenereDecrypt(messageToDecrypt,key):

    decryptedMessage=""

    key = key.upper()

    for i in range (len(messageToDecrypt)):

        if messageToDecrypt[i].isupper() or messageToDecrypt[i].islower():

            gap=ord(key[i % len(key)]) - ord('A')

            decryptedMessage += caesar.caesarCypherDecrypt(messageToDecrypt[i],gap)

        else:

            decryptedMessage+=messageToDecrypt[i]

    return decryptedMessage


def messageGroup(message,lenghtKey):

    groupList = [""] * lenghtKey

    for i in range (len(message)):

        if message[i].isupper() or message[i].islower():

            groupList[iGroup%lenghtKey] += message[i]

            iGroup+=1

    return groupList


def countLetter(string):

    letterCountList = [0] * numberLetter

    for char in string:

        indexToPush = ord(char.upper()) - 65

        letterCountList[indexToPush] += 1
        
    return letterCountList


def letterFrequencyList(letterCountList):

    letterFrequencyList = [0] * numberLetter

    for i in range (len(letterFrequencyList)):

        letterFrequencyList[i] = (letterCountList[i] / sum(letterCountList))*100

    return letterFrequencyList

def listStringGapped(string):

    listOfGappedString=[]

    for i in range (numberLetter):

        listOfGappedString.append(caesar.caesarCypherDecrypt(string , i))

    return listOfGappedString
