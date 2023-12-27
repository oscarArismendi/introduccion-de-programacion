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
# a = (2, 10, 1991)
# b = (25, 12, 1990)
# c = ('Donald', True, b)
# x, y = ((27, 3), 9) 
# z, w = x
# v = (x, a)
# # # # Sin usar el computador, indique cuál es el resultado y el tipo de las siguientes expresiones. A continuación, verifique sus respuestas en el computador.
# print("a<b:",a<b) #True-good
# print("y+w:",y+w)#12-god
# print("x+a:",x+a)# (27,3,2,10,1991)-good
# print("len(v):",len(v))#2-good
# print("v[1][1]:",v[1][1])#10-good
# print("c[0][0]:",c[0][0])#'D'-good
# print("z,y:",z,y)# 27 9-good
# print("a+b[1:5]:",a+b[1:5])# (10,1991,25,12)-bad es (2,10,1991,12,1990)- esta mal porque no me di cuenta que b[1:5] = (12,1990) esa era la primera operacion no la suma
# print("(a+b)[1:5]:",(a+b)[1:5])# (10,1991,25,12)-good
# print("str(a[2])+str(b[2]):",str(a[2])+str(b[2]))# "19911990"-good sin comillas
# print("str(a[2]+b[2]):",str(a[2]+b[2]))#"3981"-good sin comillas
# print("str((a+b)[2]):",str((a+b)[2]))#"1991"-good sin comillas
# print("str(a+b)[2]:",str(a+b)[2])#"1"-bad es ,- estaba mal porque no me di cuenta que cuando conviertes una tupla en string es con todo parentesis y comas

# # # Ejercicio 3 supermercado
# # # Un supermercado utiliza tablas de datos para llevar la información de su inventario.
# # # En un programa, cada tabla de datos es una lista de tuplas.
# # # La lista productos tiene el código, el nombre, el precio y la cantidad de unidades del producto en bodega:

# productos = [
#     (41419, 'Fideos',        450, 210),
#     (70717, 'Cuaderno',      900, 119),
#     (78714, 'Jabon',         730, 708),
#     (30877, 'Desodorante',  2190,  79),
#     (47470, 'Yogur',          99, 832),
#     (50809, 'Palta',         500,  55),
#     (75466, 'Galletas',      235,   0),
#     (33692, 'Bebida',        700,  20),
#     (89148, 'Arroz',         900, 121),
#     (66194, 'Lapiz',         120, 900),
#     (15982, 'Vuvuzela',    12990,  40),
#     (41235, 'Chocolate',    3099,  48),
# ]

# # # La lista clientes tiene el rut y el nombre de los clientes del supermercado:

# clientes = [
#     ('11652624-7', 'Perico Los Palotes'),
#     ( '8830268-0', 'Leonardo Farkas'),
#     ( '7547896-8', 'Fulanita de Tal'),
# ]

# # # La lista ventas contiene las ventas realizadas, representadas por el número de boleta, la fecha de la venta y el rut del cliente:

# ventas = [
#     (1, (2010,  9, 12),  '8830268-0'),
#     (2, (2010,  9, 19), '11652624-7'),
#     (3, (2010,  9, 30),  '7547896-8'),
#     (4, (2010, 10,  1),  '8830268-0'),
#     (5, (2010, 10, 13),  '7547896-8'),
#     (6, (2010, 11, 11), '11652624-7'),
# ]

# # # El detalle de cada venta se encuentra en la lista itemes. Cada ítem tiene asociado un número de boleta, un código de producto y una cantidad:

# itemes = [
#     (1, 89148,  3),
#     (2, 50809,  4),
#     (2, 33692,  2),
#     (2, 47470,  6),
#     (3, 30877,  1),
#     (4, 89148,  1),
#     (4, 75466,  2),
#     (5, 89148,  2),
#     (5, 47470, 10),
#     (6, 41419,  2),
# ]

# # # Por ejemplo, en la venta con boleta número 2, fueron vendidas 4 paltas, 2 bebidas y 6 yogures.
# # # Escriba las siguienes funciones:

# # # >>> producto_mas_caro(productos)
# # # 'Vuvuzela'
# # # para la funcion productos_mas_caros quiero que reciba la lista productos:
# # #     1)Hacer dos variables llamadas precio_mayor y nombre_producto_mayor para saber que voy a imprimir
# # #     2)Hacer un ciclo que pase por toda la lista de productos
# # #     3)Ir comprobando si el precio del producto por el que paso es mayor a precio_mayor y si es asi cambiar precio_mayor a ese precio
# # #     y cambiar nombre_producto_mayor al producto que se esta leyendo en ese momemeto
# # #     4)Al salir del ciclo Imprimir nombre_producto_mayor
# def productos_mas_caros(productos):
#     precio_mayor = 0
#     nombre_producto_mayor = ""
#     for producto in productos:#el código en 0, el nombre en  1, el precio en 2 y la cantidad de unidades del producto en 3
#         if producto[2] > precio_mayor:
#             precio_mayor = producto[2]
#             nombre_producto_mayor = producto[1]
#     print(nombre_producto_mayor)

# productos_mas_caros(productos)
# # # >>> valor_total_bodega(productos)
# # # 1900570
# # # para la funcion valor_total_bodega(productos):
# # #     1)hacer una variable llamada suma_total
# # #     2)Hacer un ciclo que pase por la lista productos
# # #     3)A suma_total sumarrle el precio del producto por la cantidad que tenga
# # #     4)Al salir del ciclo imprimir suma_total
# def valor_total_bodega(productos):
#     suma_total = 0
#     for producto in productos:#el código en 0, el nombre en  1, el precio en 2 y la cantidad de unidades del producto en 3
#         suma_total += (producto[2]*producto[3])
#     print(suma_total)
# valor_total_bodega(productos)
# # # >>> ingreso_total_por_ventas(itemes, productos)
# # # 13944
# # # para la funcion ingreso_total_por_ventas(itemes,productos):
# # #     1) crear una variable suma_total
# # #     2) Hacer un ciclo que pase por la lista itemes
# # #     3) En el ciclo hacer una variable que sea precio_producto 
# # #     4) hacer otro ciclo que pase por la lista productos buscando uno que sea igual al codigo del itemes
# # #     5) Cuando se encuentre la condicion de arriba darle el valor a precio_producto del producto que se encontro y salir del ciclo
# # #     6) Sumarle a suma_total el precio_producto multiplicada por el numero de itemes que comprobando
# # #     7) Al salir del ciclo imprimir suma_total
# def ingreso_total_por_ventas(itemes,productos):
#     suma_total = 0
#     for item in itemes:# número de boleta de venta en 0, un código de producto en 1 y la cantidad vendida en el 2
#         precio_producto = 0
#         for producto in productos:#el código en 0, el nombre en  1, el precio en 2 y la cantidad de unidades del producto en 3
#             if producto[0] == item[1]:
#                 precio_producto = producto[2]
#                 break#para salir del ciclo for
#         suma_total += (precio_producto*item[2])
#     print(suma_total)

# ingreso_total_por_ventas(itemes,productos)    
# # # >>> producto_con_mas_ingresos(itemes, productos)
# # # 'Arroz'
# # # para la funcion producto_con_mas_ingresos(itemes, productos):
# # #     1) Hacer el diccionario ingresos_totales_producto el cual con el codigo del producto dira cuanto se gano con ese producto y como se llama en 
# # #     una tupla
# # #     2) inicializar todos los codigos en el diccionario con (0,"") el primero es la ganancia el segundo el nombre
# # #     3) Hacer un ciclo que pase por la lista de item
# # #     4) Ir sumandole al diccionario con el codigo del item el numero de items vendidos en la primera variable de la tupla
# # #     5) Al terminar hacer una variable llamada ganancia_mayor y nombre_producto_mayor
# # #     6) Hacer un ciclo que pase por todo el diccionario
# # #     7) En el ciclo hacer otro que pase por los productos
# # #     8) El que producto que consida en  el codigo entra en un if que el precio multiplicara el primer valor de la tupla y pondra el nombre del 
# # #     producto en el segundo valor de la tupla
# # #     9) Si el precio en le primer valor de la tupla es mayor a ganancia_mayor darle ese valor a ganancia_mayor y guardar el nombre del producto en
# # #     nombre_producto_mayor
# # #     10) Al terminar el ciclo print(nombre_producto_mayor)
# def producto_con_mas_ingresos(itemes, productos):
#     ingresos_totales_producto = {}
#     for producto in productos:#el código en 0, el nombre en  1, el precio en 2 y la cantidad de unidades del producto en 3
#         ingresos_totales_producto[producto[0]] = (0,producto[1])
    
#     for item in itemes:# número de boleta de venta en 0, un código de producto en 1 y la cantidad vendida en el 2
#         ingresos_totales_producto[item[1]] = (ingresos_totales_producto[item[1]][0]+item[2],ingresos_totales_producto[item[1]][1])
    
#     ganancia_mayor = 0
#     nombre_producto_mayor = ""
#     for producto in productos:#el código en 0, el nombre en  1, el precio en 2 y la cantidad de unidades del producto en 3
#         ingresos_totales_producto[producto[0]] = (ingresos_totales_producto[producto[0]][0]*producto[2],ingresos_totales_producto[producto[0]][1])
#         if ingresos_totales_producto[producto[0]][0] > ganancia_mayor:
#             ganancia_mayor = ingresos_totales_producto[producto[0]][0]
#             nombre_producto_mayor = ingresos_totales_producto[producto[0]][1] 

#     print(nombre_producto_mayor)
# producto_con_mas_ingresos(itemes, productos)    

# # # >>> cliente_que_mas_pago(itemes, productos, clientes)
# # # 'Fulanita de Tal'
# # # pensamientos para la funcion cliente_que_mas_pago(itemes, productos, clientes):
# # #     1)Hacer un diccionario llamado compra_total_cliente el cual la llave sera el codigo del cliente y el valor es cuanto compro 
# # #     2)Para inicializar compra_total_cliente toca hacer un ciclo que pase por clientes
# # #     3)Despues de hacer ese ciclo hacer un ciclo que pase por ventas(pienso que se debio poner)
# # #     4)hacer un ciclo que pase por items 
# # #     5) cuando el tickete del item sea igual al tickete de ventas hacer otro ciclo que pase por productos
# # #     6) cuando en productos se encuentre el que tenga el mismo codigo del de item entonces sumarle a al rut del cliente la compra_total_cliente
# # #     7)Al salir del todo hacer una varia que diga precio_mayor y otra que diga nombre_precio_mayor
# # #     8) hacer un ciclo que pase por el diccionario compra_total_cliente y vaya modificando precio_mayor y nombre_precio_mayor
# # #     9)Al salir del ciclo imprimir nombre_precio_mayor
# def cliente_que_mas_pago(itemes, productos, clientes):
#     compra_total_cliente = {}
#     for cliente in clientes:#tiene el rut en 0 y el nombre de los clientes en 1
#         compra_total_cliente[cliente[0]] = 0
    
#     for venta in ventas:#representadas por el número de boleta en 0, la fecha de la venta en 1 y el rut del cliente en 2
#         for item in itemes:# número de boleta de venta en 0, un código de producto en 1 y la cantidad vendida en el 2
#             if item[0] == venta[0]:
#                 for producto in productos:#el código en 0, el nombre en  1, el precio en 2 y la cantidad de unidades del producto en 3
#                     if producto[0] == item[1]:
#                         compra_total_cliente[venta[2]] += (producto[2]*item[2])
                    
#     precio_mayor = 0
#     nombre_precio_mayor = ""
#     for cliente in clientes:#tiene el rut en 0 y el nombre de los clientes en 1
#         if compra_total_cliente[cliente[0]] > precio_mayor:
#             precio_mayor = compra_total_cliente[cliente[0]]
#             nombre_precio_mayor = cliente[1]
#     print(nombre_precio_mayor)                    

# cliente_que_mas_pago(itemes,productos,clientes)

# # # >>> total_ventas_del_mes(2010, 10, itemes, productos)
# # # 4160
# # # pensamientos para hacer la funcion total_ventas_del_mes(año, mes, itemes, productos):
# # #     1)Hacer una variable que sea suma_total
# # #     2)Hacer un ciclo que pase por ventas(pienso que se debio añadir en la funcion la lista ventas)
# # #     3)Hacer un if que cuando el ciclo pase por una venta con el mismo año y mes haga otro ciclo que pase por itemes
# # #     4)En el ciclo de items cuando el ticket sea igual al ticket de ventas hacer un ciclo que pase por productos
# # #     5)En el ciclo de productos cuando el codigo sea igual que el codigo del item actual hacer una multiplicacion entre la cantidad del item y el valor del producto 
# # #     y sumarla a suma_total
# # #     6)Al terminar todos los ciclos imprimir suma_total
# def total_ventas_del_mes(año, mes, itemes, productos):
#     suma_total = 0
#     for venta in ventas:#representadas por el número de boleta en 0, la fecha de la venta en 1(0 el año,1 el mes, 2 el dia) y el rut del cliente en 2
#         if venta[1][0] == año and venta[1][1] == mes:
#             for item in itemes:# número de boleta de venta en 0, un código de producto en 1 y la cantidad vendida en el 2
#                 if item[0] == venta[0]:
#                     for producto in productos:#el código en 0, el nombre en  1, el precio en 2 y la cantidad de unidades del producto en 3
#                         if producto[0] == item[1]:
#                             suma_total += (item[2]*producto[2])
    
#     print(suma_total)

# total_ventas_del_mes(2010, 10, itemes, productos)
# # # >>> fecha_ultima_venta_producto(47470, itemes, ventas)
# # # (2010, 10, 13)
# # # pensamientos para hacer la funcion fecha_ultima_venta_producto(codigo_producto, itemes, ventas):
# # #     1) hacer una lista llamada ventas_producto en la cual se van a añadir todas las fechas en que se vendio el producto 
# # #     2)Hacer un ciclo que pase por itemes
# # #     3)Hacer en el ciclo un if que cuando sea igual codigo_producto al codigo del item hacer un ciclo que pase por ventas
# # #     4)Hacer un if en el ultimo ciclo que cuando el ticket de item sea igual al ticket de venta añada a la  lista ventas_producto la tupla de la fecha
# # #     5)Al salir de todos los ciclos imprimir el ultimo dato de la lista ventas_producto
# def fecha_ultima_venta_producto(codigo_producto, itemes, ventas):
#     ventas_producto = []
#     for item in itemes:# número de boleta de venta en 0, un código de producto en 1 y la cantidad vendida en el 2
#         if codigo_producto == item[1]:
#             for venta in ventas:#representadas por el número de boleta en 0, la fecha de la venta en 1(0 el año,1 el mes, 2 el dia) y el rut del cliente en 2
#                 if venta[0] == item[0]:
#                     ventas_producto.append(venta[1])
    
#     print(ventas_producto[-1])

# fecha_ultima_venta_producto(47470, itemes, ventas)

# # # Ejercicio 4 fechas
# # # Una fecha puede ser representada como una tupla (año, mes, dia).
# # # 1. Escriba la función dia_siguiente(f) que reciba como parámetro una fecha f y entegue cuál es la fecha siguiente:
# # #     >>> dia_siguiente((2011, 4, 11))
# # #     (2011, 4, 12)
# # #     >>> dia_siguiente((2011, 4, 30))
# # #     (2011, 5, 1)
# # #     >>> dia_siguiente((2011, 12, 31))
# # #     (2012, 1, 1)
# # # Como recomendación, dentro de su función use una lista con la cantidad de días que tiene cada mes:

# def dia_siguiente(año,mes,dia):
        
#     dias_mes = [31, 28, 31, 30,
#                 31, 30, 31, 31,
#                 30, 31, 30, 31]
#     dia += 1
#     if dia > dias_mes[mes-1]:
#         dia = 1
#         mes += 1
#         if mes > 12:
#             mes = 1
#             año += 1
#     print((año,mes,dia))

# dia_siguiente(*(2011, 4, 11))#el * desempaqueta la tupla en tres valores
# dia_siguiente(*(2011, 4, 30))
# dia_siguiente(*(2011, 12, 31))

# # # 2. Escriba la función dias_entre(f1, f2) que retorne la cantidad de días que han transcurrido entre las fechas f1 y f2:
# # #     >>> hoy = (2011, 4, 11)
# # #     >>> navidad = (2011, 12, 25)
# # #     >>> dias_entre(hoy, navidad)
# # #     258
# # #     >>> dias_entre(hoy, hoy)
# # #     0
# # # pensamientos para la funcion dias_entre(f1, f2):
# # #     1) asegurarse que f1 sea la fecha menor si no intercambiar
# # #     2) Hacer un while que le siga sumando a f1 hasta que sea igual a f2
# # #     3) dentro del while llevar un contador de cuantos ciclos se hiciero
# # #     4) Imprimir el contador 
# def dias_entre(f1, f2):#0 año, 1 mes y 2 dia
#     if f1[0] > f2[0]:
#         f1,f2 = f2,f1 #intercambiando los valores de las tuplas
#     elif f1[0] == f2[0] and f1[1] > f2[1]:
#         f1,f2 = f2,f1 #intercambiando los valores de las tuplas
#     elif f1[0] == f2[0] and f1[1] == f2[1] and f1[2] > f2[2]:
#         f1,f2 = f2,f1 #intercambiando los valores de las tuplas
#     dias_mes = [31, 28, 31, 30,
#                 31, 30, 31, 31,
#                 30, 31, 30, 31]
#     contador_dias = 0
#     while(f1 != f2):
#         contador_dias += 1
#         f1 = (f1[0],f1[1],f1[2]+1)
#         if f1[2] > dias_mes[f1[1]-1]:
#             f1 = (f1[0],f1[1],1)
#             f1 = (f1[0],f1[1]+1,f1[2])
#             if f1[1] > 12:
#                 f1[1] = (f1[0],1,f1[2])
#                 f1[0] = (f1[0]+1,f1[1],f1[2])
    
#     print(contador_dias)
# hoy = (2011, 4, 11)
# navidad = (2011, 12, 25)
# dias_entre(hoy, navidad)
# dias_entre(hoy, hoy)
# # # 3. Escriba un programa que le diga al usuario cuántos días de edad tiene:
# # #     Ingrese su fecha de nacimiento.
# # #     Dia: 14
# # #     Mes: 5
# # #     Anno: 1990
# # #     Ingrese la fecha de hoy.
# # #     Dia: 20
# # #     Mes: 4
# # #     Anno: 2011
# # #     Usted tiene 7646 dias de edad
# # # pensamientos para el programa:
# # #     1) Recibir las 6 variables
# # #     2) hacer un contador_dias que cuente cuante los dias que se necesitaron para que fueran iguales
# # #     3) Hacer un ciclo while que no se detenga hasta que la fecha de nacimiento sea igual que la fecha de hoy
# # #     4) Ir sumano de uno en uno hasta que sean iguales
# # #     5) imprimir contador_dias
# print("Ingrese su fecha de nacimiento.")
# dia_nacimiento = int(input("Dia: "))
# mes_nacimiento = int(input("Mes: "))
# año_nacimiento = int(input("Año: "))
# print("Ingrese la fecha de hoy.")
# dia_actual = int(input("Dia: "))
# mes_actual = int(input("Mes: "))
# año_actual = int(input("Año: "))

# contador_dias = 0
# dias_mes = [31, 28, 31, 30,
#             31, 30, 31, 31,
#             30, 31, 30, 31]
# while(año_nacimiento != año_actual or mes_nacimiento != mes_actual or dia_nacimiento != dia_actual):
#     contador_dias += 1    
#     dia_nacimiento += 1
#     if dia_nacimiento > dias_mes[mes_nacimiento-1]:
#         dia_nacimiento = 1
#         mes_nacimiento += 1
#         if mes_nacimiento > 12:
#             mes_nacimiento = 1
#             año_nacimiento += 1

# print("Usted tiene {} de edad".format(contador_dias))
# # # Ejercicio 5 Expresiones con conjuntos
# # # Considere las siguientes asignaciones:
a = {5, 2, 3, 9, 4}
b = {3, 1}
c = {7, 5, 5, 1, 8, 6}
d = [6, 2, 4, 5, 5, 3, 1, 3, 7, 8]
e = {(2, 3), (3, 4), (4, 5)}
f = [{2, 3}, {3, 4}, {4, 5}]
# # # Sin usar el computador, indique cuál es el resultado y el tipo de las siguientes expresiones. A continuación, verifique sus respuestas en el computador.
#set en python no estan garantizados a estar ordenos por lo cual si se necesitan ordenarlos es mejor hacerlo de antemano
print("len(c) =",len(c)) # 6-bad porque lo esta definiendo como set entonces c termina siendo {7,5,1,8,6}->y puede que lo ordene{1,5,6,7,8}
print("len(set(d)) =",len(set(d))) #8-good
print("a & (b | c)  =",a & (b | c))#{2}-bad porque b|c es {1,3,5,6,7,8} & a es -> {3,5}
print("(a & b) | c =",(a & b) | c)#{3,7,5,5,1,8,6}-bad no los quite repetidos es-> y puede que lo ordene {1,3,5,6,7,8}
print("c - a =",c - a)#{7,5,1,8,6}-bad porque solo habia un 5 en c por eso cuando se resta se quita-> {8,1,6,7}
print("max(e) =",max(e))#(4,5)-good comprueba primero el primer mayor valor y en caso de empate comprueba el segundo
print("f[0] < a =",f[0] < a)#True-good porque tiene menos elementos
print("set(range(4)) & a =",set(range(4)) & a)#{2,3,4}-bad porque los valores de range son 0,1,2,3 empieza desde cero->{2,3}
print("(set(range(4)) & a) in f =",(set(range(4)) & a) in f)#{}-bad porque la primera parte daba {2,3} y eso si estaba en f rta = True
print("len(set('perro')) =",len(set('perro')))#4-good
print("len({'perro'}) =",len({'perro'}))#1-good porque es solo un elemento en el set
