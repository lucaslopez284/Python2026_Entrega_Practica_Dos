# Solicite al usuario una lista de nombres de participantes (separados por
# coma). El programa debe asignar aleatoriamente a cada persona un amigo
# invisible, cumpliendo que nadie se tenga a sí mismo.
# Validaciones:
# Debe haber al menos 3 participantes.
# No debe haber nombres duplicados (comparar ignorando mayúsculas y espacios extra).
import random

def validacion(participantes)-> bool:
    if len(participantes) < 3:
        return False
    for participante in set(participantes):
        if participantes.count(participante) > 1:
            return False
    return True

def asignar_amigos(participantes)-> dict:
    asignados = partipantes.copy()
    while True:
        random.shuffle(asignados)
        valido = True
        for indice in range(len(participantes)):
            if participantes[indice] == asignados[indice]:
                valido = False
                break
        if valido:
            break
    # Convierto dos listas en un diccionario
    return dict(zip(participantes, asignados))

partipantes = input ("Ingrese una lista de participantes (separados por coma): ").lower().split(",")
partipantes = [par.strip() for par in partipantes]
if validacion(partipantes):
    resultado = asignar_amigos(partipantes)
    print("Sorteo de amigo invisible:")
    for participante, asignado in resultado.items():
        print(f"{participante.capitalize()} -> {asignado.capitalize()}")
else:
    print("Los participantes son menos de tres y/o existen nombres duplicados")
