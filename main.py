""" **********************************************************
    Universidad de Cádiz
    Recuperación de la Información
    Proyecto RI
    Jorge Guerrero Díaz
    Cristian Leilael Rico Espinosa
********************************************************** """

# Import Libraries
from tika import parser

filepath = '.\\corpus\\000084578400037'  # Path for 1 file.
parsed_document = parser.from_file(filepath)

print(parsed_document['content'])
