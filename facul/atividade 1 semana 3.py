par = 0;
imp = 0;
for i in range(10):
    num = int(input("Digite o " + str(i + 1) + " numero: "))
    if num % 2 == 0:
        par += 1
    else: 
        imp += 1
print("A quantidade de numeros pares e: ", par, "e a quantidade de numeros impares e: ", imp,)