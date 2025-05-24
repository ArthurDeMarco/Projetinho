def media(*numeros):
    """
    Calcula a média dos números passados para a função
   
    :param numeros: lista de números
    :return: valor da média calculada
    """
    soma = 0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)