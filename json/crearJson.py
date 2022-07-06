'''
Created on 5 jul. 2022

@author: cesar.hernandez
'''

import requests
from datos.formatoDatos import crearDiccionarioAirport,crearDiccionarioCountry,crearDiccionarioEmployee,crearDiccionarioLanguaje,datosEmpleado

def lista():
    listaEmpleados = datosEmpleado()
    return listaEmpleados
    
def peticionPost():
    for i in lista():
        employee = crearDiccionarioEmployee(i)
        country = crearDiccionarioCountry(i)
        languaje = crearDiccionarioLanguaje(i)
        airport = crearDiccionarioAirport(i)
        resp1 = requests.post('http://localhost:8080/agregarempl', json= employee)
        resp2 = requests.post('http://localhost:8080/agregarco', json= country)
        resp3 = requests.post('http://localhost:8080/agregarair', json= airport)
        resp4 = requests.post('http://localhost:8080/agregarlan', json= languaje)
        print(resp4)
        


