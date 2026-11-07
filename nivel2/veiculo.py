from abc import ABC, abstractmethod

class Veiculo (ABC):
    def __init__(self, placa: str, diaria: float):
        self.placa = placa
        self.diaria = diaria

    @property
    def placa (self):
        return self.__placa

    @property
    def diaria (self):
        return self.__diaria

    @placa.setter
    def placa (self, placa):
        self.__placa = placa

    @diaria.setter
    def diaria (self, diaria):
        if not isinstance (diaria, (float, int)):
            raise TypeError ('Diaria deve ser valor numérico')

        if diaria < 0:
            raise ValueError ("Diaria deve ser maior que zero")
        self.__diaria = diaria

    @abstractmethod
    def calcular_aluguel (self, dias: int):
        return self.diaria * dias
#posso usar implementação ou deve ser pass?

    def descricao (self):
        return f"Placa: {self.placa}, Diaria: {self.diaria:.2f}"

class Carro (Veiculo):
    def calcular_aluguel (self, dias: int) -> float:
        return super().calcular_aluguel(dias)

class Moto (Veiculo):
    def calcular_aluguel (self, dias: int) -> float:
        return super().calcular_aluguel(dias) * 0.8

class Caminhao (Veiculo):
    def calcular_aluguel (self, dias: int) -> float:
        return super().calcular_aluguel(dias) + 100

moto = Moto ('123', 200)
print(moto.calcular_aluguel(5))
