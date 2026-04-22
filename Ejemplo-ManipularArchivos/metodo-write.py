from os import strerror

try:
    file = open('Ejemplo-ManipularArchivos/nuevoArchivo.txt', 'wt')
    for i in range(10):
        s = "linea #" + str(i+1) + "\n"
        print(s)
        for char in s:
            file.write(char)
    file.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))