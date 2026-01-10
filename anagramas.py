texto1 = input("Ingresa el primer texto: ")
texto2 = input("Ingresa el segundo texto: ")

# Eliminar espacios y convertir a minúsculas
texto1 = texto1.replace(" ", "").lower()
texto2 = texto2.replace(" ", "").lower()

# Verificar que no estén vacíos
if texto1 == "" or texto2 == "":
    print("Las cadenas vacías no son anagramas")
else:
    # Comparar caracteres ordenados
    if sorted(texto1) == sorted(texto2):
        print("Los textos son anagramas")
    else:
        print("Los textos NO son anagramas")
