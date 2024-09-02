s = input("informe a string: ")

invertida = ""

for i in range(len(s) - 1, -1, -1):
    invertida += s[i]

print(f"string invertida: {invertida}")