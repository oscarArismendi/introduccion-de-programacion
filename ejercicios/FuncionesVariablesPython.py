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
# # # 2)A continuación, escriba un programa que indique si el número ingresado es palíndromo o no, usando la función invertir_digitos:
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
def buscando_Alza():
    alza = 0.0
    anterior = 0.0
    for i in range(1,n+1,1): # pido el valor del alza cada dia
        x = float(input("Dia {:2}: ".format(i)))
        if i != 1:
            if x-anterior > alza: #buscamos el alza mayor
                alza = x-anterior
        anterior = x
    return alza
n = int(input("Cuantos dias? "))

alza = buscando_Alza()
if alza == 0.0:
    print("No hubo alzas.")
else:
    print("La mayor alza fue de {:.2f} pesos".format(alza))