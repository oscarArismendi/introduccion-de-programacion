# # # Debido a la gran cantidad de crímenes y casos sin resolver, la policía local ha decidido implementar su propio sistema de reconocimiento de sospechosos con la técnica basada en el uso del DNA.
# # # Para esto la policía mantiene dos listas de información; la primera contiene el nombre de las personas registradas en la región (nombre y apellido), la otra, un cromosoma representativo del DNA de cada una de esas personas.
# # # Por simplicidad, un cromosoma se considera como una cadena de 0 (ceros) y 1 (unos), de largo 20.
# # # El método para determinar el sospechoso, es el siguiente:
# # #     Se obtiene una muestra del cromosoma del autor del delito (20 caracteres)
# # #     Se busca en la lista de cromosomas, aquel cromosoma que es más parecido a la muestra. El más parecido se define como el cromosoma que tiene más genes (caracteres) iguales a la muestra.
# # #     Al terminar la búsqueda, se muestra el nombre de la persona cuyo cromosoma es sospechoso, con el porcentaje de parentesco.
# # # La informacíon inicial del programa se debe ingresar directamente en el código, es decir, nombres y cromosomas, en cambio la secuencia encontrda en la escena del crimen, debe ser ingresada por el usuario.
# # # Desarrolle un programa que lleve a cabo la búsqueda descrita a partir de una muestra de entrada.Recuerde que como se trata de dos listas, la información del nombre como la de los cromosomas, deben estar en la misma posición en ambas listas.
# # # Consideremos, personas como Pedro, Juan y Diego. Sus secuencias serán:
# # #     00000101010101010101
# # #     00101010101101110111
# # #     00100010010000001001

#inicializamos variables:
lista_nombres =["Pedro","Juan","Diego"] 
lista_cromosomas = ["00000101010101010101","00101010101101110111","00100010010000001001"]
indice_culpable = 0
porcentaje_culpable = -1
cromosoma_culpable = input("Ingrese secuencia: ")
cantidad_de_personas = len(lista_nombres)
#ciclo para recorrer todos los nombres y cromosomas en las dos listas:
for i in range(0,cantidad_de_personas,1): 
    porcentaje_actual = 0 
    cromosoma_actual = lista_cromosomas[i]
    #ciclo para recorrer el cromosoma del culpable y compararlo con cada persona
    for j in range(0,20,1):
        if cromosoma_actual[j] == cromosoma_culpable[j]:
            porcentaje_actual += 5
    
    #vemos si aumento el porcentaje del culpable y de ser asi escogemos a nuestro nuevo sospechoso
    if porcentaje_actual > porcentaje_culpable:
        porcentaje_culpable = porcentaje_actual
        indice_culpable = i
print("El culpable es {} con un parentezco de {}%".format(lista_nombres[indice_culpable],porcentaje_culpable))
