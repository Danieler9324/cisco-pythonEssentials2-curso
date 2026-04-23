# Pida al usuario el nombre del archivo de entrada.
# Lea el archivo (si es posible) y cuente todas las letras latinas (las letras mayúsculas y minúsculas se tratan como iguales).
# Imprima un histograma simple en orden alfabético (solo se deben presentar recuentos distintos de cero).
from os import strerror

archnombre = input("Ingresa el nombre del archivo: ")

try:
    archivo = open(archnombre, "rt")
    contador = {}
    for linea in archivo:
        for caracter in linea:
            if caracter.isalpha():
                caracter = caracter.lower()
                contador[caracter] = contador.get(caracter, 0) + 1
    archivo.close()
    for letra in sorted(contador.keys()):
        print(letra, contador[letra])

except IOError as excp:
    print("No se puede acceder al codigo fuente: ", strerror(excp.errno))
    exit(excp.errno)