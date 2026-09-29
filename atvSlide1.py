print('**************************************************')

print('APLICACAO ALUNO')

class Aluno:
    def __init__(self,nome:str, matricula:str):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def lancar_nota (self, valor:float):
        if (valor < 0 or valor > 10):
            return print("Digite um valor entre 0 e 10")
        else:
            self.notas.append(valor)

    def media (self) -> float:
        qnt_notas = len(self.notas)
        soma = 0

        for nota in self.notas:
            soma+=nota

        media = soma/qnt_notas
        return media

    def aprovado(self)->bool:
        if self.media() >= 6:
            return True
        else:
            return False

    def __str__(self):
        return (f"{self.nome} ({self.matricula}) - média {self.media():.2f}")

aluno1 = Aluno("Alana B","20261148060006")
aluno2 = Aluno("Hércules S","20261148060007")
aluno3 = Aluno("Hades D","20261148060008")

aluno1.lancar_nota(9)
aluno1.lancar_nota(8)
aluno1.lancar_nota(10)

aluno2.lancar_nota(1)
aluno2.lancar_nota(2)
aluno2.lancar_nota(3)

aluno3.lancar_nota(10)
aluno3.lancar_nota(7)
aluno3.lancar_nota(9)

alunos=[aluno1,aluno2,aluno3]

def listarAprovados(listaAlunos):
    aprovados = []
    for aluno in listaAlunos:
        if aluno.aprovado() is True:
            aprovados.append(aluno)
    return aprovados

for aluno in listarAprovados(alunos):
    print(aluno)


print('**************************************************')

print('APLICACAO RETANGULO')

class Retangulo:
    def __init__(self,base:float,altura:float):
        self.base = base
        self.altura = altura

    def area (self):
        self.base*self.altura

    def perimetro(self):
        2*(self.base+self.altura)

    def __eq__(self,outro):
        return self.base == outro.base and self.altura == outro.altura

retangulo1 = Retangulo(4,5)
retangulo2 = Retangulo(4,5)

print ("Os dois retangulos sao iguais?", retangulo1.__eq__(retangulo2))

print('**************************************************')

print('APLICACAO DATA')

class Data:
    def __init__ (self, dia:int, mes:int, ano:int):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    @classmethod 
    def de_texto(cls, dataTexto: str):
        dia, mes, ano = dataTexto.split("/")
        return cls (int(dia), int(mes), int(ano))

    @staticmethod
    def bissexto(ano:int) -> bool:
        if (ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0):
            return True
        else:
            return False

    def __str__(self):
        zeroDia = ""
        zeroMes = ""

        if (self.dia < 10):
            zeroDia = "0"
        if (self.mes < 10):
            zeroMes = "0"

        return f"{zeroDia}{self.dia}/{zeroMes}{self.mes}/{self.ano}"

            
data = Data(9, 5, 2000)

data2 = Data.de_texto("10/9/2021")

print(data)
print(data2)

ano = int(input('Escolha um ano para saber se ele e bissexto'))

print(f'{ano} bissexto: ', Data.bissexto(ano))