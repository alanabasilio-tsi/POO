from datetime import date

class QuantidadeIndisponivelError (Exception):
    pass

class EquipamentoAntigoError (Exception):
    pass

class Equipamento:

    listaEquipamentos = []

    def __init__(self, nome:str, patrimonio: str, dataAquisicao: str, qnt:int, valor:float):
        self.nome = nome
        self.patrimonio = patrimonio
        self.dataAquisicao = self.converterData(dataAquisicao)
        self.qnt = qnt
        self.valor = valor
        self.qntInicial = qnt

        self.listaEquipamentos.append(self) #inserir objeto em lista

    def __eq__(self, outro):
        if isinstance (outro, Equipamento):
            return self.patrimonio == outro.patrimonio
        return False

    @property
    def qnt (self):
        return self.__qnt

    @property
    def valor (self):
        return self.__valor

    @qnt.setter
    def qnt(self, qnt):
        if not isinstance(qnt, int):
            raise TypeError('Quantidade deve ser inteira!')

        if qnt < 0:
            raise ValueError('Quantidade não pode ser negativa!')

        self.__qnt = qnt

    @valor.setter
    def valor(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError('Valor deve ser float!')
    
        if valor < 0:
            raise ValueError('Valor não pode ser negativo!')
    
        self.__valor = valor

    def __str__(self):
        return f"Equipamento({self.nome}, Patrimonio: {self.patrimonio}, Data de aquisicao: {self.dataAquisicao}, Quantidade: {self.qnt}, Valor: {self.valor})"

    def consultarEquipamento (self, dado):
        for equipamento in self.listaEquipamentos:
            if dado == equipamento.nome or dado == equipamento.patrimonio:
                return equipamento
        else:
            return 'Equipamento não encontrado' 

    def registrarEmprestimo (self,equipamento):
        equipamentoEncontrado = self.consultarEquipamento(equipamento)
       
        if equipamentoEncontrado != "Equipamento não encontrado":

            if Equipamento.anos_de_uso (equipamentoEncontrado.dataAquisicao) > 10:
                raise EquipamentoAntigoError ('Equipamento antigo com mais de 10 anos de uso')
            if equipamentoEncontrado.qnt > 0:
                equipamentoEncontrado.qnt -= 1
                return f'Emprestimo registrado com sucesso!'
            
            else:
                raise QuantidadeIndisponivelError ('Equipamento com estoque indisponível')

        return f'Equipamento não encontrado'

    def registrarDevolucao (self,equipamento):
            equipamentoEncontrado = self.consultarEquipamento(equipamento)
           
            if equipamentoEncontrado != "Equipamento não encontrado":
                
                if equipamentoEncontrado.qnt < equipamentoEncontrado.qntInicial:
                    equipamentoEncontrado.qnt += 1
                    return f'Devolucao feita com sucesso!'
                
                return f'Equipamento com estoque completo!'
    
            return f'Equipamento não encontrado'
    
    @classmethod
    def listarEquipamentos (cls):
        cls.listaEquipamentos = sorted(cls.listaEquipamentos, key=lambda equipamento: equipamento.dataAquisicao)

        for equipamento in cls.listaEquipamentos:
            print(equipamento)

    @classmethod
    def de_registro (cls, registro: str):
        atributos = registro.split(';')

        nome = atributos[0]
        patrimonio = atributos[1]
        dataAquisicao = atributos[2]
        qnt = int(atributos[3])
        valor = float(atributos[4])

        equipamento = cls (nome,patrimonio,dataAquisicao,qnt,valor)
       
        return equipamento

    @staticmethod
    def converterData (data: str) -> date:
        return date.strptime (data,"%d/%m/%Y")

    @staticmethod
    def anos_de_uso (data: date) -> int:
        anosDiferenca = date.today().year - data.year
        return anosDiferenca

try:
    e = Equipamento('Notebook','123', '21/09/2012',3,45)

    e2 = Equipamento('Teclado','456', '03/09/2020',5,60)

    e3 = Equipamento('Mouse','789', '03/10/2017',2,21)


    Equipamento.listarEquipamentos()

    e.registrarEmprestimo('123') #REGISTRAR ERRO PARA QUANDO FOR MAIOR QUE 10 ANOS

    print(e)

    e4 = Equipamento.de_registro('Monitor;111;15/12/2022;6;400')

    Equipamento.listarEquipamentos()

except EquipamentoAntigoError as erro:
    print(erro)

except QuantidadeIndisponivelError as erro:
    print(erro)