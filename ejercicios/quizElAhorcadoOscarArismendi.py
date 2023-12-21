# # # Desarrolle un programa para jugar al popular juego elahorcado, el cual consiste en un personaje, el cual está a punto de ser ejecutado.
# # # Para salvarlo es necesario adivinar una palabra, de la cual sólo se conoce su longitud. El jugador debe ir eligiendo letra por letra, de modo de ir completando la palabra.
# # # Si el jugador se equivoca en una letra, es decir, la letra seleccionada no pertenece a la palabra a adivinar, el personaje pierde alguna parte de su cuerpo (un brazo, una pierna, el tronco, etc).
# # # Se puede jugar hasta que el personaje pierda la cabeza, el último resto de su trágica vida.
# # # Lea cada letra de la palabra que debe adivinarse en elementos sucesivos de un string llamado palabra. El jugador debe adivinar las letras que pertenecen a la palabra y el programa debe terminar cuando todas las letras se hayan adivinado, es decir, ganar el juego, o bien se haya cometido un número establecido de desaciertos, es decir, gana el computador.
# # # Observaciones:
# # #     Utilice un string para anotar las soluciones.
# # #     Asigne el caracter “_” a cada elemento del string, y cada vez que se adivine una letra, substituya el caracter por la letra correspondiente.
# # #     El programa debe realizarse utilzando funciones
# # #     Considere las siguientes partes del cuerpo del ahorcado: pierna derecha, pierna izquierda,brazo derecho,brazo izquierdo,tronco,cabeza

#Funciones
def crear_palabra_espacios(palabra):
    palabra_creada = ""
    for i in range(0,len(palabra),1):
        palabra_creada += "_"
    return palabra_creada
def mostrar_palabra(palabra):
    print('"',end="")
    print(palabra,end="")
    print('"')


def ingresar_caracter():
    caracter = ""
    while(len(caracter) != 1):#nos aseguramos de que ingrese solo 1 caracter
        caracter = input("Ingrese letra: ")
    return caracter
def modificar_palabra(palabra_original,palabra_actual,caracter):
    n = len(palabra_original)#cantidad de caracteres palabra original
    contador_letras_modificadas = 0
    contador_letras_repetidas = 0 # para saber si repitio la letra en el caso que tenga letras bien y 0 modificadas
    for i in range(0,n,1):
        if(palabra_original[i] == caracter):
            if(palabra_actual[i] == caracter):
                contador_letras_repetidas += 1
            else:
                palabra_actual = palabra_actual[:i] + caracter + palabra_actual[i+1:]
                contador_letras_modificadas += 1
    if(contador_letras_repetidas > 0):
        return "-"#la letra ya la habia puesto
    elif contador_letras_modificadas > 0:
        return palabra_actual # retorna la palabra modificada
    else:
        return "+"#pierde una parte del cuerpo
#Inicializar variables:
palabra = input("Ingrese la palabra: ")
palabra_usuario = crear_palabra_espacios(palabra)#creamos la palabra con solo espacios
lista_partes_cuerpo = ["pierna derecha","pierna izquierda","brazo izquierdo","brazo derecho","tronco","cabeza"]
estado_juego = 0 # 0 sigue jugando, 1 gano y 2 perdio

#Espacio principal:
print("Comienza el juego!")
#Bucle principal:
mostrar_palabra(palabra_usuario)
while(estado_juego == 0):
    
    caracter = ingresar_caracter()
    resultado = modificar_palabra(palabra,palabra_usuario,caracter)
    if(resultado == "-"):#letra repetida
        print("Ya ingresaste esa letra!")
    elif resultado == "+": #muestra que parte  pierde
        print('Pierde "{}"'.format(lista_partes_cuerpo[0]) )
        lista_partes_cuerpo.remove(lista_partes_cuerpo[0])
    else:
        palabra_usuario = resultado
        mostrar_palabra(palabra_usuario)
    if(palabra_usuario == palabra): # el usuario gano
        estado_juego = 1
    if(len(lista_partes_cuerpo) == 0):#el usuario perdio
        estado_juego = 2

if estado_juego == 1:
    print("Haz ganado!")
else:
    print("Haz perdido el juego!")
    
