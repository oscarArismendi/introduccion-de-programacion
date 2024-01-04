# # # Nivel principiante
# # # 1)Se requiere realizar un programa en Python que permita leer 3 números enteros positivos e imprima
# # # La sumatoria de los tres números.
# # # #solucion 1:
# print("Ingrese 3 numeros enteros positivos: ")
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# print(a+b+c)
# # # solucion 2:
# lista_numeros = [0,0,0]
# print("Ingrese 3 numeros:")
# for i in range(3):
#     lista_numeros[i] = int(input(""))
# print("La suma de los 3 numeros es:",sum(lista_numeros))
# # # 2. El centro de salud de campuslands desea realizar un programa que le permita calcular el IMC de los Estudiantes nuevos.
# # # El programa debe mostrar el nombre del estudiante, la edad, el imc y la categoría según el IMC obtenido
# # # Ver Imagen suministrada.
#el nombre en 0, edad en 1, peso en 2 ,altura en metros en 3 y despues del for imc en 4
# imc_estudiantes = [["Oscar",27,60,1.73]]
# i = 0
# for imc in imc_estudiantes:
#     imc_estudiantes[i]=tuple(imc+[imc[2]/(imc[3]**2)])
#     i += 1
# categoria = "Debajo de los valores normales"

# if imc_estudiantes[0][4] > 40.0:
#     categoria = "OBESIDAD III"
# elif imc_estudiantes[0][4] >= 35.0:
#     categoria = "OBESIDAD II"
# elif imc_estudiantes[0][4] >= 30.0:
#     categoria = "OBESIDAD I"
# elif imc_estudiantes[0][4] >= 25.0:
#     categoria = "SOBREPESO"
# elif imc_estudiantes[0][4] >= 18.5:
#     categoria = "NORMAL"

# print("El estudiante {} de edad {} tiene un imc de {:.2f} lo cual lo pone en la categoria de {}".format(imc_estudiantes[0][0],imc_estudiantes[0][1],imc_estudiantes[0][4],categoria))
# # # 3. Teniendo en cuenta el punto 2 se requiere tener el registro de 20 estudiantes y poder determinar
# # # el estado de salud de la comunidad estudiantil. El programa debe mostrar el siguiente reporte:}
# # # a. Cuantos estudiantes se encuentran en el peso ideal.
# # # b. Cuantos estudiantes se encuentran en obesidad grado I
# # # c. Cuantos estudiantes se encuentran en obesidad grado II
# # # d. Cuantos estudiantes se encuentran en obesidad grado III
# # # e. Cuantos estudiantes se encuentran en Sobrepeso
#el nombre en 0, edad en 1, peso en 2 ,altura en metros en 3 y despues del for imc en 4
# imc_estudiantes = [["1.",27,61,1.73],["2.",27,62,1.63],["3.",27,63,1.73],["4.",27,64,1.73],["5.",27,65,1.73],["6.",27,66,1.73],
#                    ["7.",27,67,1.73],["8.",27,68,1.73],["9.",27,69,1.73],["10.",27,70,1.73],["11.",27,71,1.73],["12.",27,72,1.73],
#                    ["13.",27,73,1.73],["14.",27,74,1.73],["15.",27,75,1.73],["16.",27,76,1.73],["17.",27,77,1.73],["18.",27,78,1.73],
#                    ["19.",27,79,1.73],["20.",27,80,1.73]]
# i = 0
# for imc in imc_estudiantes:
#     imc_estudiantes[i]=tuple(imc+[imc[2]/(imc[3]**2)])
#     i += 1
# obesidad_3 = 0
# obesidad_2 = 0
# obesidad_1 = 0
# sobrepeso =  0
# normal = 0
# debajo_de_normal = 0

# for imc in imc_estudiantes:
#     if imc[4] > 40.0:
#         obesidad_3 += 1
#     elif imc[4] >= 35.0:
#         obesidad_2 += 1
#     elif imc[4] >= 30.0:
#         obesidad_1 += 1
#     elif imc[4] >= 25.0:
#         sobrepeso += 1
#     elif imc[4] >= 18.5:
#         normal += 1
#     else:
#         debajo_de_normal += 1
# print("La cantidad de estudiantes que se encuentra debajo del peso ideal son",debajo_de_normal)
# print("La cantidad de estudiantes que se encuentra en peso ideal son",normal)
# print("La cantidad de estudiantes que se encuentra en sobrepeso son",sobrepeso)
# print("La cantidad de estudiantes que se encuentra en obesidad grado I son",obesidad_1)
# print("La cantidad de estudiantes que se encuentra en obesidad grado II son",obesidad_2)
# print("La cantidad de estudiantes que se encuentra en obesidad grado III son",obesidad_3)
# # # 4)Se desea realizar un programa en Python que permita ingresar n números enteros positivos y cuando se
# # # Ingrese un numero negativo debe mostrar en pantalla el siguiente reporte.
# # # a. Total de números ingresados
# # # b. Total de números pares ingresados
# # # c. Promedio de los números pares
# # # d. Promedio de los números impares
# # # e. Cuantos números son menores que 10
# # # f. Cuantos números están entre 20 y 50
# # # g. Cuantos números son mayores que 100
# # # Pensamientos:
# # #     1)Hacer una lista donde almacenare los numeros
# # #     2) recibir los numeros en un bucle 
# # #     3) Hacer un bucle que pase por la lista y cuente cada uno de las variables necesarios
# lista_numeros = []
# x = 0
# print("Ingrese numeros:")
# while (x >= 0):
#     x = int(input(""))
#     if(x >= 0):
#         lista_numeros.append(x)
# numeros_ingresado = len(lista_numeros)# pregunta a
# contador_pares = 0 # pregunta b
# promedio_pares = 0 # pregunta c
# contador_impares = 0
# promedio_impares = 0 # pregunda d
# contador_menores_10 = 0#pregunta e
# contador_entre_20_y_50 = 0 #pregunta f
# contador_mayor_100 = 0 # pregunta g
# for  x in lista_numeros:
#     if (x % 2 == 0):
#         contador_pares += 1
#         promedio_pares += x
#     else:
#         contador_impares += 1
#         promedio_impares += x
#     if (x < 10):
#         contador_menores_10 += 1 
#     elif (x >= 20 and x <= 50):
#         contador_entre_20_y_50 += 1 
#     elif (x > 100):
#         contador_mayor_100 += 1

# if(contador_pares != 0):
#     promedio_pares /= contador_pares
# if(contador_impares != 0):
#     promedio_impares /= contador_impares
# print("Los siguientes datos son de los numeros enteros positivos ingresados:")
# print("Total de numeros ingresados",numeros_ingresado)
# print("Total de numeros pares ingresados:",contador_pares)
# print("Promedio de los numeros pares:",promedio_pares)
# print("Promedio de los numeros impares:",promedio_impares)
# print("Numeros menores de 10:",contador_menores_10)
# print("Numeros entre 20 y 50:",contador_entre_20_y_50)
# print("Numeros mayores que 100:",contador_mayor_100)
# # # Nivel intermedio
# # # 1)El centro de prevención de sismos en Colombia desea realizar un programa que le permita llevar el
# # # Registro del los sismos presentados en 5 ciudades del país. Por cada ciudad se realizan n cantidad de
# # # Registros. El programa debe permitir registrar las muestras del movimiento en cada ciudad.
# # # Requerimientos:
# # # 1. El programa debe tener un menú con las siguientes opciones
# # # 1. Registrar Ciudad
# # # 2. Registrar Sismo
# # # 3. Buscar sismos por ciudad
# # # 4. Informe de riesgo
# # # 5. Salir
# # # Restricciones:
# # # 1. Todas las ciudades deben tener la misma cantidad de sismos registrado
# # # 2. El informe de riesgos presenta la siguiente clasificación:
# # # 1. Amarillo (Sin riesgo) : El promedio de los sismos es < 2,5
# # # 2. Naranja (Riesgo medio) : El promedio de los sismos esta entre 2.6 y 4.5
# # # 3. Rojo (Riesgo alto) : El promedio de los sismos es mayor a 4.5
# # # La solución debe implementar listas , listas dentro de listas
# # # pensamientos:
# # #     1)Hacer una lista de ciudades donde el primer valor de la lista sea el nombre de la ciudad ingresada
# # #     2)Para los sismos tiene que ingresar el nombre de la ciudad y el puntaje del sismo
# # #     3)En buscar sismos por ciudad si escribe el nombre de la ciudad mostrarle los sismos
# # #     4)En el segundo espacio de la lista tener el promedio de la ciudad y mostrar la clasificacion en el informe de riesgo
# # #     5)El salir no saca del programa, en otras palabras el bucle principal
# lista_ciudades = []
# estado_menu = 0
# n = 3 # cantidad por ciudad
# nombres_ciudades = []
# while(estado_menu != 5):
#     print("1. Registar ciudad")
#     print("2. Registar sismo")
#     print("3. Buscar sismo por ciudad")
#     print("4. Informe de riesgo")
#     print("5. Salir")
#     estado_menu = int(input(""))
#     if(estado_menu == 1):#Registro de ciudad
#         nombre = input("Ingrese el nombre de la ciudad: ")
#         lista_ciudades.append([nombre,0])#nombre y promedio
#         nombres_ciudades.append(nombre)
#         estado_menu = 0
#     elif (estado_menu == 2): #Registro sismo
#         nombre = input("Ingrese la ciudad del sismo: ")
#         # estado = any(nombre in ciudad for ciudad in lista_ciudades)
#         indice = 0
#         for ciudad in lista_ciudades:
#             if(ciudad[0] == nombre):
#                 break
#             indice += 1
#         if(indice == len(lista_ciudades)):
#             print("La ciudad no se encuentra en la lista")
#         else:
#             contador_sismos = len(lista_ciudades[indice])-2
#             print(f"la ciudad debe tener {n} registros de sismos actualmente tiene {contador_sismos}")
#             while(contador_sismos < n):
#                 sismo = float(input("Ingrese la magnitud del sismo: "))
#                 lista_ciudades[indice].append(sismo)
#                 lista_ciudades[indice][1] += sismo #promedio en la ciudad
#                 contador_sismos += 1
#             print("Ya se ha completado el numero de registros necesarios en esta ciudad")
#         estado_menu = 0
#     elif (estado_menu == 3): # Buscar sismo por ciudad
#         nombre = input("Ingrese el nombre de la ciudad: ")
#         for ciudad in lista_ciudades:
#             if(ciudad[0] == nombre):
#                 for i in range(len(ciudad)):
#                     if(i > 1):
#                         print(ciudad[i],end = " ")
#                 break
#             indice += 1
#         if(indice == len(lista_ciudades)):
#             print("La ciudad no se encuentra en la lista")
#             estado_menu = 0
#             break
#         else:
#             print("")
#     elif (estado_menu == 4): #informe de riesgo
#         for ciudad in lista_ciudades:
#             cantidad = len(ciudad)-2
#             riesgo = 0.0
#             if(cantidad != 0):
#                 riesgo = ciudad[1]/cantidad
#             else:
#                 continue
#             print(f"{ciudad[0]} riesgo: ",end="")
#             if(riesgo < 2.6):
#                 print("Amarillo (Sin riesgo)")
#             elif (riesgo >=2.6 and riesgo <= 4.5):
#                 print("Naranja (Riesgo medio)")
#             else:
#                 print("Rojo (Riesgo alto)")
# # # 2) La alcaldía de Bucaramanga desea realizar un programa que le permita calcular el valor de CO2 producido
# # # En las diferentes instalaciones gubernamentales de la ciudad. Tenga en cuenta las siguientes observaciones:
# # # El programa debe permitir mostrar cual de las instalaciones tiene mayor producción de CO2.
# # # Requerimientos: El programa debe contar con un menú principal que permita realizar todos los
# # # Procesos solicitados.
# # # 1. Registrar Dependencia
# # # 2. Registrar consumo por dependencia : Tengan en cuenta que se debe registrar los valores
# # # consumidos por los dispositivos en cada una de las oficinas.
# # # 3. Ver CO2 producido
# # # 4. Dependencia que produce mayor CO2
# # # 5. Salir
# # # pensamientos:
# # #     1) Hacer un diccionario para las dependencias 
# # #     2) Hacer el menu que va a ser un while 
# # #     3) para registrar dependencia que ponga solo el nombre y agregarla al diccionario
# # #     4) Para registrar un consuma hacer un menu que diga registrar dispositivo en el cual dira si es electrodomestico o transporte
# # #     5) Sumatoria de todos los co2
# # #     6) Mostrar el nombre de la dependencia que produce mayor CO2
# # #     7) salir cuando estado_menu sea igual a 5
# dependencias = {}
# estado_menu = 0
# while (estado_menu != 5):#menu principal
#     print("1. Registrar Dependencia")
#     print("2. Registrar consumo por dependencia")
#     print("3. Ver CO2 producido")
#     print("4. Dependencia que produce mayor CO2")
#     print("5. Salir")
#     estado_menu = int(input(""))
#     if(estado_menu == 1):#registro de dependencia
#         nombre = input("Ingrese el nombre de la dependencia: ")
#         if(dependencias.get(nombre) != None):
#             print("Ya esta registrada la dependencia")
#         else:
#             dependencias[nombre] = []
#     elif (estado_menu == 2):#registro consumo de dependencia
#         estado_registro = 0
#         while(estado_registro != 2):
#             print("1.Registrar un electrodomestico")
#             print("2.Registrar un transporte")
#             print("3.Volver al menu principal")
#             opcion_usuario = int(input(""))
#             if(opcion_usuario == 3):
#                 break
#             dependencia = ""
#             while(dependencias.get(dependencia) == None):
#                 dependencia = input("Ingrese el nombre de la dependencia donde hara el registro: ")
#             if(opcion_usuario == 1):
#                 nombre = input("Ingrese el nombre del electrodomestico: ")
#                 tiempo = float(input("Ingrese el tiempo de uso en horas: "))
#                 consumo = int(input("Ingrese los kwh consumidos por {}: ".format(nombre)))
#                 consumo = float((consumo/1000)*0.3)
#                 dependencias[dependencia].append([nombre,consumo*tiempo])#añade el nombre del electrodomestico y lo emetido en co2
#             elif(opcion_usuario == 2):
#                 nombre = input("Ingrese el nombre del transporte: ")
#                 recorrido = float(input("Ingrese los kilometros recorridos: "))
#                 dependencias[dependencia].append([nombre,recorrido*31.7])#añade el nombre del transporte y lo emetido en co2
#             elif(opcion_usuario == 3):
#                 estado_registro = 2
#         estado_registro = 0
#     elif(estado_menu == 3):#ver co2 producido
#         total = 0.0
#         for dependencia in dependencias:
#             for datos in dependencias[dependencia]:
#                 total += datos[1]#sumo lo emitdo en co2
#         print(f"El total emitido en CO2 es: {total}")
#     elif(estado_menu == 4):#la dependencia que produce mas CO2
#         total = 0.0
#         mayor = -1
#         nombre = ""
#         for dependencia in dependencias:
            
#             for datos in dependencias[dependencia]:
#                 total += datos[1]#sumo lo emitdo en co2
#             if(total > mayor):
#                 mayor = total
#                 nombre = dependencia
#         print(f"El total emitido en CO2 es: {nombre}")
# # # 3) En el contexto de la gestión de inventarios, se requiere desarrollar un programa en Python que permita
# # # realizar el control detallado de productos en un negocio. Cada producto estará caracterizado por los siguientes
# # # atributos:
# # # •Código del producto.
# # # •Nombre del producto.
# # # •Valor de compra del producto.
# # # •Valor de venta del producto.
# # # •Stock mínimo permitido.
# # # •Stock máximo permitido.
# # # •Nombre del proveedor del producto.
# # # El programa debe cumplir con las siguientes funcionalidades:
# # # 1.Registro de Productos:
# # # 1. El usuario podrá registrar nuevos productos proporcionando la siguiente información: código,
# # # nombre, valor de compra, valor de venta, stock mínimo, stock máximo y nombre del
# # # proveedor.
# # # 2.Visualización de Productos:
# # # 1. El programa deberá permitir la visualización de la lista de productos registrados, mostrando
# # # todos los atributos de cada producto en un formato claro y legible.
# # # 3.Actualización de Stock:
# # # 1. Se debe implementar la posibilidad de actualizar el stock de un producto específico. El
# # # usuario ingresará el código del producto y la cantidad que desea agregar o restar al stock.
# # # 4. Informe de Productos Críticos:
# # # 1. El programa deberá generar un informe que muestre los productos cuyo stock
# # # se encuentra por debajo del límite mínimo establecido.
# # # 5. Cálculo de Ganancia Potencial:
# # # 2. Implementar una función que calcule la ganancia potencial total considerando
# # # la diferencia entre el valor de venta y el valor de compra de cada producto,
# # # multiplicada por la cantidad en stock.
# # # Pensamientos:
# # #     1) hacer un diccionario de productos
# # #     2) En el registro añadir al diccionario como una lista de todos los valores
# # #     3) Imprimir nombre, valor de compra, valor de venta, stock mínimo, stock máximo y nombre de proveedor.
# # #     Despues imprimir la key y los valores de la key
# # #     4) ingresar el codigo del producto y cambiar el stock por el que ponga el usuario
# # #     5)Mostrar keys de productos que esten por debajo de lo establecido
# # #     6)Sumar todas las ganancias

