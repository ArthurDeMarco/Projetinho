nome = input("Digite o nome que ficara no cartao(max 20 caracteres):")

if len(nome) >= 21:
    print("O nome e longo demais, use no maximo 20 caracteres")
else:
    print("Seu nome foi aceito!")