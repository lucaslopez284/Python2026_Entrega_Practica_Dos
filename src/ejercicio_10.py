# Simule una competencia de cocina donde 5 participantes son evaluados por 3
# jueces en cada ronda. Cada juez otorga un puntaje del 1 al 10. El puntaje de la
# ronda es la suma de los tres jueces.

# Imprima la tabla de posiciones luego de cada ronda para ver la progresión de la competencia.
# Cada ronda debe indicar quién fue el ganador (mayor puntaje en la ronda).
# La cantidad de rondas ganadas se debe contabilizar.
# Se debe imprimir la tabla final con: puntaje total acumulado, cantidad de
# rondas ganadas, mejor puntaje en una ronda, y promedio por ronda. La tabla
# debe estar en orden decreciente por puntaje total.

rounds = [
{
'theme': 'Entrada',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Santiago': {'judge_1': 6, 'judge_2': 7,
'judge_3': 6},
'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 8},
}
},
{
'theme': 'Plato principal',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Mateo': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Camila': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
'Lucía': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
}
},
{
'theme': 'Postre',
'scores': {
'Valentina': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
'Mateo': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Camila': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Santiago': {'judge_1': 7, 'judge_2': 7,
'judge_3': 6},
'Lucía': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
}
},
{
'theme': 'Cocina internacional',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 9,
'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
'Santiago': {'judge_1': 8, 'judge_2': 9,
'judge_3': 7},
'Lucía': {'judge_1': 7, 'judge_2': 7,
'judge_3': 8},
}
},
{
'theme': 'Final libre',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 8,
'judge_3': 9},
'Mateo': {'judge_1': 8, 'judge_2': 9,
'judge_3': 8},
'Camila': {'judge_1': 7, 'judge_2': 7,
'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 7},
}
}
]

reporte = { 'Valentina': {'puntos': 0, 'rondas_ganadas': 0, 'mejor ronda': 0, 'promedio': 0},
      'Mateo': {'puntos': 0, 'rondas_ganadas': 0, 'mejor ronda': 0, 'promedio': 0},
      'Camila': {'puntos': 0, 'rondas_ganadas': 0, 'mejor ronda': 0, 'promedio': 0},
      'Santiago': {'puntos': 0, 'rondas_ganadas': 0, 'mejor ronda': 0, 'promedio': 0},
      'Lucía': {'puntos': 0, 'rondas_ganadas': 0, 'mejor ronda': 0, 'promedio': 0}}


def puntos_por_rondas(puntos)-> int:
    return puntos["judge_1"] + puntos["judge_2"] + puntos["judge_3"] 

def promedio(puntos, rondas)-> float:
    return puntos / rondas

def ganador_ronda(ronda)-> tuple[str,int]:
    ganador = max(ronda, key=lambda jugador: ronda[jugador])
    return ganador, ronda[ganador]

def sumar_puntos(reporte, puntajes):
    for jugador in reporte:
        reporte[jugador]["puntos"] = reporte[jugador]["puntos"] + puntajes[jugador]

def tabla_posiciones_parcial(reporte):
    reporte_en_orden = sorted(reporte, key=lambda jugador: reporte[jugador]["puntos"], reverse=True)
    posicion = 1
    for jugador in reporte_en_orden:
        print(f"{posicion}- {jugador:<10} {reporte[jugador]['puntos']}")
        posicion = posicion + 1





personas = ["Valentina", "Mateo", "Camila", "Santiago", "Lucía"]
for ronda in rounds:
    puntajes_ronda = {"Valentina" : puntos_por_rondas(ronda["scores"]["Valentina"]),
                      "Mateo" : puntos_por_rondas(ronda["scores"]["Mateo"]),
                      "Camila" : puntos_por_rondas(ronda["scores"]["Camila"]),
                      "Santiago" : puntos_por_rondas(ronda["scores"]["Santiago"]),
                      "Lucía" : puntos_por_rondas(ronda["scores"]["Lucía"])}
    datos_ganador = ganador_ronda(puntajes_ronda)
    sumar_puntos(reporte,puntajes_ronda)
    print(f"Ganador: {datos_ganador[0]} ({datos_ganador[1]} pts)")
    tabla_posiciones_parcial(reporte)



