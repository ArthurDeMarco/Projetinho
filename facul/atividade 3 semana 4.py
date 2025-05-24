meses = [
    "janeiro", "fevereiro", "março", "abril",
    "maio", "junho", "julho", "agosto",
    "setembro", "outubro", "novembro", "dezembro"
]
temperaturas = []
soma = 0
for mes in meses:
    temperatura = float(input("Temperatura média em " + mes + ": "))
    temperaturas.append(temperatura)
    soma += temperatura
media = soma / 12
print(f"Meses com temperatura acima da média de {media:.1f} graus:")
for i in range(12):
    if temperaturas[i] > media:
        print(f"{meses[i]}: {temperaturas[i]:.1f} graus")