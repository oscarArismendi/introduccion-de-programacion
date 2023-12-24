# # # Ejercicio 1 registro de ventas y productos unicos
# # # Imagina que trabajas en una tienda y te han proporcionado un registro de ventas. Tu tarea es procesar esta información para obtener algunas métricas útiles utilizando tuplas y conjuntos en Python.
# # # Registro de Ventas:
# # # ventas = [
# # #     ("ProductoA", 10, 150),
# # #     ("ProductoB", 5, 200),
# # #     ("ProductoA", 8, 120),
# # #     ("ProductoC", 12, 80),
# # #     ("ProductoB", 3, 210),
# # #     ("ProductoA", 15, 130),
# # #     ("ProductoC", 7, 85),
# # # ]
# # # 1. Calcular Total de Ventas por Producto:
# # # Crea un diccionario que contenga el total de ventas para cada producto. Utiliza tuplas para representar la información de cada venta.
# # # 2. Encontrar Productos con Más de 10 Ventas:
# # # Crea un conjunto que contenga los nombres de los productos que han tenido más de 10 ventas.
# # # 3. Calcular Ganancia Total:
# # # Calcula la ganancia total sumando el precio total de cada venta.
# # # pensamientos:
# # # 1.hacer un diccionario{key:value} que la llave sea el nombre del producto y que el valor sea una lista con el valor de las ventas totales del producto y las tuplas de cada venta sin el nombre del producto
# # # 2.hacer un for que pase por informacion producto y si pasa de 10 poner el producto en el conjunto_ventas_10{}
# # # 3. aprovechar el for anterior para crear una variable sumando el precio total de ccada venta para encontrar la ganancia total
# ventas = [
#     ("ProductoA", 10, 150),
#     ("ProductoB", 5, 200),
#     ("ProductoA", 8, 120),
#     ("ProductoC", 12, 80),
#     ("ProductoB", 3, 210),
#     ("ProductoA", 15, 130),
#     ("ProductoC", 7, 85),
# ]
# informacion_productos = {}#diccionario
# ganancia_a = 0
# ganancia_b = 0
# ganancia_c = 0

# for producto in ventas:
#     if producto[0] == "ProductoA":
#         if informacion_productos.get("ProductoA") == None:
#             informacion_productos["ProductoA"] = [producto[1],producto[1:]]
#         else:
#             informacion_productos["ProductoA"][0] += producto[1]
#             informacion_productos["ProductoA"].append(producto[1:])
#         ganancia_a += producto[2]
#     elif producto[0] == "ProductoB":
#         if informacion_productos.get("ProductoB") == None:
#             informacion_productos["ProductoB"] = [producto[1],producto[1:]]
#         else:
#             informacion_productos["ProductoB"][0] += producto[1]
#             informacion_productos["ProductoB"].append(producto[1:])
#         ganancia_b += producto[2]

#     else:
#         if informacion_productos.get("ProductoC") == None:
#             informacion_productos["ProductoC"] = [producto[1],producto[1:]]
#         else:
#             informacion_productos["ProductoC"][0] += producto[1]
#             informacion_productos["ProductoC"].append(producto[1:])
#         ganancia_c += producto[2]

# print(informacion_productos)#primera respuesta
# conjunto_ventas_10 = set()#conjunto
# llaves = ["ProductoA","ProductoB","ProductoC"]#llaves para hacer el for
# for valores in llaves:
#     if informacion_productos[valores][0] > 10:
#         conjunto_ventas_10.add(valores)

# print(conjunto_ventas_10)#segunda respuesta
# ganancia_total = ganancia_c + ganancia_a + ganancia_b
# print(ganancia_total)#tercera respuesta 

# # # Ejercicio 2 Expresiones con tuplas
# # # Considere las siguientes asignaciones:
a = (2, 10, 1991)
b = (25, 12, 1990)
c = ('Donald', True, b)
x, y = ((27, 3), 9) 
z, w = x
v = (x, a)
# # # Sin usar el computador, indique cuál es el resultado y el tipo de las siguientes expresiones. A continuación, verifique sus respuestas en el computador.
print("a<b:",a<b) #True-good
print("y+w:",y+w)#12-god
print("x+a:",x+a)# (27,3,2,10,1991)-good
print("len(v):",len(v))#2-good
print("v[1][1]:",v[1][1])#10-good
print("c[0][0]:",c[0][0])#'D'-good
print("z,y:",z,y)# 27 9-good
print("a+b[1:5]:",a+b[1:5])# (10,1991,25,12)-bad es (2,10,1991,12,1990)- esta mal porque no me di cuenta que b[1:5] = (12,1990) esa era la primera operacion no la suma
print("(a+b)[1:5]:",(a+b)[1:5])# (10,1991,25,12)-good
print("str(a[2])+str(b[2]):",str(a[2])+str(b[2]))# "19911990"-good sin comillas
print("str(a[2]+b[2]):",str(a[2]+b[2]))#"3981"-good sin comillas
print("str((a+b)[2]):",str((a+b)[2]))#"1991"-good sin comillas
print("str(a+b)[2]:",str(a+b)[2])#"1"-bad es ,- estaba mal porque no me di cuenta que cuando conviertes una tupla en string es con todo parentesis y comas
