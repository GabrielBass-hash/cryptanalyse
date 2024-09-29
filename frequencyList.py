import csv
import numpy as np

def readLetterFrequencyOfLanguage(file):

    listOfLanguageLetterFrequency = []
    
    with open(file,newline='') as csvfile:

        reader = csv.reader(csvfile,delimiter = ';')

        for row in reader:
            
            listOfLanguageLetterFrequency.append(row[1:-1])


    return np.transpose(listOfLanguageLetterFrequency)
