from modulos.inicial import *

# genero la lista inicial de estudiantes
campers = generar_estudiantes()
campers_objeto = json.dumps(campers,indent=4)#pasa la lista de diccionarios a objeto de json
file = open("campers_general.json","w")#sobrescribiendo el archivo completo, lo crea si no existe el archivo
file.write(campers_objeto)
file.close()
# nuevo_estudiante = añadir_estudiante()
# campers.append(nuevo_estudiante)

# campers_objeto = json.dumps(campers,indent=4)
# file = open("campers.json","w")#sobrescribiendo el archivo completo, lo crea si no existe el archivo
# file.write(campers_objeto)
# file.close()


