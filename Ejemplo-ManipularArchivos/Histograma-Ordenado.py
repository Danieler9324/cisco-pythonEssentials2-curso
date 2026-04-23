# El histograma de salida se ordenará en función de la frecuencia de los caracteres (el contador más grande debe presentarse primero).
# El histograma debe enviarse a un archivo con el mismo nombre que el de entrada, pero con la extensión '.hist' (debe concatenarse con el nombre original).
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

    ordenar = sorted(contador.items(), key=lambda x: x[1], reverse=True)
    nombreSalida = archnombre + ".hist"
    salida = open(nombreSalida, "wt")

    for letra, cantidad in ordenar:
        linea = f"{letra} -> {cantidad}\n"
        salida.write(linea)
    
    salida.close()

    print("Histograma guardado en: ", nombreSalida)
    

except IOError as excp:
    print("No se puede acceder al codigo fuente: ", strerror(excp.errno))
    exit(excp.errno)        