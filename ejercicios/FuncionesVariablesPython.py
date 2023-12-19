# # # Ejercicio 1 Digitos
# # # Escriba un programa que determine la cantidad de dígitos en un número entero ingresado por el usuario:
# numero = int(input("Ingrese un numero: "))#Lo ingresa como int para asegurar que sea un numero entero
# numero = str(numero) #Lo convertimos denuevo a string para poder usar len
# #Mostarmos el resultado
# if len(numero) > 1:
#     print(numero,"tiene",len(numero),"digitos")
# else:
#     print(numero,"tiene",len(numero),"digito")
# # # Ejercicio 2 Digito verificador
# # # Desarrolle un programa que calcule el dígito verificador de un rol UTFSM.
# # # Para calcular el dígito verificador, se deben realizar los siguiente pasos:
# # # 1.Obtener el rol sin guión ni dígito verificador.
# # # 2.Invertir el número. (e.g: de 201012341 a 143210102).
# # # 3.Multiplicar los dígitos por la secuencia 2, 3, 4, 5, 6, 7, si es que se acaban los números, se debe comenzar denuevo, por ejemplo, con 143210102:
# # # 4.Al resultado obtenido, es decir, 52, debemos sacarle el módulo 11, es decir:
# # # 5. Con el resultado obtenido en el paso anterior, debemos restarlo de 11:
# # # 6.Finalmente, el dígito verificador será el obtenido en la resta: 201012341-3.
# paso 1
# rol = input("Ingrese el rol sin guion ni digito verificador: ")
# # paso 2
# rol = rol[::-1]
# # paso 3
# suma = 0
# i = 2
# for c in rol:
#     # print(c+"x"+str(i)+"+")
#     suma += (int(c)*i)
#     i += 1
#     if i > 7:
#         i = 2
# # paso 4
# suma %= 11
# # paso 5
# digitoVerificador = 11 - suma
# #paso 6
# rol = rol[::-1]
# print(rol+"-"+str(digitoVerificador))   
# # # Ejercicio 3 Numeros palindromos
# # # 1)Escriba la función invertir_digitos(n) que reciba un número entero n y entregue como resultado el número n con los dígitos en el orden inverso:
# # # 2)A continuación, escriba un programa que indique si el número ingresado es palíndromo o no, usando la función invertir_digitos:
# def invertir_digitos(numero):#debe ingresar el numero como un string
#     return numero[::-1]
# n = int(input("Ingrese n: "))
# n = str(n)
# n2 = invertir_digitos(n) # crea el numero invertido
# rta = True 
# for i in range(0,len(n),1): # comprobamos si los digitos en determinada posicion son iguales
#     # n = "12" i=0 "1"
#     # n2 = "21"    "2"
#     if n[i] != n2[i]:
#         rta = False
#         break
# if rta: 
#     print ("Es palindromo")
# else:
#     print("No es palindromo")
# # # Ejercicio 4 Alzas del dolar
# # # Un analista financiero lleva un registro del precio del dólar día a día, y desea saber cuál fue la mayor de las alzas en el precio diario a lo largo de ese período.
# # # Escriba un programa que pida al usuario ingresar el número n de días, y luego el precio del dólar para cada uno de los n días.
# # # El programa debe entregar como salida cuál fue la mayor de las alzas de un día para el otro.
# # # Si en ningún día el precio subió, la salida debe decir: No hubo alzas.
# def buscando_Alza():
#     alza = 0.0
#     anterior = 0.0
#     for i in range(1,n+1,1): # pido el valor del alza cada dia
#         x = float(input("Dia {:2}: ".format(i)))
#         if i != 1:
#             if x-anterior > alza: #buscamos el alza mayor
#                 alza = x-anterior
#         anterior = x
#     return alza
# n = int(input("Cuantos dias? "))

# alza = buscando_Alza()
# if alza == 0.0:
#     print("No hubo alzas.")
# else:
#     print("La mayor alza fue de {:.2f} pesos".format(alza))
# # # Ejercicio 5 Maquina de alimentos
# # # Una máquina de alimentos tiene productos de tres tipos A,B y C que valen respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10, $50 y $100.
# # # Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio del producto, el programa debe entregar las monedas de vuelto, una por una.

# def elegir_producto():
#     producto = ""
#     print("La maquina tiene los productos A, B y C")
#     while(producto.upper() != "A" and producto.upper() != "B" and producto.upper() != "C"):
#         producto = input("Elija producto: ")
#     return producto.upper()
# def monedas(producto):
#     precio = 0
#     if producto == "A":
#         precio = 270
#     elif producto == "B":
#         precio = 340
#     else:
#         precio = 390
#     print("Solo se aceptan monedas de $100, $50 o $10")
#     print("Ingrese monedas: ")
#     ingresado = 0
#     while ingresado < precio: #pedimos el dinero
#         x = int(input())
#         if x != 100 and x != 50 and x != 10:
#             print("Moneda no valida")
#         else:
#             ingresado += x
            
#     print("Su vuelto: ")
#     while(ingresado > precio):
#         diferencia = ingresado - precio
#         if diferencia >= 100:
#             print(100)
#             ingresado -= 100
#         elif diferencia >= 50:
#             print(50)
#             ingresado -= 50
#         else:
#             print(10)
#             ingresado -= 10

# producto = elegir_producto() #el usuario selecciona su producto
# monedas(producto)#Se le pide el dinero y se le da su cambio de ser necesario
# # # Ejercicio 6 promocion con descuento
# # # El supermercado Pitón Market ha lanzado una promoción para todos sus clientes que posean la tarjeta Raw Input. La promoción consiste en aplicar un descuento por cada n productos que pasan por caja.
# # # El primer descuento es de 20%, y se aplica sobre los primeros  n  productos ingresados. Luego, cada descuento es la mitad del anterior, y es aplicado sobre los siguientes  n  productos.
# # # Por ejemplo, si  n  = 3 y la compra es de 11 productos, entonces los tres primeros tienen 20% de descuento, los tres siguientes 10%, los tres siguientes 5%, y los dos últimos no tienen descuento.
# # # Escriba un programa que pida al usuario ingresar  n  y la cantidad de productos, y luego los precios de cada producto. Al final, el programa debe entregar el precio total, el descuento total y el precio final después de aplicar el descuento.
# # # Si al aplicar el descuento el precio queda con decimales, redondee el valor hacia abajo.
n =int(input("n: ")) # productos necesarios para el descuento 
cntProductos = int(input("Cantidad productos: "))
total = 0
actual = 0
descuento = 0
porcentaje = 0.2
for i in range(1,cntProductos+1,1):
    x = int(input("Precio producto {}: ".format(i)))
    actual += x
    if i % n == 0:
        total += actual
        descuento += actual*porcentaje
        porcentaje /= 2
        actual = 0
total += actual
descuento = int(descuento)
print("Total: {}".format(total))
print("Descuento: {}".format(descuento))
print("Por pagar: {}".format(total-descuento))
