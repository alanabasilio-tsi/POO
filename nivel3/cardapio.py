class Prato:
    def __init__ (self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    @property
    def nome (self):
        return self.__nome

    @nome.setter
    def nome (self, nome):
        if not isinstance(nome, str):
            raise TypeError('O prato deve ser uma string.')
        self.__nome = nome

    @property
    def preco (self):
        return self.__preco

    @preco.setter
    def preco (self, preco):
        if not isinstance (preco, float):
            raise TypeError ('O preço deve ser um valor númerico.')
        if  preco <= 0:
            raise ValueError ('O preço deve ser maior que zero.')

class Cardapio:
    def __init__(self):
        self.lista_pratos = []

    def adicionar_prato(self, prato: Prato):
        if not isinstance(prato, Prato):
            raise TypeError('Apenas objetos Prato podem ser adicionados.')    
        self.lista_pratos.append(prato)

class Restaurante:
    def __init__(self, nome: str):
        self.nome = nome
        self.cardapio = Cardapio()
