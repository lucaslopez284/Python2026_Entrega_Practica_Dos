# Dada la siguiente reseña de una película:
# Solicite al usuario una lista de palabras consideradas spoilers (separadas por
# coma). El programa debe reemplazar todas las apariciones de esas palabras en el
# texto por asteriscos (*) de la misma longitud, sin distinguir mayúsculas de
# minúsculas.
review = """La película sigue a un grupo de astronautas que
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo
a través
de tormentas solares y fallos en el sistema de navegación. Al
llegar
a Marte descubren que la base está abandonada y los
suministros
destruidos. Torres decide sacrificar la nave nodriza para
salvar
al equipo y logran volver a la Tierra en una cápsula de
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje
secreto."""

def reemplazar(string):
    aux = ""
    for chr in string:
        aux += "*"
    return aux

spoilers = input("Ingrese la lista de spoilers, separando cada palabra con coma: ")
spoilers = [s.strip().lower() for s in spoilers.split(",")]

lista_de_review = review.split()
lista_de_review = [reemplazar(palabra) if palabra.lower() in spoilers else palabra
    for palabra in lista_de_review]

print(" ".join(lista_de_review))

