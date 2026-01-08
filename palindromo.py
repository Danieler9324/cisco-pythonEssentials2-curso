texto = input("Ingresa un texto: ")

if texto == "":
    print("La cadena vacía no es un palindromo")
else:
    i = 0
    j = len(texto) - 1
    es_palindromo = True

    while i < j:
        if texto[i] == " ":
            i += 1
            continue

        if texto[j] == " ":
            j -= 1
            continue

        if texto[i].lower() != texto[j].lower():
            es_palindromo = False
            break

        i += 1
        j -= 1

    if es_palindromo:
        print("Es un palindromo")
    else:
        print("No es un palindromo")
