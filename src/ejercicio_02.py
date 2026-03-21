# Dada la siguiente playlist con canciones y sus duraciones en formato "m:ss":

# Calcule la duración total de la playlist en formato Xm Ys, y encuentre la
# canción más larga y la más corta.
# Nota: Deberá convertir las duraciones de string a valores
# numéricos para poder operar con ellas.


playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]

def duracion_a_segundos(duracion):
    minutos, segundos = duracion.split(':')
    return int(minutos) * 60 + int(segundos)

def segundos_a_duracion(segundos):
    minutos = segundos // 60
    seg = segundos % 60
    return f"{minutos}:{seg:02d}"

total = sum(duracion_a_segundos(item["duration"]) for item in playlist)
total = segundos_a_duracion(total)
cancion_mas_larga = max(playlist, key=lambda item: duracion_a_segundos(item["duration"]))
cancion_mas_corta = min(playlist, key=lambda item: duracion_a_segundos(item["duration"]))
print(f"La duracion total de la playlist es: {total}")
print(f'Canción más larga: "{cancion_mas_larga ["title"]}" ({(cancion_mas_larga ["duration"])})')
print(f'Canción más corta: "{cancion_mas_corta ["title"]}" ({(cancion_mas_corta ["duration"])})')