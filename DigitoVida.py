naci = input("Ingresa tu fecha de nacimiento (Dia-Mes-Año): ")
suma = 0

for d in naci:
    if d.isdigit():
        suma += int(d)

print(suma)