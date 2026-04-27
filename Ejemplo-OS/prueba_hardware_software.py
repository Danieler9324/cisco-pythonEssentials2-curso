# Para linux
import os
# print(os.uname())

# print("Nombre del sistema operativo: ", os.systemname())
# print("Nombre de la maquina en la red: ", os.nodename())
# print("Muestra la actualizacion del SO: ", os.release())
# print("Nombre de la version del sistema operativo: ", os.version)
# print("Muestra el identificador del hardware: ", os.machine())

# Para windows
import platform
print(platform.uname())

print("Nombre del sistema operativo: ", platform.system())
print("Nombre de la maquina en la red: ", platform.node())
print("Muestra la actualizacion del SO: ", platform.release())
print("Nombre de la version del sistema operativo: ", platform.version)
print("Muestra el identificador del hardware: ", platform.machine())


#System
print ("--------------- Ejemplo de System ---------------------")
valor = os.system("mkdir mi_primer_directorio")
print(valor) # 0 = exito 
             # 1 = archivo existente
    