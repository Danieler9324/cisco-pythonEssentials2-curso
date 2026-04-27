# Escribe una función o método llamado find que tome dos argumentos llamados path y dir. El argumento path debe aceptar una ruta relativa o absoluta a un directorio donde 
# debe comenzar la búsqueda, mientras que el argumento dir debe ser el nombre de un directorio en el que deseas encontrar la ruta dada. Tu programa debería mostrar las rutas 
# absolutas si encuentra un directorio con el nombre dado.

# La búsqueda en el directorio debe realizarse de forma recursiva. Esto significa que la búsqueda también debe incluir todos los subdirectorios en la ruta dada.
import os

def find(path, dir):
    try:
        for elemento in os.listdir(path):
            ruta_completa = os.path.join(path, elemento)

            if os.path.isdir(ruta_completa):
                if elemento == dir:
                    print(os.path.abspath(ruta_completa))
                
                find(ruta_completa, dir)

    except PermissionError:
        pass

direc = input("Ingresa la ruta del directorio: ")
nombre = input("Ingresa el nombre del directorio a buscar: ")

find(direc, nombre)