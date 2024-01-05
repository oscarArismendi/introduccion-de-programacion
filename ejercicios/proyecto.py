#1. Registro de campers : El programa debe permitir a las personas encargadas de procesar las #inscripciones
#a el programa; la información que se tiene por cada camper es la siguiente : nro de identificación, #nombre,
#Apellidos, dirección, acudiente, teléfonos de contacto(Nro celular y nro fijo),estado.
#1) campers = []
#   ruta = ["Ruta NodeJS", "Ruta Java", "Ruta NetCore"] 
# En python quiero crear funcion que se añada a campers el diccionario 
    # {
        # identificacion:input
        # nombre: input
        # apellido: input
        # direcion:input 
        # acudiente:input
        # telefono:input
        # estado: input
        #ruta: input(""Ruta NodeJS", "Ruta Java", "Ruta NetCore"") # la ruta puede ser aleatorio ruta[random(0,2)]
    # }
    #el diccionario toca añadirlo a campers
    # campers.append(diccionario)
#pasar json  a la lista campers 
#2)
# nro de identificación, nombre,Apellidos, dirección, acudiente, teléfonos de contacto(Nro celular y nro fijo),estado.
import json
import random

def generar_estudiantes():

    campers = [
        
    ]
    nombres = ["Arthuro","Carlos","Luis"]
    apellidos = ["Villalobo","Arismendi","Vega"]
    direcciones = ["Centro","Bosque","Pidecuentas"]
    acudientes = ["Sandra","Maria","Teresa"]
    telefonos = [["318","607625"],["317","607631"],["316","607615"]]
    estados = ["Activo","Inactivos"]
    for i in range(0,33,1):#(33) 0 1 2 --- 32 
        obje = {
            "nro_de_identificacion":i+1,
            "nombre" : nombres[random.randint(0,2)],
            "Apellidos" : apellidos[random.randint(0,2)],# 0%3 = 0 1%3 = 1 2%3 = 2 3 % 3 = 0
            "direccion" : direcciones[random.randint(0,2)],
            "acudientes" : acudientes[random.randint(0,2)],
            "telefonos" : telefonos[random.randint(0,2)],
            "estado" : estados[random.randint(0,1)]
        }
        campers.append(obje)
    return campers

def añadir_estudiante():
    nombre = input("Ingrese nombre estudiante")
    obj = {"nombre":nombre}
    return obj

campers = generar_estudiantes()
campers_objeto = json.dumps(campers,indent=4)#pasa diccionario a objeto
file = open("campers.json","w")#sobrescribiendo el archivo completo, lo crea si no existe el archivo
file.write(campers_objeto)
file.close()
nuevo_estudiante = añadir_estudiante()
campers.append(nuevo_estudiante)

campers_objeto = json.dumps(campers,indent=4)
file = open("campers.json","w")#sobrescribiendo el archivo completo, lo crea si no existe el archivo
file.write(campers_objeto)
file.close()

