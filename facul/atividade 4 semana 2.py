print("Vamos fazer o calculo do seu abono da ultima parcela!")
salario = float(input("Qual o seu salario "))
abono = 0

if salario < 5000: 
    abono = salario * 0.15
else:
    abono = salario * 0.10

print("Seu salario com abono ficou ", abono)