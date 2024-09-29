import vigenere
import caesar
import input

def main():

    choiceProcess,cryptoType,message,key= input.inputInit()
    
    if choiceProcess == "decrypt":

        if cryptoType == "caesar":

            print(caesar.caesarCypherDecrypt(message,key))

        else:

            print(vigenere.vigenereDecrypt(message,key))

    else:

        if cryptoType == "caesar":

            print(caesar.caesarCypherEncrypt(message,key))

        else:

            print(vigenere.vigenereDecrypt(message,key))
            
main()