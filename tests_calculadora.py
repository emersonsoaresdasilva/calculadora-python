from calculadora import *
from unittest import main, TestCase

class TestesCalculadora(TestCase):
    def test_operacao_soma_one(self):
        resultado = Calculadora().calcular(5,5, 'soma')
        self.assertEqual(resultado, 10)

    def test_operacao_soma_two(self):
        resultado = Calculadora().calcular(-1,-1, 'soma')
        self.assertEqual(resultado, -2)

    def test_operacao_soma_three(self):
        resultado = Calculadora().calcular(0,0, 'soma')
        self.assertEqual(resultado, 0)

    def test_operacao_subtracao_one(self):
        resultado = Calculadora().calcular(10,5, 'subtracao')
        self.assertEqual(resultado, 5)

    def test_operacao_subtracao_two(self):
        resultado = Calculadora().calcular(50,1, 'subtracao')
        self.assertEqual(resultado, 49)

    def test_operacao_subtracao_three(self):
        resultado = Calculadora().calcular(0,0, 'subtracao')
        self.assertEqual(resultado, 0)

    def test_operacao_multiplicacao_one(self):
        resultado = Calculadora().calcular(5,5, 'multiplicacao')
        self.assertEqual(resultado, 25)

    def test_operacao_multiplicacao_two(self):
        resultado = Calculadora().calcular(5,5, 'multiplicacao')
        self.assertEqual(resultado, 25)

    def test_operacao_multiplicacao_three(self):
        resultado = Calculadora().calcular(5,5, 'multiplicacao')
        self.assertEqual(resultado, 25)

    def test_operacao_divisao_one(self):
        resultado = Calculadora().calcular(0,0, 'divisao')
        self.assertEqual(resultado, ZeroDivisionError)

    def test_operacao_divisao_two(self):
        resultado = Calculadora().calcular(10,2, 'divisao')
        self.assertEqual(resultado, 5)

    def test_operacao_divisao_three(self):
        resultado = Calculadora().calcular(-1, -1, 'divisao')
        self.assertEqual(resultado, 1)

    def test_operacao_sem_operador(self):
        resultado = Calculadora().calcular(10,10, None)
        self.assertEqual(resultado, None)

if __name__ == '__main__':
    main()