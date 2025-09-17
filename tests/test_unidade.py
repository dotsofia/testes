from calculadora import Calculadora
import math
import sys

# Validar se os parâmetros são interpretados corretamente e os valores retornados estão corretos.

def test_entrada_saida_soma(self):
    calc = Calculadora ()
    resultado = calc.somar(5, 3)
    self.assertEqual(resultado, 8)
    self.assertEqual(calc.obter_ultimo_resultado(), 8)

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


# 5.2 Entrada e Saida
def test_entrada_saida_bool_rejeitado(self):
        """Espera-se que booleans sejam rejeitados (bool é subclass de int em Python;
           implementação atual aceita True/False — este teste VAI FALHAR hoje)."""
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar(True, 1)

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

# 5.2 Tipagem
def test_tipagem_bool_em_divisao(self):
    """Teste de tipagem com bool em outra operação (deveria ser rejeitado)."""
    calc = Calculadora()
    with self.assertRaises(TypeError):
        calc.dividir(False, 2)  # vai falhar com a implementação atual (aceita False)

def test_consistencia_historico ( self ) :
    calc = Calculadora ()
    calc.somar(2, 3)
    calc.multiplicar(4, 5)
    self.assertEqual(len(calc.historico) , 2)
    self.assertIn("2 + 3 = 5", calc.historico)
    self.assertIn("4 * 5 = 20", calc.historico)

# 5.2 Consistência
def test_consistencia_historico_formatacao_divisao(self):
        """Verifica formatação exata de string no histórico para divisão."""
        calc = Calculadora()
        calc.dividir(5, 2)
        self.assertIn("5 / 2 = 2.5", calc.historico)  # deve passar com a implementação atual

def test_inicializacao ( self ) :
    calc = Calculadora()
    self.assertEqual(calc.resultado , 0)
    self.assertEqual(len(calc.historico), 0)

# 5.2 Inicialização
def test_inicializacao_tipos(self):
    calc = Calculadora()
    self.assertIsInstance(calc.historico, list)
    self.assertIsInstance(calc.resultado, (int, float))

def test_modificacao_historico ( self ) :
    calc = Calculadora()
    calc.somar(1 , 1)
    self.assertEqual(len(calc.historico) , 1)
    calc.limpar_historico()
    self.assertEqual(len(calc.historico) , 0)

# 5.2 Modificação de Dados
def test_modificacao_limpar_historico_retorno(self):
    """Espera-se que limpar_historico retorne a lista vazia. 
        Implementação atual retorna None (este teste VAI FALHAR hoje)."""
    calc = Calculadora()
    calc.somar(1, 1)
    retorno = calc.limpar_historico()
    self.assertEqual(retorno, [])  # atualmente return None -> falhará

def test_limite_inferior ( self ) :
    calc = Calculadora()
    # Teste com zero
    resultado = calc.somar(0 , 5)
    self.assertEqual( resultado , 5)
    # Teste com numeros negativos muito pequenos
    resultado = calc.multiplicar( -1e-10 , 2)
    self.assertEqual( resultado , -2e-10)

# 5.2 Testes de Limite Inferior
def test_limite_inferior_nan_deve_erro(self):
    """Verifica que NaN em entradas é tratado como erro. Atualmente a soma com NaN produz NaN (este teste VAI FALHAR)."""
    calc = Calculadora()
    with self.assertRaises(ValueError):
        calc.somar(math.nan, 1)  # implementação atual não levanta ValueError

def test_limite_superior ( self ) :
    calc = Calculadora()
    # Teste com numeros grandes
    resultado = calc.somar(1e10, 1e10)
    self.assertEqual(resultado , 2e10 )
    resultado = calc.subtrair(sys.float_info.max, 2)
    self.assertEqual(resultado , sys.float_info.max - 2)

# 5.2 Limite Superior
def test_limite_superior_float_infinite(self):
    calc = Calculadora()
    big = sys.float_info.max
    resultado = calc.somar(big, big)
    self.assertTrue(math.isinf(resultado))  # deve tornar-se inf

def test_divisao_por_zero ( self ):
    calc = Calculadora()
    with self.assertRaises( ValueError ):
        calc.dividir(10 , 0)

# 5.2 Valores Fora do Intervalo
def test_divisao_por_zero_mensagem_exata(self):
    calc = Calculadora()
    with self.assertRaises(ValueError) as cm:
        calc.dividir(10, 0)
    self.assertEqual(str(cm.exception), " Divisao por zero nao permitida ")  # verifica mensagem exata


def test_fluxos_divisao ( self ):
    calc = Calculadora()
    # Caminho normal
    resultado = calc.dividir(10 , 2)
    self.assertEqual( resultado , 5)
    # Caminho de erro
    with self.assertRaises( ValueError ):
        calc.dividir(10 , 0)

# 5.2 Fluxos de Controle
def test_fluxos_potencia_negativa_expoente_nao_inteiro(self):
    """Se base negativa e expoente não-inteiro, idealmente lançar ValueError (atua lmente retorna complexo -> este teste VAI FALHAR)."""
    calc = Calculadora()
    with self.assertRaises(ValueError):
        calc.potencia(-1, 0.5)  # implementação atual retorna número complexo, não ValueError


def test_mensagens_erro ( self ) :
    calc = Calculadora()
    try :
        calc.dividir(5 , 0)
    except ValueError as e :
        self.assertEqual(str ( e ) , " Divisao por zero nao permitida ")

# 5.2 Mensagens de Erro
def test_mensagem_erro_tipagem_contem_trecho(self):
    calc = Calculadora()
    try:
        calc.multiplicar("a", 2)
    except TypeError as e:
        self.assertIn("Argumentos", str(e))



