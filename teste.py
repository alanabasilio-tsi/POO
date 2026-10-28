from abc import ABC, abstractmethod

class Forma(ABC):
    
    def __init__(self,b:float, h:float):
        self.b = b
        self.h = h

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimetro(self) -> float: ...

    def descreva(self) -> str:
        return f'Area: {self.area()}\n Perimetro: {self.perimetro()}'

class Retangulo(Forma):
    def area(self)->float:
        return self.b * self.h

    def perimetro(self)->float:
        return 2*self.h + 2*self.b

class Triangulo (Forma):

    def area(self)->float:
        return (self.b * self.h) /2

    def perimetro(self)->float:       
        lado_triangulo = (((self.b/2)**2) + self.h**2)**0.5

        print(f"lado: {lado_triangulo}")

        return self.b + 2*lado_triangulo

try:
    f = Forma(4,5)
    
except TypeError as e:
    print(f'Erro: {e}')
    
t = Triangulo(6,4)

print(t.descreva())
