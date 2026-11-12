import erros
import veiculo

class Locadora:
    def __init__ (self, cod_locadora: int):
        self.cod_locadora = cod_locadora
        self.estoque = []
        self.faturamento_total = 0

    @property
    def cod_locadora (self):
        return self.__cod_locadora

    @cod_locadora.setter 
    def cod_locadora(self, cod_locadora):
        if not isinstance (cod_locadora, int):
            raise TypeError ('Tipo precisa ser inteiro!')
        if cod_locadora <= 0:
            raise ValueError ('Precisa ser maior que zero')
        self.__cod_locadora = cod_locadora

    def cadastrar_veiculo(self, objeto: veiculo.Veiculo): #EXPLICAR MELHOR AGREGAÇÃO E COMPOSIÇÃO
        if not isinstance(objeto, veiculo.Veiculo):
            raise TypeError('Apenas instâncias de Veiculo podem ser cadastradas!')
        self.estoque.append(objeto)

    def ver_estoque (self):
        for veiculo in self.estoque:
            print (veiculo.descricao())

    def alugar (self, placa:str, dias: int):
        for veiculo in self.estoque:
            if veiculo.placa == placa:
                self.faturamento_previsto(veiculo.calcular_aluguel(dias))
                return f'{veiculo} alugado com sucesso!'
            
        raise erros.veiculoNaoEncontrado ('Veículo não encontrado no estoque da locadora')      

    def faturamento_previsto (self, faturamento: float):
        self.faturamento_total += faturamento 
        return self.faturamento_total

    def ver_faturamento (self):
        return self.faturamento_total

############ TESTES
locadora1 = Locadora(1)    

carro1 = veiculo.Carro ('123', 500)
moto1 = veiculo.Moto ('456', 200)
veiculo1 = veiculo.Veiculo('789',600)

locadora1.cadastrar_veiculo(carro1) 
locadora1.cadastrar_veiculo(moto1)   

locadora1.alugar('123',5)
locadora1.ver_estoque()
print(locadora1.ver_faturamento())
