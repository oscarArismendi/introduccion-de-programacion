import json
import random

def generar_estudiantes():

    campers = [
        
    ]
    nombres = ["Arthuro","Carlos","Luis","Marta","Ana","Maria"]
    apellidos = ["Villalobo","Arismendi","Vega","Nogera","Aceros","Vasquez"]
    direcciones = ["Centro","Bosque","Pidecuentas","Floridablanca","Cabecera","Real de minas"]
    acudientes = ["Sandra","Maria","Teresa",]
    celular = "31"
    for i in range(8):
        celular += str(random.randint(0,9))
    casa = "6076"
    for i in range(0,6,1):
        casa += str(random.randint(0,9))
    estados = ["inscrito","aprobado","reprobado"]
    for i in range(0,33,1):#(33) 0 1 2 --- 32 
        obje = {
            "nro_de_identificacion":i+1,
            "nombre" : nombres[random.randint(0,6)],
            "Apellidos" : apellidos[random.randint(0,6)]+apellidos[random.randint(0,6)],
            "direccion" : direcciones[random.randint(0,6)],
            "acudientes" : acudientes[random.randint(0,2)],
            "telefonos" :[celular,casa],
            "estado" : estados[random.randint(0,2)]
        }
        campers.append(obje)
    return campers

def añadir_estudiante():
    nombre = input("Ingrese nombre estudiante")
    obj = {"nombre":nombre}
    return obj

