# Dadas las siguientes publicaciones de una red social, extraiga todos los
# hashtags (palabras que comienzan con #), cuente la frecuencia de cada uno, y
# muestre los hashtags trending (los que aparecen más de una vez).

posts = [
"""Arrancando el lunes con energía #Motivación
#NuevaSemana""",
"""Terminé mi primer proyecto en Python #Python
#Programación #OrgullosoDeMi""",
"""No puedo creer el final de la serie #SinSpoilers
#SerieAdicta""",
"""Nuevo video en el canal sobre #InteligenciaArtificial y
#Python""",
"""Entrenamiento de hoy completado #Fitness #Motivación
#NoPainNoGain""",
"""Leyendo sobre #InteligenciaArtificial y el futuro del
trabajo #Tecnología""",
"""Arranqué a estudiar #Programación por mi cuenta #Python
#Autodidacta""",
"""Finde de lluvia, maratón de series #SerieAdicta #Relax""",
"""Workshop de #InteligenciaArtificial en la universidad
#Tecnología #Programación"""
]

texto = "\n".join(posts)
lista_de_palabras = texto.split()
lista_de_tendencias = [palabra for palabra in lista_de_palabras if palabra.startswith("#")]
for tendencia in sorted(set(lista_de_tendencias), key=lambda x: lista_de_tendencias.count(x), reverse=True):
    if lista_de_tendencias.count(tendencia) > 1:
        print(f"{tendencia}: {lista_de_tendencias.count(tendencia)}")
print(f"Total de hashtags únicos: {len(set(lista_de_tendencias))}")