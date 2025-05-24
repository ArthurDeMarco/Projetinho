lista1 = []
lista2 = []
intercalados = []
for _ in range(5):
    num = int(input("Informe um elemento da lista 1: "))
    lista1.append(num)
for _ in range(5):
    num = int(input("Informe um elemento da lista 2: "))
    lista2.append(num)
for i in range(5):
    intercalados.append(lista1[i])
    intercalados.append(lista2[i])
print("Elementos intercalados:", intercalados)