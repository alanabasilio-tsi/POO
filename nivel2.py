class Veiculo:
    def __init__(self, placa: str, diaria: float):
        self.__placa = placa
        self.__diaria = diaria

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
        if not isinstance (diaria, float):
            raise TypeError ('Diaria deve ser valor numérico')

        if diaria < 0:
            raise TypeError ("Diaria deve ser maior que zero")
        self.__diaria = diaria

    def calcular_aluguel (self, dias: int):
        pass

    def __str__ (self):
        return f"Placa: {self.__placa}, Diaria: {self.__diaria}"

class Carro (Veiculo):
    def calcular_aluguel (self, dias: int) -> float:
        aluguel = self.diaria * dias
        return aluguel

class Moto (Veiculo):
    def calcular_aluguel (self, dias: int) -> float:
        aluguel = (self.diaria * dias) - (self.diaria * dias)*0.2
        return aluguel

class Caminhao (Veiculo):
    def calcular_aluguel (self, dias: int) -> float:
        return 100

moto = Moto ('123', 200)
print(moto.calcular_aluguel(5))