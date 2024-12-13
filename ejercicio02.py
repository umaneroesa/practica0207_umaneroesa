#Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, donde n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
import os

n= int(input("Introduzca un numero entero entre el 1 y 10 "))
nombre = 'tabla-' + str(n) + '.txt'

if os.path.isfile(nombre):
    file = open(nombre, 'r')
    print(file.read())
    file.close()
else:
    print("No existe")