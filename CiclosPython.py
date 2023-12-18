# # # Ejercicio 1 Numero Invertido
# # # Escriba un programa que pida al usuario un entero de n dígitos, y entregue el número con los dígitos en orden inverso:
# numero = input("Ingrese numero: ")[::-1]
# print(numero)
# # # Ejercicio 2 Tiempo de viaje
# # # n viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.
# # # Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
# # # El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
# tramo = -1
# sumaTotal = 0
# while tramo != 0:
#     tramo = int(input("Duracion tramo: "))
#     sumaTotal += tramo
# print("Tiempo total de viaje:",str(int(sumaTotal/60))+":"+str(sumaTotal%60),"horas")
# # # Ejercicio 3 Dibujos de asteriscos
# # # 1)Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:
# altura = int(input("Altura: "))
# ancho = int(input("Ancho: "))
# for i in range(0,altura,1):
#     for j in range(0,ancho,1):
#         print("*",end="")
#     print("")
# # # 2)Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:
# altura = int(input("Altura: "))
# for i in range(0,altura,1):
#     for j in range(0,i+1,1):
#         print("*",end="")
#     print("")
# # # 3)Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de aclerdo al ejemplo:
# lado = int(input("Lado: "))

# act = lado
# mx = lado + (2*(lado-1))
# for i in range(0,(lado*2)-1,1):
#     x = int((mx-act)/2)
#     print(" "*x,end="")
#     print("*"*act)
#     if i < (lado-1):
#         act += 2
#     else:
#         act -= 2
# # # Ejercicio 4 Generar PI
# # # La entrada del programa debe ser un número entero n� que indique cuántos términos de la suma se utilizará.
# # # 4(1-1/3+1/5+1/7+....)
# # # La entrada del programa debe ser un número entero n� que indique cuántos términos de la suma se utilizará.
# n = int(input("n: "))
# x = float(0.0)
# for i in range(0,n,1):
#     if i%2 == 0:
#         x += float(1/(1+(2*i)))
#     else:
#       x -= float(1/(1+(2*i)))  
# print(4.0*x)
# # # Ejercicio 5 Suma de fracciones
# # # Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:
# # # en forma decimal:
# # # El programa debe mostrar tres columnas que contengan la siguiente información:
# print(f"{'Potencia':<20} {'Fraccion':<20} {'Suma':<20}")
# x = 0.5
# i = 1
# suma = 0.0
# while x > 0.000001:
#     suma += x
#     print(f"{i:<20} {x:<20} {suma:<20}")
#     x *= 0.5
#     i += 1
# # # Ejercicio 6 Contar combinaciones de dado
# # # Un jugador debe lanzar dos dados numerados de 1 a 6, y su puntaje es la suma de los valores obtenidos.
# # # Un puntaje dado puede ser obtenido con varias combinaciones posibles. Por ejemplo, el puntaje 4 se logra con las siguientes tres combinaciones: 1+3, 2+2 y 3+1.
# # # Escriba un programa que pregunte al usuario un puntaje, y muestre como resultado la cantidad de combinaciones de dados con las que se puede obtener ese puntaje.