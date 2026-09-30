"""
MÓDULO: comparativos_dunder.py
Exemplo completo e testável de métodos dunder de comparação (Rich Comparisons) em Python.
"""

import unittest
from functools import total_ordering


class Produto:
    """
    Classe que representa um produto e implementa todos os métodos dunder de comparação.
    """

    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = float(preco)

    # -------------------------------------------------------------------------
    # REPRESENTAÇÃO E CONVERSÃO (DUNDERS AUXILIARES)
    # -------------------------------------------------------------------------

    def __str__(self) -> str:
        """String legível para o usuário final."""
        return f"{self.nome} (R$ {self.preco:.2f})"

    def __repr__(self) -> str:
        """Representação detalhada para depuração."""
        return f"Produto(nome='{self.nome}', preco={self.preco})"

    def __bool__(self) -> bool:
        """Avaliação booleana: Verdadeiro se o preço for maior que zero."""
        return self.preco > 0

    # -------------------------------------------------------------------------
    # MÉTODOS DUNDER DE COMPARAÇÃO (RICH COMPARISONS)
    # -------------------------------------------------------------------------

    def __eq__(self, outro: object) -> bool:
        """Igual a (==): Compara se os preços são iguais."""
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.preco == outro.preco

    def __ne__(self, outro: object) -> bool:
        """Diferente de (!=): Compara se os preços são diferentes."""
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.preco != outro.preco

    def __lt__(self, outro: object) -> bool:
        """Menor que (<): Compara se o preço é estritamente menor."""
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.preco < outro.preco

    def __le__(self, outro: object) -> bool:
        """Menor ou igual (<=): Compara se o preço é menor ou igual."""
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.preco <= outro.preco

    def __gt__(self, outro: object) -> bool:
        """Maior que (>): Compara se o preço é estritamente maior."""
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.preco > outro.preco

    def __ge__(self, outro: object) -> bool:
        """Maior ou igual (>=): Compara se o preço é maior ou igual."""
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.preco >= outro.preco


@total_ordering
class ProdutoOtimizado:
    """
    Exemplo alternativo usando @total_ordering:
    Basta definir __eq__ e APENAS UM operador de ordem (__lt__, __le__, __gt__ ou __ge__).
    O Python gera todos os outros automaticamente!
    """

    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = float(preco)

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, ProdutoOtimizado):
            return NotImplemented
        return self.preco == outro.preco

    def __lt__(self, outro: object) -> bool:
        if not isinstance(outro, ProdutoOtimizado):
            return NotImplemented
        return self.preco < outro.preco


# =============================================================================
# SUÍTE DE TESTES UNITÁRIOS (UNITTEST)
# =============================================================================


class TestesDunderComparacao(unittest.TestCase):
    """
    Suíte de testes automatizados cobrindo todos os métodos dunder de comparação.
    """

    def setUp(self):
        self.p_barato = Produto("Caneta", 5.0)
        self.p_medio = Produto("Caderno", 25.0)
        self.p_medio_clone = Produto("Livro", 25.0)
        self.p_caro = Produto("Mochila", 150.0)
        self.p_gratis = Produto("Amostra", 0.0)

    # 1. Teste de Igualdade (__eq__) e Diferença (__ne__)
    def test_igualdade_e_diferenca(self):
        self.assertTrue(self.p_medio == self.p_medio_clone)  # __eq__
        self.assertFalse(self.p_barato == self.p_caro)  # __eq__
        self.assertTrue(self.p_barato != self.p_caro)  # __ne__
        self.assertFalse(self.p_medio != self.p_medio_clone)  # __ne__

    # 2. Teste de Menor que (__lt__) e Menor ou Igual (__le__)
    def test_menor_que_e_menor_igual(self):
        self.assertTrue(self.p_barato < self.p_medio)  # __lt__
        self.assertFalse(self.p_caro < self.p_medio)  # __lt__

        self.assertTrue(self.p_barato <= self.p_medio)  # __le__ (menor)
        self.assertTrue(self.p_medio <= self.p_medio_clone)  # __le__ (igual)
        self.assertFalse(self.p_caro <= self.p_barato)  # __le__ (falso)

    # 3. Teste de Maior que (__gt__) e Maior ou Igual (__ge__)
    def test_maior_que_e_maior_igual(self):
        self.assertTrue(self.p_caro > self.p_medio)  # __gt__
        self.assertFalse(self.p_barato > self.p_caro)  # __gt__

        self.assertTrue(self.p_caro >= self.p_medio)  # __ge__ (maior)
        self.assertTrue(self.p_medio >= self.p_medio_clone)  # __ge__ (igual)
        self.assertFalse(self.p_barato >= self.p_caro)  # __ge__ (falso)

    # 4. Teste de Ordenação Nativa (sorted / list.sort)
    def test_ordenacao_de_lista(self):
        lista_desordenada = [self.p_caro, self.p_barato, self.p_medio]
        lista_esperada = [self.p_barato, self.p_medio, self.p_caro]

        # O método sorted() usa __lt__ por padrão
        self.assertEqual(sorted(lista_desordenada), lista_esperada)

    # 5. Teste de Avaliação Booleana (__bool__)
    def test_avaliacao_booleana(self):
        self.assertTrue(bool(self.p_barato))
        self.assertFalse(bool(self.p_gratis))

    # 6. Teste de Comparação com Tipos Incompatíveis
    def test_comparacao_com_tipo_incompativel(self):
        # Quando retornado NotImplemented, o Python trata como False em == e True em !=
        self.assertFalse(self.p_barato == "uma string qualquer")
        self.assertTrue(self.p_barato != 100)

        # Para operadores de ordem (<, >), o Python lança TypeError
        with self.assertRaises(TypeError):
            _ = self.p_barato < 50

    # 7. Teste da Classe Otimizada com @total_ordering
    def test_decorador_total_ordering(self):
        po1 = ProdutoOtimizado("Teclado", 100.0)
        po2 = ProdutoOtimizado("Mouse", 50.0)

        # __gt__, __le__ e __ge__ foram gerados automaticamente pelo decorador!
        self.assertTrue(po1 > po2)
        self.assertTrue(po2 <= po1)
        self.assertTrue(po1 >= po2)


if __name__ == "__main__":
    # Executa a suíte de testes automaticamente ao rodar o arquivo
    unittest.main(verbosity=2)