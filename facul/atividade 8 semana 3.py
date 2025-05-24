valor = 0;
max = int(input("Informe o valor-limite: "))
num1 = 0
num2 = 1
serie = "0, 1"
while valor < max:
    valor = num1 + num2
    if valor < max:
        num1 = num2
        num2 = valor;
        serie += ", " + str(valor)
print("Fibonacci:", serie)