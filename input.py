
def inputCryptOrDecrypt():

    choiceProcess = { '1' : "Decrypt",
                     '2' : "Encrypt"}

    case = str(input("what do you need today ? :\n1 - Decrypt\n2 - Encrypt\n ->> : "))

    while not case in choiceProcess.keys():

        case = str(input("Please choose an available model from the list :\n1 - Decrypt\n2 - Encrypt\n ->> : "))
    
    return choiceProcess[case]


def inputEncryptMethod( choiceProcesss ):

    methodList= { '1':"caesar", 
                 '2':"Vigenere" }
    
    if choiceProcesss == "Decrypt":
            
        encryptMethod =  str(input("What's the type of encryption is used ? :\n1 - Caesar\n2 - Vigenere\n ->> : "))

        while not encryptMethod in methodList.keys():

            encryptMethod = str(input("Please choose an available model from the list :\n1 - Caesar\n2 - Vigenere\n ->> : "))

    else:

        encryptMethod =  str(input("What's the type of encryption you want to use ? :\n1 - Caesar\n2 - Vigenere\n ->> : "))

        while not '1' <= encryptMethod <= '2':

            encryptMethod = str(input("Please choose an available model from the list :\n1 - Caesar\n2 - Vigenere\n ->> : "))
    
    return methodList[encryptMethod]


def inputInit():

    choiceProcess = inputCryptOrDecrypt()

    cryptoType = inputEncryptMethod( choiceProcess )


inputInit()