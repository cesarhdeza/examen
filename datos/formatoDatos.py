'''
Created on 5 jul. 2022

@author: cesar.hernandez
'''

from archivo import consultaArchivo

def datos():
    lista = consultaArchivo.leer_datos()
    return lista

def datosEmpleado():
    lista = datos()
    listaFormato = []
    for i in lista:
        a = valores(i)
        listaFormato.append(a)
    return listaFormato
    

def valores(cadena):
    listavalores = cadena.replace('\n', '')
    listavalores = listavalores.split(', ')
    return listavalores

def crearDiccionarioEmployee(lista):
    diccionarioEmployee = {'surname': lista[1], 'firstname': lista[0]}
    return diccionarioEmployee

def crearDiccionarioCountry(lista):
    diccionarioCountry = {'code': '', 'name': lista[2],}
    return diccionarioCountry

def crearDiccionarioLanguaje(lista):
    diccionarioLanguaje = {'name': lista[3]}
    return diccionarioLanguaje

def crearDiccionarioAirport(lista):
    diccionarioAirport = {'name': lista[4]}
    return diccionarioAirport


