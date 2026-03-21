# Calcule el costo de envío de un paquete según su peso (en kg) y la zona de
# destino. El usuario debe ingresar ambos valores.
# Las zonas válidas son: local, regional, nacional.
# Peso / Zona    |Local  |Regional |Nacional
# Hasta 1 kg     |$500   |$1000    |$2000
# Entre 1 y 5 kg |$1000  |$2500    |$4500
# Más de 5 kg    |$2000  |$5000    |$8000
# Si la zona no es válida, debe indicar el error.

def valido_local(peso)-> float:
    if peso < 1:
        return 500
    elif peso <=5:
        return 1000
    else:
        return 2000

def valido_regional(peso)-> float:
    if peso < 1:
        return 1000
    elif peso <=5:
        return 2500
    else:
        return 5000

def valido_nacional(peso)-> bool:
    if peso < 1:
        return 2000
    elif peso <=5:
        return 4500
    else:
        return 8000

peso = float(input("Ingrese el peso del paqute (kg): "))
zona = input("Ingrese la zona de destino (local/regional/nacional): ").lower()
match zona:
    case "local":
        print(f"Costo de envio: ${valido_local(peso)}")
    case "regional":
        print(f"Costo de envio: ${valido_regional(peso)}")
    case "nacional":
        print(f"Costo de envio: ${valido_nacional(peso)}")
    case _:
        print("Zona no válida. Las zonas disponibles son: local, regional, nacional.")