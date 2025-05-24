frase = input("Digite um texto qualquer:")
consoantes = ""
for letra in frase:
    if letra.lower() not in "aeiou":
        consoantes = consoantes + letra

print(consoantes)
