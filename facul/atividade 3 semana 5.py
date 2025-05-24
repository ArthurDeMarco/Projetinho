
from collections import namedtuple

localizacoes = []
locais = namedtuple("locais", ["latitudes", "longitudes", "local"])
while True:
    nome_local = input("Digite o nome do local: ")
    latitude = input("Digite a latidute: ")
    longitude = input("Digite a longitude: ")
    localizacao = locais(latitudes=latitude, longitudes=longitude, local=nome_local)
    localizacoes.append(localizacao)
    if input("Gostaria de cadastrar mais um monumento? (s/n): ") == "n":
        break
for localizacao in localizacoes:
    print(f"  Local: {localizacao.local}")
    print(f"  Latidudes: {localizacao.latitudes}")
    print(f"  Longitudes: {localizacao.longitudes}")