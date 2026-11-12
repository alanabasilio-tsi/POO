import prato, entregador, cardapio

class Cliente:
    def __init__ (self, nome: str):
        self.nome = nome

class Itens:
    def __init__(self,prato:prato.Prato, qnt:int):
        self.prato = prato
        self.qnt = qnt

    def calcular_subtotal (self)->float:
        return self.prato.preco * self.qnt

class Pedido:
    def __init__ (self, cliente: Cliente, entregador: entregador.Entregador):
        self.cliente = cliente
        self.entregador = entregador
        self.lista_itens = []

    def __str__(self):
        return f"{self.qnt}x {self.prato.nome} (R$ {self.calcular_subtotal():.2f})"
    
    def adicionar_item (self, item: Itens):
        self.lista_itens.append(item)

    def calcular_total (self, distancia: int)->float:
        total = 0.0
        for obj_item in self.lista_itens:
            total += obj_item.calcular_subtotal()
        total += self.entregador.taxa_entrega(distancia)
        return total

###### TESTEEEEEEEEE

try:
    cliente1 = Cliente ('alana')

    #entregador1 = entregador.Entregador(1)
    entregador2 = entregador.DeBike(2)
    entregador3 = entregador.DeMoto(3)

    prato1 = prato.Prato('Pizza', 40.5)
    prato2 = prato.Prato('Hamburguer', 33.3)

    cardapio1 = cardapio.Cardapio()
    cardapio1.adicionar_prato(prato1)
    cardapio1.adicionar_prato(prato2)

    item1 = Itens(prato1, 2)
    item2 = Itens(prato2, 1)

    pedido1 = Pedido (cliente1,entregador2)
    pedido1.adicionar_item(item1)
    pedido1.adicionar_item(item2)

    #pedido1.calcular_total(25)
    print(pedido1.calcular_total(10))

except entregador.EntregaForaDeAreaError as erro:
    print ('Erro na entrega')