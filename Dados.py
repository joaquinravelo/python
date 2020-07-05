import random
import string
import statistics
import math



min = 1
max = 6

juego: str = input("tiras los dados?")
## Contamos los turnos, para saber cuantas veces tiramos los dados
turnos = 0
## Creamos una lista vacia para contener todos los resultados del dado 1
listadado1 = []
listadado2 = []
## Creamos una concatenacion para repetir los dados las veces que queramos
while juego == "si":
    turnos= turnos + 1
    print ("tirando los dados")
    print ("salio:")
    ###Agregar resultados del dado 1 a una lista
    dado1 = []
    dado1 = int(random.randint(min, max))
    print(dado1)
    listadado1.append(dado1)
    ##
    ###Agregar resultados del dado 2 a una lista
    dado2 = []
    dado2 = int(random.randint(min, max))
    print(dado2)
    listadado2.append(dado2)
    ##
    #while len(listadado1) < (turnos):
    print("otra vez?")
    juego=input()
if juego != "si":
    print("Turnos:", turnos)
    print("Lista de resultados del dado 1:", listadado1)
    print("Lista de resultados del dado 2:", listadado2)
    ##
    ##Crear una lista consolidada de resultados
listaambos = listadado1 + listadado2
print ("La lista consolidada de resultados es:", listaambos)
print ("gracias")
## Preguntamos que estadisticas queremos ver de cada uno
stats: str = input("Quieres ver estadisticas de los dados?")
while stats == "si" or "ok":
    print ("Analicemos pues")
    print ("Quieres ver de cual dado?")
    cualdado = ["1", "2", "ambos"]
    escoger: str = input(cualdado)
    str(escoger)
    #print(*cualdado, sep="\n")
    #print(escoger)
    estadistica = ["promedio", "media", "moda"]
    info: str = input(estadistica)
    print ("estadisticas:", info, "del dado(s)", escoger)
    #######
    ###Dado 1
    while "1" in cualdado:
        if "promedio" in info:
            promdado1 = [listadado1]
            promdado1 = statistics.mean(listadado1)
            print(promdado1)
            break
        if "media" in info:
            mediadado1 = [listadado1]
            mediadado1 = statistics.median(listadado1)
            print(mediadado1)
            break
        if "moda" in info:
            modadado1 = [listadado1]
            modadado1 = statistics.mode(listadado1)
            print(modadado1)
            break
    print("listo el dado 1")
    #####
    ##Dado 2
    while "2" in cualdado:
        if "promedio" in info:
            promdado2 = [listadado2]
            promdado2 = statistics.mean(listadado2)
            print(promdado2)
            break
        if "media" in info:
            mediadado2 = [listadado2]
            mediadado2 = statistics.median(listadado2)
            print(mediadado2)
            break
        if "moda" in info:
            modadado2 = [listadado2]
            modadado2 = statistics.mode(listadado2)
            print(modadado2)
            print("ese es el dado 2")
            break
    print ("ese es el dado 2")
    ##########


