import abc

class Calculadora(object):
    def calcular(self, valor1, valor2, operador):
        operacao = OperacaoFabrica().criar(operador)
        return None if operacao is None else operacao.executar(valor1, valor2)

class OperacaoFabrica(object):
    def criar(self, operador):
        if operador == 'soma':
            return Soma()
        elif operador == 'subtracao':
            return Subtracao()
        elif operador == 'divisao':
            return Divisao()
        elif operador == 'multiplicacao':
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
        return valor1 / valor2 if valor1 and valor2 != 0 else ZeroDivisionError
