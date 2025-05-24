l1 = float(input("Digite o primeira lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceio lado: "))

if l1 + l2 < l3 or l1 + l3 < l2 or l3 + l2 < l1:
    print("Isso nao e um triangulo")

if l1 == l2 == l3:
    print("Esse triangulo e equilatero")
elif l1 == l2 or l1 == l2 or l3 == l2:
    print("Esse triangulo e isosceles")
else:
    print("Ele e escaleno")
