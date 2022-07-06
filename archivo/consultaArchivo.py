'''
Created on 5 jul. 2022

@author: cesar.hernandez
'''

#Recuperar los clientes
def leer_datos():
    clientes = []
    try:
        archivo = open("C:/Users/cesar.hernandez/Desktop/Python/examen/archivos/Clientes.txt")
        linea = archivo.readline()
        while linea != "":
            clientes.append(linea)
            linea = archivo.readline()
        archivo.close
    except FileNotFoundError:
        print("Archivo no encontrado")
    except FileExistsError:
        print("El archivo ya existe")
    return clientes

