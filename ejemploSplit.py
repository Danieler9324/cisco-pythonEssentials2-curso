def mysplit(text):
    if text == "":
        return []

    words = []
    current = ""

    for char in text:
        if char != " ":
            current += char
        else:
            if current != "":
                words.append(current)
                current = ""

    if current != "":
        words.append(current)

    return words

print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
    