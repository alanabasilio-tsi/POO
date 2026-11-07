
import veiculo

class Locadora:
    def __init__ (self, cod_locadora: int):
        self.cod_locadora = cod_locadora
        self.estoque = []

    @property
    def cod_locadora (self):
        return self.__cod_locadora

    @cod_locadora.setter 
    def cod_locadora(self, cod_locadora):
        if not isinstance (cod_locadora, int):
            raise TypeError ('Tipo precisa ser inteiro!')
        if cod_locadora < 0:
            raise ValueError ('Precisa ser maior que zero')

    def cadastrar_veiculo (self, objeto: veiculo.Veiculo):
        self.estoque.append(objeto)

    def ver_estoque (self):
        for veiculo in self.estoque:
            print (veiculo.descricao())

    def alugar (self, placa:str):
        
             

    #def faturamento_previsto (self):


############ TESTES
locadora1 = Locadora(1)    

carro1 = veiculo.Carro ('123',500)
moto1 = veiculo.Moto ('456',200)

locadora1.cadastrar_veiculo(carro1) 
locadora1.cadastrar_veiculo(moto1)   

locadora1.ver_estoque()