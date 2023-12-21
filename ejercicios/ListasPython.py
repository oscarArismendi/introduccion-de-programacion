#              0, 1, 4, 5, 9
# # # >>> a = [5, 1, 4, 9, 0]
# # # >>> b = list(range(3, 10)) + list(range(20, 23)) -> [3,4,5,6,7,8,9] + [20,21,22] = [3,4,5,6,7,8,9,20,21,22]
# # # >>> c = [[1, 2], [3, 4, 5], [6, 7]] 
#        c=[ 1,2
#            3,4,5
#            6,7
#]
# # # >>> d = ['perro', 'gato', 'jirafa', 'elefante']
# # # >>> e = ['a', a, 2 * a] => [  'a',
#                                   [5, 1, 4, 9, 0],
#                                   [5, 1, 4, 9, 0, 5, 1, 4, 9, 0]
#]
# # # Sin usar el computador, indique cuál es el resultado y el tipo de las siguientes expresiones. A continuación, verifique sus respuestas en el computador.
# a = [5, 1, 4, 9, 0]
# b = list(range(3, 10)) + list(range(20, 23))
# c = [[1, 2], [3, 4, 5], [6, 7]]
# d = ['perro', 'gato', 'jirafa', 'elefante']
# e = ['a', a, 2 * a]
# print("a[2] = ",a[2]) # a[2] = 4 good
# print("b[9] = ",b[9]) # b[9] = 22 good
# print("c[1][2] = ",c[1][2]) # c[1][2] = 5 good
# print("e[0]== e[1] = ",e[0]== e[1]) # e[0] == e[1] = False good
# print("len(c) = ",len(c)) # len(c) = 3 good
# print("len(c[0]) = ",len(c[0])) # len(c[0]) = 2 godd
# print("len(e) = ",len(e)) # len(e) = 3 good
# print("c[-1] = ",c[-1]) # c[-1] = [6,7] good
# print("c[-1][+1] = ",c[-1][+1]) # c[-1][+1] = 7 good
# print("c[2:] + d[2:] = ",c[2:] + d[2:])# c[2:] + d[2:] = [6,7] + ["jirafa","elefante"] = [6,7,"jirafa","elefante"] bad => [[6,7],"jirafa",elefante] coge la fila completa el c[2:]
# print("a[3:10] = ",a[3:10])# a[3:10] = [9,0,5,1,4,9,0] bad => [9,0] =>los indices 3 y 4 tienen valor pero 5 6 7 8 9 y 10 no tienen ningun valor
# print("a[3:10:2] = ",a[3:10:2])# a[3:10:2] = [9,5,4,0] bad => [9] => solo coge el indice 3 porque el siguiente indice seria 5 y ese no tiene valor
# print("d.index('jirafa') = ",d.index('jirafa'))# d.index('jirafa') = 2 good
# print("e[c[0][1]].count(5) = ",e[c[0][1]].count(5))# e[c[0][1]].count(5) = 0 bad => 2 => no sabia que el 2*a lo que hace es hacer el vector dos veces entonces c[0][1] seria => [5, 1, 4, 9, 0, 5, 1, 4, 9, 0] por lo cual cuenta 2
# print("sorted(a)[2] = ",sorted(a)[2]) # sorted(a)[2] = 4 good
# print("complex(b[0],b[1]) = ",complex(b[0],b[1])) # complex(b[0], b[1]) = complex(3,4) bad => lo pasa a complejo 3+4j => no me acordaba que los complejos era se denotaba con j

# # # Ejercicio 2 Desviación estándar
# # # Desarrolle una función llamada desviacion_estandar(valores) cuyo parámetro valores sea una lista de números reales.
# # # La función debe retornar la desviación estándar de los valores:
# # # Esto significa que hay que hacerlo siguiendo estos pasos:
# # # 1)calcular el promedio de los valores;
# # # 2)a cada valor hay que restarle el promedio, y el resultado elevarlo al cuadrado;
# # # 3)sumar todos los valores obtenidos;
# # # 4)dividir la suma por la cantidad de valores -1; 
# # # 5)sacar la raíz cuadrada del resultado.
# import math
# def desviacion_estandar(valores):
#     #calcular el promedio de los valores
#     promedio = 0
#     n = 0
#     for x in valores:
#         promedio += x
#         n += 1
#     promedio /= n
#     if n <= 1: # caso por si solo pone un numero o ninguno
#         return 0.0
#     # suma de cada valor al restarle el promedio y elevarlo al cuadrado
#     suma_total = 0.0
#     for x in valores:
#         suma_total += (x-promedio)**2
#     # dividir la suma por n-1 
#     fraccion = suma_total/(n-1)
#     #raiz de la fraccion
#     resultado = math.sqrt(fraccion)
#     return resultado

# print(desviacion_estandar([1.3,1.3,1.3]))
# print(desviacion_estandar([4.0, 1.0, 11.0, 13.0, 2.0, 7.0]))
# print(desviacion_estandar([1.5, 9.5]))
# print(desviacion_estandar([1]))

# # # Ejercicio 3 Mayores que el promedio
# # # Escriba un programa que pregunte al usuario cuántos datos ingresará, a continuación le pida que ingrese los datos uno por uno, y finalmente entregue como salida cuántos de los datos ingresados son mayores que el promedio.
# n = int(input("Cuantos datos ingresara? "))
# lista = []
# promedio = 0.0
# for i in range (1,n+1,1): #pedimos los numeros
#     x = float(input("Dato {}: ".format(i)))
#     lista.append(x)
#     promedio += x
# promedio /= n
# cnt = 0 # contador de elementos mayores al promedio
# for x in lista:
#     if x > promedio:
#         cnt += 1
# print("{} datos son mayores que el promedio".format(cnt))
# # # Ejercicio 4 iguales o distintos
# # # 1) Escriba la función todos_iguales(lista) que indique si todos los elementos de una lista son iguales:
# # # 2) A continuación, escriba una función todos_distintos(lista) que indique si todos los elementos de una lista son distintos:
# # # Sus funciones deben ser capaces de aceptar listas de cualquier tamaño y con cualquier tipo de datos:

# def todos_iguales(lista): 
#     primero = lista[0]#tomamos el primer valor
#     rta = True
#     for x in lista:
#         if primero != x: #si algun valor en la lista es distinto al primero todos no son iguales
#             rta = False
#             break
#     return rta

# def todos_distintos(lista):
#     lista.sort() # ordenamos la lista
#     n = len(lista)
#     rta = True
#     if n <= 1: # el caso de que solo haya 1 o menos digitos
#         return rta 
#     for i in range (0,n-1,1):
#         if lista[i] == lista[i+1]:#si encontramos algun elemento igual ya no todos son distintos
#             rta = False
#             break
#     return rta
# print(todos_iguales([6,6,6]))
# print(todos_iguales([6,6,1]))
# print(todos_iguales([0,90,1]))
# print(todos_distintos([6,6,6]))
# print(todos_distintos([6,6,1]))
# print(todos_distintos([0,90,1]))
# print(todos_iguales([7, 7, 7, 7, 7, 7, 7, 7, 7]))
# print(todos_distintos(list(range(1000))))
# print(todos_iguales([12]))
# print(todos_distintos(list('hiperblanduzcos')))

# # # Ejercicio 5 Estadisticos de localizacion
# # # 1)La media aritmética (o promedio) de un conjunto de datos es la suma de los valores dividida por la cantidad de datos.
# # # Escriba la función media_aritmetica(datos), donde datos es una lista de números, que entregue la media aritmética de los datos:
# # # 2)La media armónica de un conjunto de datos es el recíproco de la suma de los recíprocos de los datos, multiplicada por la cantidad de datos:
# # # Escriba la función media_armonica(datos), que entregue la media armónica de los datos:
# # # 3)La mediana de un conjunto de datos reales es el valor para el que el conjunto tiene tantos datos mayores como menores a él.

# # # Más rigurosamente, la mediana es definida de la siguiente manera:

# # # - si la cantidad de datos es impar, la mediana es el valor que queda en la mitad al ordenar los datos de menor a mayor;
# # # - si la cantidad de datos es par, la mediana es el promedio de los dos valores que quedan al centro al ordenar los datos de menor a mayor.

# # # Escriba la función mediana(datos), que entregue la mediana de los datos:
# # # La función no debe modificar la lista que recibe como argumento:
# # # 4)La moda de un conjunto de datos es el valor que más se repite.
# # # Escriba la función modas(datos), donde datos es una lista, que entregue una lista con las modas de los datos:
# # # Usando las funciones definidas anteriormente, escriba un programa que:

# # # - pregunte al usuario cuántos datos ingresará,
# # # - le pida que ingrese los datos uno por uno, y
# # # - muestre un reporte con las medias aritmética y armónica, la mediana y las modas de los datos ingresados.

# # # Si alguno de los datos es cero, el reporte no debe mostrar la media armónica.
# def media_aritmetica(lista):
#     n = len(lista) #cantidad de datos en la lista
#     suma_total = 0.0
#     for x in lista: #ciclo para sumar todos los datos de la lista
#         suma_total += x
#     return suma_total/n
# # print(media_aritmetica([6, 1, 4, 8]))
# def media_armonica(lista):
#     n = len(lista) #cantidad de datos en la lista
#     suma_reciprocos = 0.0
#     for x in lista: #ciclo para sumar los reciprocos de la lista
#         if x == 0:
#             return -1
#         suma_reciprocos += 1/x
#     return n/suma_reciprocos
# # print(media_armonica([6,1,4,8]))
# def mediana(lista):
#     n = len(lista)
#     lista2 = sorted(lista) #una segunda lista para no cambiar la primera lista
#     if n % 2 != 0:#si la cantidad de datos son impares
#         return lista2[int(n/2)] #el valor que queda en el centro
#     else: # si la cantidad de datos son pares
#         return (lista2[int(n/2)]+lista2[int(n/2)-1])/2 #promedio de los dos valores que quedan en el centro
    
# # print(mediana([5.0, 1.4, 3.2]))
# # print(mediana([5.0, 1.4, 3.2, 0.1]))
# # x = [5.0, 1.4, 3.2]
# # print(mediana(x))
# # print(x)

# def modas(lista):
#     max_value = max(lista)
#     contador_valores = []
#     for i in range(0,max_value+1,1): #creo una lista con solo ceros
#         contador_valores.append(0)
#     contador_maximo = 0
#     for x in lista: #busco cuanto es lo maximo que se repite un dato
#         contador_valores[x] += 1
#         if contador_valores[x] > contador_maximo:
#             contador_maximo = contador_valores[x]
#     rta = []   
#     for i in range(0,max_value+1,1):#creo la lista de los valores que mas se repiten
#         if contador_valores[i] == contador_maximo:
#             rta.append(i)
#     return rta

# # print(modas([5, 4, 1, 4, 3, 3, 4, 5, 0]))
# # print(modas([5, 4, 1, 4, 3, 3, 4, 5, 3]))
# # print(modas([5, 4, 5, 4, 3, 3, 4, 5, 3]))
# n = int(input("Ingrese la cantidad de datos de la lista: "))
# lista = []
# for i in range(0,n,1):
#     x = int(input("Ingrese el dato {}: ".format(i+1)))
#     lista.append(x)

# print("La media aritmetica es:",media_aritmetica(lista))
# value = media_armonica(lista)
# if value == -1:
#     print("Uno de los valores de la lista es cero, por lo cual no tiene media armonica")
# else:
#     print("La media armonica es:",value)
# print("La mediana es:",mediana(lista))
# print("las modas son:",modas(lista))
# # # Ejercicio 6 Mapear y filtrar
# # # 1)Escriba la función mapear(f, valores) cuyos parámetros sean una función f y una lista valores, y que retorne una nueva lista que tenga los elementos obtenidos al aplicar la función a los elementos de la lista:
# # # 2)Escriba la función filtrar(f, valores) cuyos parametros sean una función f que retorne un valor booleano y una lista valores, y que retorne una nueva lista que tenga todos los elementos de valores para los que la función f retorne True:
# def mapear(funcion,lista):
#     for index,x in enumerate(lista):
#         lista[index] = funcion(x)
#     return lista

# def filtrar(funcion,lista):
#     lista_final = []
#     for x in lista:
#         if(funcion(x)):
#             lista_final.append(x)
#     return lista_final

# def cuadrado(x):
#     return x**2

# def es_larga(palabra):
#     return len(palabra) > 4

# print(mapear(cuadrado,[5,2,9]))
# p = ['arroz', 'leon', 'oso', 'mochila']
# print(filtrar(es_larga,p))
# print(p)
# # # Ejercicio 7 Torneo de tenis
# # # Escriba un programa para simular un campeonato de tenis.
# # # Primero, debe pedir al usuario que ingrese los nombres de ocho tenistas. A continuación, debe pedir los resultados de los partidos juntando los jugadores de dos en dos. El ganador de cada partido avanza a la ronda siguiente.
# # # El programa debe continuar preguntando ganadores de partidos hasta que quede un único jugador, que es el campeón del torneo.
# # # El programa en ejecución debe verse así:
print("Ingrese el nombre de 8 tenistas:")
lista_jugadores = []
for i in range(1,9,1):
    jugador = input("Jugador {}: ".format(i))
    lista_jugadores.append(jugador)
i = 1
while(len(lista_jugadores)>1):
    print("Ronda {}".format(i))
    n = len(lista_jugadores)
    for i in range(0,int(n/2),1):
        ganador = input("A.{} - B.{}: ".format(lista_jugadores[i],lista_jugadores[i+1]))
        if ganador == 'A':
            lista_jugadores.remove(lista_jugadores[i+1])
        else:
            lista_jugadores.remove(lista_jugadores[i])
    
print("Campeon: {}".format(lista_jugadores[0]))