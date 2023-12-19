# # # Ejercicio 1 expresiones con listas
# # # Considere las siguientes listas:
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
n = int(input("Cuantos datos ingresara? "))
lista = []
promedio = 0.0
for i in range (1,n+1,1): #pedimos los numeros
    x = float(input("Dato {}: ".format(i)))
    lista.append(x)
    promedio += x
promedio /= n
cnt = 0 # contador de elementos mayores al promedio
for x in lista:
    if x > promedio:
        cnt += 1
print("{} datos son mayores que el promedio".format(cnt))
