#Escribir un programa que acceda al fichero de internet mediante la url indicada y muestre por pantalla el número de palabras que contiene.
import urllib.request
import os
url = "http://textfiles.com/adventure/aencounter.txt"
file = urllib.request.urlopen(url)
for line in file:
    decoded_line = line.decode()

    palabras = file.read()
    print(len(palabras.split()))
    file.close()
