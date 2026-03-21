# Valide una dirección de email ingresada por el usuario con los siguientes criterios:
# Contiene exactamente un @.
# Tiene al menos un carácter antes del @.
# Tiene al menos un punto (.) después del @.
# No empieza ni termina con @ ni con ..
# La parte después del último punto tiene al menos 2 caracteres (el dominio).

def contiene_un_arroba(email)-> bool:
    return email.count("@") == 1

def caracter_antes_arroba(email)-> bool:
    return not email.startswith("@")

def no_empieza_ni_termina_con_arroba_ni_punto(email)-> bool:
    return (not email.startswith("@") 
            and not email.startswith(".") 
            and not email.endswith("@") 
            and not email.endswith("."))

def punto_despues_del_arroba(email)-> bool:
    auxiliar = -1
    for indice, caracter in enumerate(email):
        if caracter == "@":
            auxiliar = indice
            break
    if auxiliar > 0: 
        copia = email[auxiliar:]
        return copia.count(".") >= 1
    else:
        return False
    
def tiene_dominio(email) -> bool:
    auxiliar = -1 
    if not contiene_un_arroba(email):
        return False
    copia_email = email.split("@")[1]
    for indice, caracter in enumerate(copia_email):
        if caracter == ".":
            auxiliar = indice
    if auxiliar > 0: 
        copia_final = copia_email[auxiliar + 1:]
        return len(copia_final) >= 2
    else:
        return False
    
email = input("Ingrese un email: ")
if (contiene_un_arroba(email) 
    and caracter_antes_arroba(email) 
    and no_empieza_ni_termina_con_arroba_ni_punto(email) 
    and punto_despues_del_arroba(email) 
    and tiene_dominio(email)):
    print("El email es válido.")
else:
    print("El email no es válido.")