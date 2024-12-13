#Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.
n= int(input("Introduzca un numero entero entre el 1 y 10 "))
nombre = 'tabla-' + str(n) + '.txt'
file = open(nombre, 'w')
for i in range(0,11):
    file.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) +  '\n')
file.close()
file = open(nombre, 'r')
contenido = file.read()
print(contenido)