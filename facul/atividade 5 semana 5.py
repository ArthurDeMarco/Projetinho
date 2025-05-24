vendas = {}
meses = [
    "janeiro",
    "fevereiro",
    "marco",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]
while True:
    mes = input("Informe o mes: ")
    valor = float(input("Informe o valor do mes: "))
    if not mes in meses:
        print("Mes invalido tente novamente")
        continue
    if mes in vendas:
        vendas[mes] += valor
    else:
        vendas[mes] = valor
    if input("Continuar adicionando? (s/n)") == "n":
        break
for mes in meses:
    if mes in vendas:
        print(f"{mes:>12}: R${vendas[mes]:.2f}")
    else:
        print(f"{mes:>12}: R$0.00")