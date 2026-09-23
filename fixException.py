class SaldoInsuficienteError (Exception):
    ... # print("Pobre. Saldo insuficiente")

class ValorInvalidoError (Exception):
    ... # print("Digite um valor númerico")

class ContaBancaria:
    def __init__(self,numeroConta:int) -> None:
        self.numeroConta = numeroConta
        self.saldo=0

    def depositar (self, valorDeposito):
        if (type(valorDeposito) != float):
            raise ValorInvalidoError("Erro ao depositar: Digite um valor númerico")
        
        else:

            print (f'Saldo anterior: {self.saldo}')
            
            self.saldo+=valorDeposito
        
            print (f'Novo saldo: {self.saldo}')

    def sacar (self, valorSaque):
        if (type(valorSaque)!=float):
            raise ValorInvalidoError("Erro ao sacar: Digite um valor númerico")

        if (valorSaque > self.saldo):
            raise SaldoInsuficienteError("Pobre. Saldo insuficiente")
        
        else:
            
            print (f'Saldo anterior: {self.saldo}')
            
            self.saldo -= valorSaque
        
            print (f'Novo saldo: {self.saldo}')

c1 = ContaBancaria(123)

try:
    c1.depositar(float("2.3"))
except ValorInvalidoError as erro:
    print(erro)

try:
    c1.sacar(2.0)
except ValorInvalidoError as erro:
    print(erro)
except SaldoInsuficienteError as erro:
    print(erro)

print("Fim do programa")

########################################################

class Aluno:
    def __init__(self,nome:str,matricula:str):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
    
    def lancar_nota(self,valor:float):
        self.notas.append(valor)

    def calcular_media(self)->float:
        soma = 0
        qtd_notas = self.notas.lenght()

        for nota in self.notas:
            soma += nota
        
        media = soma/qtd_notas
        
        return media
    