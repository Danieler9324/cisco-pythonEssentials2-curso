import os
os.mkdir("./mi_primer_directorio") # Ruta relativa
os.mkdir("../mi_primer_directorio") # Ruta relativa
os.mkdir("Ejemplo-OS/mi_primer_directorio") # Ruta absoluta
print(os.listdir())