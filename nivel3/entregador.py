from abc import ABC, abstractmethod

class EntregaForaDeAreaError (Exception):
    pass

class Entregador (ABC):
    def __init__ (self, id: int):
        self.id = id

    @property
    @abstractmethod
    def limite (self)->float:
        pass 

    @property
    def id (self):
        return self.__id

    @id.setter
    def id (self, id:int):
        if not isinstance (id, int):
            raise TypeError ('Id do entregador precisa ser inteiro')
        if id <= 0:
            raise ValueError ('Id não pode ser menor ou igual a 0')
        self.__id = id

    @abstractmethod
    def taxa_entrega (self, distancia: float)->float:
        pass

class DeBike (Entregador):
    @property
    def limite (self):
        return 10.0

    def taxa_entrega(self, distancia):
        if distancia > self.limite:
            raise EntregaForaDeAreaError ('Entrega fora de área do entregador')
        return distancia * 2

class DeMoto (Entregador):
    @property
    def limite (self):
        return 20.0
    
    def taxa_entrega(self, distancia):
        if distancia > self.limite:
            raise EntregaForaDeAreaError ('Entrega fora de área do entregador')
        return distancia * 3