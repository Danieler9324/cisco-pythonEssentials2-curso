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

os.makedirs("mi_segundo_directorio/mi_tercer_directorio")
os.chdir("mi_segundo_directorio")
print(os.listdir())