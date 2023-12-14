""" **********************************************************
    Universidad de Cádiz
    Recuperación de la Información
    Proyecto RI
    Jorge Guerrero Díaz
    Cristian Leilael Rico Espinosa
********************************************************** """
# Import Libraries
import os
from tika import parser

#Logic to evaluate if a word can get in the index
#Size of words
#Number of repetitions of the same word
#Dictionary of words nah nah
# Function to see if the kw already exists

def logic(i):
    if (len(i) > 2):
        print(i)
        return i

#Split the content in each word
def insertdic(parsed_document,files):
    res = parsed_document.split() 
    for i in res: 
        #kw = logic(i)
        print(i)
        if (index.has_key(i) == False):
            index[i] = files



# folderPath = '.\\corpus' 
folderPath = '.\\corpus\\'
corpusFiles = [file for file in os.listdir(folderPath)]

index = {}
i = 0

#Read all the content for each file in the directory
for files in corpusFiles:
    path = '.\\corpus\\'+ files
    parsed_document = parser.from_file(path)
    print(parsed_document['content'])
    insertdic(parsed_document['content'],files)

