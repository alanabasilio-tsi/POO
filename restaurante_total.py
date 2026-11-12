# ==============================================================================
# 1. EXCEÇÕES PERSONALIZADAS
# ==============================================================================

class EntregaForaDeAreaError(Exception):
    """Exceção lançada quando a distância ultrapassa o limite do entregador."""
    pass


class ValorInvalidoError(Exception):
    """Exceção lançada quando valores negativos ou vazios são atribuídos."""
    pass


# ==============================================================================
# 2. CLASSES DE DOMÍNIO (PRATO, CARDÁPIO, CLIENTE, ENTREGADORES)
# ==============================================================================

class Prato:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco  # Aciona o @preco.setter para validar

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str):
        if not valor or not valor.strip():
            raise ValorInvalidoError("O nome do prato não pode ser vazio.")
        self.__nome = valor.strip()

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, valor: float):
        if valor <= 0:
            raise ValorInvalidoError(f"O preço do prato deve ser maior que zero (recebido: {valor}).")
        self.__preco = float(valor)

    def __str__(self) -> str:
        return f"{self.nome} (R$ {self.preco:.2f})"


class Cardapio:
    def __init__(self):
        self.__pratos = []

    def adicionar_prato(self, prato: Prato):
        if not isinstance(prato, Prato):
            raise TypeError("Apenas objetos da classe Prato podem ser adicionados ao cardápio.")
        self.__pratos.append(prato)

    def listar_pratos(self):
        for p in self.__pratos:
            print(f" - {p}")

    def __str__(self) -> str:
        if not self.__pratos:
            return "Cardápio vazio."
        return "\n".join(f" - {p}" for p in self.__pratos)


class Cliente:
    def __init__(self, nome: str):
        self.nome = nome  # Aciona o @nome.setter

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str):
        if not valor or not valor.strip():
            raise ValorInvalidoError("O nome do cliente não pode ser vazio.")
        self.__nome = valor.strip().title()

    def __str__(self) -> str:
        return self.nome


class Entregador:
    def __init__(self, id_entregador: int):
        self.id_entregador = id_entregador

    @property
    def id_entregador(self) -> int:
        return self.__id_entregador

    @id_entregador.setter
    def id_entregador(self, valor: int):
        if valor <= 0:
            raise ValorInvalidoError("O ID do entregador deve ser positivo.")
        self.__id_entregador = valor

    def taxa_entrega(self, distancia: float) -> float:
        raise NotImplementedError("Subclasses devem implementar o método taxa_entrega.")

    def __str__(self) -> str:
        return f"{self.__class__.__name__} #{self.id_entregador}"


class DeBike(Entregador):
    DISTANCIA_MAXIMA = 5.0  # km

    def taxa_entrega(self, distancia: float) -> float:
        if distancia < 0:
            raise ValorInvalidoError("A distância não pode ser negativa.")
        if distancia > self.DISTANCIA_MAXIMA:
            raise EntregaForaDeAreaError(
                f"Entregador de bike atende até {self.DISTANCIA_MAXIMA} km (solicitado: {distancia} km)."
            )
        return 3.0 + (distancia * 1.5)


class DeMoto(Entregador):
    DISTANCIA_MAXIMA = 20.0  # km

    def taxa_entrega(self, distancia: float) -> float:
        if distancia < 0:
            raise ValorInvalidoError("A distância não pode ser negativa.")
        if distancia > self.DISTANCIA_MAXIMA:
            raise EntregaForaDeAreaError(
                f"Entregador de moto atende até {self.DISTANCIA_MAXIMA} km (solicitado: {distancia} km)."
            )
        return 5.0 + (distancia * 2.0)


# ==============================================================================
# 3. CLASSES DE PEDIDO (ITENS E PEDIDO)
# ==============================================================================

class Itens:
    def __init__(self, prato: Prato, qnt: int):
        self.prato = prato
        self.qnt = qnt  # Aciona o @qnt.setter

    @property
    def prato(self) -> Prato:
        return self.__prato

    @prato.setter
    def prato(self, valor: Prato):
        if not isinstance(valor, Prato):
            raise TypeError("O item precisa receber um objeto válido do tipo Prato.")
        self.__prato = valor

    @property
    def qnt(self) -> int:
        return self.__qnt

    @qnt.setter
    def qnt(self, valor: int):
        if valor <= 0:
            raise ValorInvalidoError("A quantidade de itens deve ser pelo menos 1.")
        self.__qnt = int(valor)

    def calcular_subtotal(self) -> float:
        return self.prato.preco * self.qnt

    def __str__(self) -> str:
        return f"{self.qnt}x {self.prato.nome} -> R$ {self.calcular_subtotal():.2f}"


class Pedido:
    def __init__(self, cliente: Cliente, entregador: Entregador):
        self.cliente = cliente
        self.entregador = entregador
        self.lista_itens = []

    def adicionar_item(self, item: Itens):
        if not isinstance(item, Itens):
            raise TypeError("Use a classe Itens para adicionar produtos ao pedido.")
        self.lista_itens.append(item)

    def calcular_subtotal_itens(self) -> float:
        return sum(obj_item.calcular_subtotal() for obj_item in self.lista_itens)

    def calcular_total(self, distancia: float) -> float:
        if not self.lista_itens:
            raise ValorInvalidoError("Não é possível calcular o total de um pedido vazio.")
        subtotal = self.calcular_subtotal_itens()
        taxa = self.entregador.taxa_entrega(distancia)
        return subtotal + taxa

    def __str__(self) -> str:
        itens_txt = "\n    ".join(str(item) for item in self.lista_itens) if self.lista_itens else "Nenhum item"
        return (
            f"Cliente: {self.cliente}\n"
            f"Entregador: {self.entregador}\n"
            f"Itens:\n    {itens_txt}\n"
            f"Subtotal (sem frete): R$ {self.calcular_subtotal_itens():.2f}"
        )


# ==============================================================================
# 4. BLOCO PRINCIPAL DE TESTES (MAIN)
# ==============================================================================

if __name__ == "__main__":
    print("=== 1. TESTE DE CADASTRO E FLUXO NORMAL ===")
    try:
        cliente1 = Cliente("alana basilio")
        entregador_bike = DeBike(1)
        entregador_moto = DeMoto(2)

        prato1 = Prato("Pizza Margherita", 40.50)
        prato2 = Prato("Hambúrguer Artesanal", 33.30)
        prato3 = Prato("Suco Natural", 9.00)

        meu_cardapio = Cardapio()
        meu_cardapio.adicionar_prato(prato1)
        meu_cardapio.adicionar_prato(prato2)
        meu_cardapio.adicionar_prato(prato3)

        print("Cardápio disponível:")
        print(meu_cardapio)
        print("-" * 45)

        item1 = Itens(prato1, 2)
        item2 = Itens(prato2, 1)

        pedido1 = Pedido(cliente1, entregador_bike)
        pedido1.adicionar_item(item1)
        pedido1.adicionar_item(item2)

        print(pedido1)
        distancia_teste = 4.0
        print(f"Total com entrega ({distancia_teste} km): R$ {pedido1.calcular_total(distancia_teste):.2f}")

    except (EntregaForaDeAreaError, ValorInvalidoError, TypeError) as erro:
        print(f"Erro inesperado no fluxo normal: {erro}")

    print("\n=== 2. TESTE DE ERRO: ENTREGA FORA DE ÁREA (BIKE > 5 KM) ===")
    try:
        # Tentando entregar a 10 km usando entregador de bike (limite é 5 km)
        total_invalido = pedido1.calcular_total(10)
        print(f"Total: R$ {total_invalido:.2f}")
    except EntregaForaDeAreaError as erro:
        print(f"[Capturado com sucesso] {erro}")

    print("\n=== 3. TESTE DE VALIDAÇÃO NOS SETTERS (PREÇO E QUANTIDADE) ===")
    try:
        prato_invalido = Prato("Refrigerante", -5.0)
    except ValorInvalidoError as erro:
        print(f"[Capturado com sucesso - Preço] {erro}")

    try:
        item_invalido = Itens(prato1, 0)
    except ValorInvalidoError as erro:
        print(f"[Capturado com sucesso - Quantidade] {erro}")

    try:
        cliente_invalido = Cliente("   ")
    except ValorInvalidoError as erro:
        print(f"[Capturado com sucesso - Nome Cliente] {erro}")

    print("\n=== 4. TESTE DE TIPO INVÁLIDO NO PEDIDO ===")
    try:
        # Tentando adicionar um Prato direto em vez de um objeto Itens
        pedido1.adicionar_item(prato3)
    except TypeError as erro:
        print(f"[Capturado com sucesso - Tipo] {erro}")

    print("\n=== 5. TESTE DE PEDIDO LONGO COM MOTO (15 KM) ===")
    try:
        pedido2 = Pedido(Cliente("carlos silva"), entregador_moto)
        pedido2.adicionar_item(Itens(prato1, 1))
        pedido2.adicionar_item(Itens(prato3, 3))
        print(pedido2)
        print(f"Total com entrega (15 km): R$ {pedido2.calcular_total(15):.2f}")
    except (EntregaForaDeAreaError, ValorInvalidoError) as erro:
        print(f"Erro no pedido 2: {erro}")