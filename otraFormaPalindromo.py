texto = input("Ingresa un texto: ")

texto_limpio = texto.replace(" ", "").lower()

if texto_limpio == "":
    print("La cadena vacia no es un palíndromo")
elif texto_limpio == texto_limpio[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
