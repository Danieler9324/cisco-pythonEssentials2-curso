line = input("Ingresa una linea de numeros, separalos con espacios: ").strip()

if line == "":
    print("No ingresaste ningun numero")
else:
    strings = line.split()
    total = 0

    try:
        for substr in strings:
            total += float(substr)
        print("El total es:", total)
    except ValueError:
        print(substr, "no es un numero.")