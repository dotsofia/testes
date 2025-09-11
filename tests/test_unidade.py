from calculadora import Calculadora
import sys

# Validar se os parâmetros são interpretados corretamente e os valores retornados estão corretos.

def test_entrada_saida_soma(self):
    calc = Calculadora ()
    resultado = calc.somar(5, 3)
    self.assertEqual(resultado, 8)
    self.assertEqual(calc.obter_ultimo_resultado(), 8)

def test_divisao_por_inteiro(self):
    calc = Calculadora ()
    resultado = calc.dividir(5, 2)
    self.assertEqual(resultado, 2.5)
    self.assertEqual(calc.obter_ultimo_resultado(), 2.5)


def test_entrada_saida_sub(self):
    calc = Calculadora ()
    resultado = calc.subtrair(5, 3)
    self.assertEqual(resultado, 2)
    self.assertEqual(calc.obter_ultimo_resultado(), 2)

def test_entrada_saida_mult(self):
    calc = Calculadora ()
    resultado = calc.multiplicar(5, 3)
    self.assertEqual(resultado, 15)
    self.assertEqual(calc.obter_ultimo_resultado(), 15)

def test_entrada_saida_div(self):
    calc = Calculadora ()
    resultado = calc.somar(10, 2)
    self.assertEqual(resultado, 5)
    self.assertEqual(calc.obter_ultimo_resultado(), 5)

def test_entrada_saida_exp(self):
    calc = Calculadora ()
    resultado = calc.potencia(2, 2)
    self.assertEqual(resultado, 4)
    self.assertEqual(calc.obter_ultimo_resultado(), 4)

def test_tipagem_invalida( self ) :
    calc = Calculadora ()
    with self.assertRaises(TypeError):
        calc.somar("5", 3) # String no lugar de numero
        calc.somar(None, 3) # None no lugar de numero
    with self.assertRaises( TypeError ):
        calc.dividir("10", 3) # String no lugar de numero
        calc.dividir(10, None) # None no lugar de numero
    with self.assertRaises(TypeError):
        calc.subtrair("5", 3) # String no lugar de numero
        calc.subtrair(None, 3) # None no lugar de numero
    with self.assertRaises( TypeError ):
        calc.multiplicar(10, None) # None no lugar de numero
        calc.multiplicar("10", 3) # String no lugar de numero
    with self.assertRaises(TypeError):
        calc.potencia("5", 3) # String no lugar de numero
        calc.potencia(None, 3) # None no lugar de numero

def test_consistencia_historico ( self ) :
    calc = Calculadora ()
    calc.somar(2, 3)
    calc.multiplicar(4, 5)
    self.assertEqual(len(calc.historico) , 2)
    self.assertIn("2 + 3 = 5", calc.historico)
    self.assertIn("4 * 5 = 20", calc.historico)

def test_inicializacao ( self ) :
    calc = Calculadora()
    self.assertEqual(calc.resultado , 0)
    self.assertEqual(len(calc.historico), 0)

def test_modificacao_historico ( self ) :
    calc = Calculadora()
    calc.somar(1 , 1)
    self.assertEqual(len(calc.historico) , 1)
    calc.limpar_historico()
    self.assertEqual(len(calc.historico) , 0)

def test_limite_inferior ( self ) :
    calc = Calculadora()
    # Teste com zero
    resultado = calc.somar(0 , 5)
    self.assertEqual( resultado , 5)
    # Teste com numeros negativos muito pequenos
    resultado = calc.multiplicar( -1e-10 , 2)
    self.assertEqual( resultado , -2e-10)

def test_limite_superior ( self ) :
    calc = Calculadora()
    # Teste com numeros grandes
    resultado = calc.somar(1e10, 1e10)
    self.assertEqual(resultado , 2e10 )
    resultado = calc.subtrair(sys.float_info.max, 2)
    self.assertEqual(resultado , sys.float_info.max - 2)

def test_divisao_por_zero ( self ):
    calc = Calculadora()
    with self.assertRaises( ValueError ):
        calc.dividir(10 , 0)

def test_fluxos_divisao ( self ):
    calc = Calculadora()
    # Caminho normal
    resultado = calc.dividir(10 , 2)
    self.assertEqual( resultado , 5)
    # Caminho de erro
    with self.assertRaises( ValueError ):
        calc.dividir(10 , 0)

def test_mensagens_erro ( self ) :
    calc = Calculadora()
    try :
        calc.dividir(5 , 0)
    except ValueError as e :
        self.assertEqual(str ( e ) , " Divisao por zero nao permitida ")





