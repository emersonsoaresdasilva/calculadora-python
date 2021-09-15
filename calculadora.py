# Ínicio →
import abc
from unittest import main, TestCase

class Calculadora(object):
    def calcular(self, valor1, valor2, operador):
        operacao = OperacaoFabrica().criar(operador)
        return 0 if operacao is None else operacao.executar(valor1, valor2)

class OperacaoFabrica(object):
    def criar(self, operador):
        if operador == 'soma':
            return Soma()
        elif operador == 'subtracao':
            return Subtracao()
        elif operador == 'divisao':
            return Divisao()
        return Multiplicacao()

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        return valor1 + valor2

class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 - valor2

class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 * valor2

class Divisao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 / valor2

class TestesCalculadora(TestCase):
    def test_operacao_soma_T1(self):
        resultado = Calculadora().calcular(5,5, 'soma')
        self.assertEqual(resultado, 10)

    def test_operacao_soma_T2(self):
        resultado = Calculadora().calcular(-1,-1, 'soma')
        self.assertEqual(resultado, -2)

    def test_operacao_soma_T3(self):
        resultado = Calculadora().calcular(0,0, 'soma')
        self.assertEqual(resultado, 0)

    def test_operacao_subtracao_T1(self):
        resultado = Calculadora().calcular(10,5, 'subtracao')
        self.assertEqual(resultado, 5)

    def test_operacao_subtracao_T2(self):
        resultado = Calculadora().calcular(50,1, 'subtracao')
        self.assertEqual(resultado, 49)

    def test_operacao_subtracao_T3(self):
        resultado = Calculadora().calcular(0,0, 'subtracao')
        self.assertEqual(resultado, 0)

    def test_operacao_multiplicacao_T1(self):
        resultado = Calculadora().calcular(5,5, 'multiplicacao')
        self.assertEqual(resultado, 25)

    def test_operacao_multiplicacao_T2(self):
        resultado = Calculadora().calcular(5,5, 'multiplicacao')
        self.assertEqual(resultado, 25)

    def test_operacao_multiplicacao_T3(self):
        resultado = Calculadora().calcular(5,5, 'multiplicacao')
        self.assertEqual(resultado, 25)

    def test_operacao_divisao_T1(self):
        resultado = Calculadora().calcular(5,5, 'divisao')
        self.assertEqual(resultado, 1)

    def test_operacao_divisao_T2(self):
        resultado = Calculadora().calcular(10,2, 'divisao')
        self.assertEqual(resultado, 5)

    def test_operacao_divisao_T3(self):
        resultado = Calculadora().calcular(5250,5, 'divisao')
        self.assertEqual(resultado, 1050)

if __name__ == '__main__':
    main()
# ← Fim