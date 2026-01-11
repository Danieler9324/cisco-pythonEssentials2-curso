def read_int(prompt, min, max):
    try:
        numero = int(input(prompt))
        if numero <= min or numero >= max:
            raise ValueError
        return numero
    except ValueError:
        print("Debe ser un numero entero")
    except:
        print("Tu numero debe estar en el rango de", min,"a", max)

v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)
    