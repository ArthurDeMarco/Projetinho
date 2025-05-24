import random

class Carta:
    __valor = 0
    __valor = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "dama", "valete", "rei" ]
    __naipe = 0
    __naipe = ["ouros", "espadas", "copas", "paus"]
    
    def __init__(self):
        self.__sortear()
        
    def imprimir(self):
        print(self.__valores)

