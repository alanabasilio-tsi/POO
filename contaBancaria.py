print('**************************************************')
print('APLICAÇÃO BANCO ###############################')

import errosDeConta

class ContaBancaria:
    def __init__(self) -> None:
        self.saldo = 0

    @property
    def saldo (self) -> float:
        return self._saldo

    @saldo.setter 
    def saldo (self, saldo:float):
        if (saldo >= 0):
            self._saldo = saldo
        else:
            raise errosDeConta.ValorInvalidoError ('Valor inválido')

    def depositar (self, valorDeposito):
        if (valorDeposito <= 0 ):
            raise errosDeConta.ValorInvalidoError("Erro ao depositar: Informe um valor válido")
        
        else:
            print (f'Saldo anterior: {self._saldo}')           
            self._saldo+=valorDeposito       
            print (f'Novo saldo: {self._saldo}')

    def sacar (self, valorSaque):
        if (valorSaque <= 0):
            raise errosDeConta.ValorInvalidoError("Erro ao sacar: Digite um valor númerico")

        if (valorSaque > self._saldo):
            raise errosDeConta.SaldoInsuficienteError("Saldo insuficiente")

        if (valorSaque > 1000):
            raise errosDeConta.LimiteExcedidoError("Limite de R$1000 excedido")           
        
        else:           
            print (f'Saldo anterior: {self._saldo}')           
            self.saldo -= valorSaque      
            print (f'Novo saldo: {self._saldo:.2f}')

