import prato

class Cardapio:
    def __init__(self):
        self.__lista_pratos = []

    @property
    def lista_pratos(self):
        return self.__lista_pratos

    @lista_pratos.setter
    def lista_pratos(self,lista_pratos):
        self.__lista_pratos = lista_pratos

    def adicionar_prato(self, item_prato: prato.Prato):
        if not isinstance(item_prato, prato.Prato):
            raise TypeError('Apenas objetos Prato podem ser adicionados.')    
        self.lista_pratos.append(item_prato)

    
