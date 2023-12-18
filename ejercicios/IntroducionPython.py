import math
from datetime import date
###ejercicio 1 Saludo
###Escriba un programa que pida al usuario que escriba su nombre, y lo salude llamándolo por su nombre.
# nombre = input("Ingrese su nombre: ")
# print("Hola, ",nombre)
###Ejercicio 2 Circulos
###Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
# radio = int(input("Ingrese el radio: "))
# print("Perimetro: ", round(2*math.pi*radio,1))
# print("Area: ", round(math.pi*pow(radio,2),1))
# # # Ejercicio 3 Promedio
# # # Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
# nota1 = int(input("Primera nota: "))
# nota2 = int(input("Segunda nota: "))
# nota3 = int(input("Tercera nota: "))
# nota4 = int(input("Cuarta nota: "))
# print("El promedio es: ", (nota1+nota2+nota3+nota4)/4)
# # # Ejercicio 4 conversion de unidades de longitud
# # # Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.
# longitud = int(input("Ingrese longitud: "))
# print(longitud," cm = ",round(longitud/2.54,4)," in")
# # # Ejercicio 5 pitagoras
# # # Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: 
# a = int(input("Ingrese cateto a: "))
# b = int(input("Ingrese cateto b: "))
# h = math.sqrt(pow(a,2)+pow(b,2))
# print("La hipotenusa es ",h)
# # # Ejercicio 6 Hora futura
# # # Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:
# horaActual = int(input("Hora actual: "))
# cntHoras = int(input("Cantidad de horas: "))
# cnt = cntHoras
# while cntHoras > 0:
#     horaActual +=1
#     horaActual %= 24
#     cntHoras-=1
# print("En ",cnt, " horas, el reloj en hora militar marcara las ",horaActual, "AM"if horaActual <12 else "PM")
# # # Ejercicio 7
# # # Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.
# numero = input("Ingrese un numero: ")
# print(numero.rsplit(".")[-1])
# print("0.{}".format(numero.rsplit(".")[-1]))
# # # Ejercicio 8 que nota necesito
# # # Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.
# # # El promedio del ramo se calcula con la siguiente formula.
# # # nc = (c1+c2+c3)/3
# # # Donde NC es el promedio de certámenes, NL el promedio de laboratorio y NF la nota final
# # # Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.
# crt1 = int(input("Ingrese nota certamen 1: "))
# crt2 = int(input("Ingrese nota certamen 2: "))
# lab = int(input("Ingrese nota laboratorio: "))
# crt3 = int((3/0.7)*int(60-(lab*0.3)-(((crt1+crt2)/3)*0.7)))
# if crt3<0:
#     crt3 = 0
# print("Necesita nota", crt3,"en el certamen 3")
# # # Ejercicio 9 palabra mas larga
# # # Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.
# palabra1 = input("Palabra 1: ")
# palabra2 = input("Palabra 2: ")
# if len(palabra1) > len(palabra2):
#     print("La palabra",palabra1,"tiene",len(palabra1)-len(palabra2),"letras mas que",palabra2+".")
# elif len(palabra2) > len(palabra1):
#     print("La palabra",palabra2,"tiene",len(palabra2)-len(palabra1),"letras mas que",palabra1+".")
# else:
#     print("Las dos palabras tienen el mismo largo")
# # # Ejercicio 10 edad
# # # Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento
# # # Por supuesto, el resultado entregado depende del día en que su programa será ejecutado.
# # # El programa debe tener en cuenta si el cumpleaños ingresado ya pasó durante este año, o si todavía no ocurre.
dia = int(input("Dia: "))
mes = int(input("Mes: "))
año = int(input("Año: "))
hoy = str(date.today()).rsplit("-")
añoActual = int(hoy[0])
mesActual = int(hoy[1])
diaActual = int(hoy[2])
edad = añoActual-año
if mesActual < mes and diaActual < dia:
    edad -= 1
print("Usted tiene",edad,"años")