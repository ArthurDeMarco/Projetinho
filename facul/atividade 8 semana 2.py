num1 = float(input("Digite o primeira nota: "))
num2 = float(input("Digite o segunda nota: "))
num3 = float(input("Digite o terceira nota: "))
num4 = float(input("Digite o quarta nota: "))
pre = float(input("Informe quantas faltas: "))

media = (num1 + num2 + num3 + num4)/4
vec = 40 - pre

if media <= 6.99 and vec <= 29:
    print("Reprovado")
elif media >= 6.99 and vec <= 29:
    print("Reprovado")
elif media <= 6.99 and vec >= 29:
    print("Reprovado")
else:
    print("Aprovado")