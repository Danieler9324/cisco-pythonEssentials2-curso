# Cifrado César.
text = input("Ingresa tu mensaje: ")
try:
    valor = int(input("Ingresa un numero del 1 al 25: "))
except ValueError: 
     print("Error: debes ingresar un numero entero")
else:
    if valor < 1 or valor > 25 :
        print("El numero ingresado debe estar entre 1 al 25")
    else: 
        cipher = ''
        for char in text:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    code = ord(char) - base
                    code = (code + valor) % 26
                    cipher += chr(code + base)
                else:
                    cipher += char

        print(cipher)