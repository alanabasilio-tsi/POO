print('#APLICAÇÃO FUNCIONARIO #######################')
class SalarioInvalidoError (Exception):
    pass

class Funcionario:
    salarioMinimo = 1621
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    @property
    def salario (self) -> float:
        return self._salario

    @salario.setter
    def salario (self, salarioNovo: float):  
            if (salarioNovo < self.salarioMinimo):
                raise SalarioInvalidoError("Salário abaixo do mínimo!")
            self._salario = salarioNovo

    def aumentar (self, percentual):
        float(percentual)
        if (percentual > 0 and percentual <= 30):
            self._salario += (percentual*self._salario)/100 
        else:
            raise ValueError ("Valor inválido")

try:
    funcionario = Funcionario('alana',1000)
    funcionario2 = Funcionario('alana',30000)
    funcionario2.aumentar(50)
    funcionario2.aumentar(30)
    print(funcionario2.salario)

except SalarioInvalidoError as erro:
    print (erro)

except ValueError as erro:
    print (erro)

print('#APLICAÇÃO EMAIL #######################')
print('**************************************************')

class EmailInvalidoError (Exception):
    pass

class Email:
    def __init__ (self, email:str):
        self.email = email

    @property
    def email (self):
        return self._email

    @email.setter
    def email (self, email):
        if ("@" in email and '.' in email):
            self._email = email
        else:
            raise EmailInvalidoError ('Email inválido!')

try:
    email = Email ('alaninha')
    email2 = Email ('alaninha@gg.com')
    print (email2.email)

except EmailInvalidoError as erro:
    print (erro)


