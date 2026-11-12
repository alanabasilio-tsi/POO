import cardapio

class Restaurante:
    def __init__(self):
        self.cardapio = cardapio.Cardapio()

    @property
    def cardapio (self):
        return self.__cardapio

    @cardapio.setter
    def cardapio (self, cardapio):
        if not isinstance (cardapio, cardapio.Cardapio):
            raise TypeError ('Cardapio deve ser um objeto do tipo Cardapio')
        self.__cardapio = cardapio