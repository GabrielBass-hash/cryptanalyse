import string

def caesarCypherEncrypt(stringToEncrypt, key):

    stringEncrypted = ""

    for char in stringToEncrypt:

        if string.isupper(char):

            placeOfLetter = (ord(char) - ord('A') + key) % 26

            stringEncrypted += chr(ord('A') + placeOfLetter)

        elif string.islower():

            placeOfLetter = (ord(char) - ord('a') + key) % 26

            stringEncrypted += chr(ord('a')+ placeOfLetter)

        else:

            stringEncrypted += char

    return stringEncrypted


def caesarCypherDecrypt(stringToEncrypt, key):

    stringEncrypted = ""

    for char in stringToEncrypt:

        print(char)

        if char.isupper():

            placeOfLetter = (ord(char) - ord('A') - key) % 26

            stringEncrypted += chr(ord('A') + placeOfLetter)

        elif char.islower():

            placeOfLetter = (ord(char) - ord('a') - key) % 26

            stringEncrypted += chr(ord('a')+ placeOfLetter)

        else:

            stringEncrypted += char

    return stringEncrypted
