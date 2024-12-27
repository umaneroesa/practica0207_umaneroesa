#Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa debe  incorporar funciones para crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.
import os
file= open("listin.txt" , "w")
file.close()
seleccion=input("Seleccione una opcion: \n 1. Crear fichero no existente \n 2. Consultar numero de cliente \n 3. Añadir telefono nuevo cliente \n 4. Eliminar un telefono \n Seleccion: ")
select=int(seleccion)
while select!=0:
    if select==2:
        nombre=input("Nombre del cliente: ")
        if os.path.isfile("listin.txt"):
            file=open("listin.txt", "r")
            print(file.readline())
            file.close()
        else:
            print("No esixte")
    elif select==3:
        file=open("listin.txt","a")
        nombre= input("Nombre del cliente: ")
        numero = input("Numero de telefono de " + nombre + ": ")
        file.write(nombre + ", " + numero)
        file.close()
    elif select==4:
        nombre= input("Nombre del cliente: ")
        if os.path.isfile("listin.txt"):
            os.remove(nombre)
            file.close()
        else:
            print("No esixte")
    seleccion=input("Seleccione una opcion: \n 1. Crear fichero no existente \n 2. Consultar numero de cliente \n 3. Añadir telefono nuevo cliente \n 4. Eliminar un telefono \n Seleccion: ")
    select=int(seleccion)
