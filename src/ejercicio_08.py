# Implemente el cifrado César, que consiste en desplazar cada letra del alfabeto
# una cantidad fija de posiciones. 
# El programa debe:
# Solicitar un mensaje al usuario.
# Solicitar un valor de desplazamiento (número entero).
# Mostrar el mensaje cifrado.
# Mostrar el mensaje descifrado a partir del cifrado (para verificar que funciona).

mensaje = input("Ingrese un mensaje: ")
desplazamiento = int (input("Ingrese un valor de desplazamiento (número entero): "))
desplazado = ""
def cifrar(mensaje, desplazamiento)-> str:
    desplazado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            if caracter.isupper():
                nueva_letra = (ord(caracter) - ord('A') + desplazamiento) % 26
                nueva_letra = chr(nueva_letra + ord('A'))
                desplazado = desplazado + nueva_letra
            else:
                nueva_letra = (ord(caracter) - ord('a') + desplazamiento) % 26
                nueva_letra = chr(nueva_letra + ord('a'))
                desplazado = desplazado + nueva_letra
        else:
            desplazado = desplazado + caracter
    return desplazado

mensaje_desplazado = cifrar(mensaje, desplazamiento)
print(f"Mensaje cifrado: {mensaje_desplazado}")
print(f"Mensaje descifrado: {cifrar(mensaje_desplazado, -desplazamiento)}")