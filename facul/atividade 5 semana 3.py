nume = int(input("Receba o numerador:"))
expo = int(input("Receva o expoente: "))
resul = 1
for i in range(expo):
    resul *= nume
print("O expoente" , resul)