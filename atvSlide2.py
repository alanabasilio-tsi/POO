class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    @property
    def salario (self) -> float:
        return self._salario