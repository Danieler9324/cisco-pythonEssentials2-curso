import os

# Mkdir
try:
    os.mkdir("./mi_primer_directorio") # Ruta relativa
    os.mkdir("../mi_primer_directorio") # Ruta relativa
    os.mkdir("Ejemplo-OS/mi_primer_directorio") # Ruta absoluta
    print(os.listdir())
except FileExistsError:
    print("El directorio ya existe en la ruta especificada")

#Makedirs
try:
    os.makedirs("mi_segundo_directorio/mi_tercer_directorio")
    os.chdir("mi_segundo_directorio")
    print(os.listdir())
except FileExistsError:
    print("El directorio ya existe en la ruta especificada")

#getcwd
try:
    os.makedirs("mi_cuarto_directorio/mi_quinto_directorio")
    os.chdir("mi_cuarto_directorio")
    print(os.getcwd())
    os.chdir("mi_quinto_directorio")
    print(os.getcwd())
except FileExistsError:
    print("El directorio ya existe en la ruta especificada")

#rmdir

os.mkdir("mi_sexto_directorio")
print(os.listdir())
os.rmdir("mi_sexto_directorio")
print(os.listdir())
    
#removedirs

os.makedirs("mi_septimo_directorio/mi_octavo_directorio")
os.removedirs("mi_septimo_directorio/mi_octavo_directorio")
print(os.listdir())