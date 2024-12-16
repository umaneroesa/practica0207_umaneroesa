#Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
import os
n= int(input("Introduzca un numero entero entre el 1 y 10 "))
m= int(input("Introduzca un numero entero entre el 1 y 10 "))
nombre = 'tabla-' + str(n) + '.txt'
if os.path.isfile(nombre):
    file = open(nombre, 'r')
    linea= file.readlines()
    x=linea[m:m+1]
    print(x)
    file.close()
else:
    print("No existe")