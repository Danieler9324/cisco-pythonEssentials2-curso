word = input("Ingresa la palabra: ").lower()
text = input("Ingresa la cadena de caracteres: ").lower()

pos = 0
found = True

for char in word:
    pos = text.find(char, pos)
    if pos == -1:
        found = False
        break
    pos += 1

if found:
    print("Sí")
else:
    print("No")
