# # # Nivel principiante
# # # 1)Se requiere realizar un programa en Python que permita leer 3 números enteros positivos e imprima
# # # La sumatoria de los tres números.
# print("Ingrese 3 numeros enteros positivos: ")
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# print(a+b+c)
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
imc_estudiantes = [["1.",27,61,1.73],["2.",27,62,1.63],["3.",27,63,1.73],["4.",27,64,1.73],["5.",27,65,1.73],["6.",27,66,1.73],
                   ["7.",27,67,1.73],["8.",27,68,1.73],["9.",27,69,1.73],["10.",27,70,1.73],["11.",27,71,1.73],["12.",27,72,1.73],
                   ["13.",27,73,1.73],["14.",27,74,1.73],["15.",27,75,1.73],["16.",27,76,1.73],["17.",27,77,1.73],["18.",27,78,1.73],
                   ["19.",27,79,1.73],["20.",27,80,1.73]]
i = 0
for imc in imc_estudiantes:
    imc_estudiantes[i]=tuple(imc+[imc[2]/(imc[3]**2)])
    i += 1
obesidad_3 = 0
obesidad_2 = 0
obesidad_1 = 0
sobrepeso =  0
normal = 0
debajo_de_normal = 0

for imc in imc_estudiantes:
    if imc[4] > 40.0:
        obesidad_3 += 1
    elif imc[4] >= 35.0:
        obesidad_2 += 1
    elif imc[4] >= 30.0:
        obesidad_1 += 1
    elif imc[4] >= 25.0:
        sobrepeso += 1
    elif imc[4] >= 18.5:
        normal += 1
    else:
        debajo_de_normal += 1
print("La cantidad de estudiantes que se encuentra debajo del peso ideal son",debajo_de_normal)
print("La cantidad de estudiantes que se encuentra en peso ideal son",normal)
print("La cantidad de estudiantes que se encuentra en sobrepeso son",sobrepeso)
print("La cantidad de estudiantes que se encuentra en obesidad grado I son",obesidad_1)
print("La cantidad de estudiantes que se encuentra en obesidad grado II son",obesidad_2)
print("La cantidad de estudiantes que se encuentra en obesidad grado III son",obesidad_3)



