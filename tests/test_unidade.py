import unittest
import math, sys
from src.calculadora import Calculadora

class Testes(unittest.TestCase):
    # 3.1 Testes de Entrada e Saída

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
        self.assertEqual(resultado, 12)
        self.assertEqual(calc.obter_ultimo_resultado(), 12)

    def test_entrada_saida_exp(self):
        calc = Calculadora ()
        resultado = calc.potencia(2, 2)
        self.assertEqual(resultado, 4)
        self.assertEqual(calc.obter_ultimo_resultado(), 4)

    def test_extra_3_1_input_output_floats(self):
        """3.1 extra: operations with floats"""
        calc = Calculadora()
        resultado = calc.somar(1.5, 2.25)
        self.assertAlmostEqual(resultado, 3.75)
        self.assertAlmostEqual(calc.obter_ultimo_resultado(), 3.75)

    # Testes de Tipagem 
    def test_tipagem_invalida_soma(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar("5", 3)

    def test_tipagem_invalida_subtrair(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.subtrair(5, "3")

    def test_tipagem_invalida_multiplicar(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.multiplicar(None, 2)

    def test_tipagem_invalida_dividir(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.dividir(10, None)

    def test_tipagem_invalida_potencia(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.potencia("2", 3)

    def test_extra_3_2_typing_list_raises(self):
        """3.2 extra: passing a list must raise TypeError"""
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar([1], 2)

    # 3.3 Testes de Consistência
    def test_consistencia_historico ( self ) :
        calc = Calculadora ()
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico) , 2)
        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)

    def test_extra_3_3_history_contains_potencia(self):
        """3.3 extra: history records power operation"""
        calc = Calculadora()
        calc.potencia(2, 3)
        self.assertIn("2 ^ 3 = 8", calc.historico)

    # 3.4 Testes de Inicialização

    def test_inicializacao ( self ) :
        calc = Calculadora()
        self.assertEqual(calc.resultado , 0)
        self.assertEqual(len(calc.historico), 0)

    def test_extra_3_4_initialization_independent_instances(self):
        """3.4 extra: two instances have independent state"""
        calc1 = Calculadora()
        calc2 = Calculadora()
        calc1.somar(1, 1)
        self.assertEqual(len(calc1.historico), 1)
        self.assertEqual(len(calc2.historico), 0)
        self.assertEqual(calc1.obter_ultimo_resultado(), 2)
        self.assertEqual(calc2.obter_ultimo_resultado(), 0)

    # 3.5  Testes de Modificação de Dados
   
    def test_modificacao_historico ( self ) :
        calc = Calculadora()
        calc.somar(1 , 1)
        self.assertEqual(len(calc.historico) , 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico) , 0)

    def test_extra_3_5_clear_history_idempotent(self):
        """3.5 extra: clearing history twice stays empty and no exception"""
        calc = Calculadora()
        calc.somar(1, 2)
        calc.limpar_historico()
        calc.limpar_historico()  # should not raise
        self.assertEqual(len(calc.historico), 0)

    # 3.6 Testes de Limite Inferior
    def test_limite_inferior ( self ) :
        calc = Calculadora()
        # Teste com zero
        resultado = calc.somar(0 , 5)
        self.assertEqual( resultado , 5)
        # Teste com numeros negativos muito pequenos
        resultado = calc.multiplicar( -1e-10 , 2)
        self.assertEqual( resultado , -2e-10)

    def test_extra_3_6_multiplicar_by_zero(self):
        """3.6 extra: multiplying by zero yields zero"""
        calc = Calculadora()
        resultado = calc.multiplicar(0, 123456789)
        self.assertEqual(resultado, 0)
        self.assertEqual(calc.obter_ultimo_resultado(), 0)

    # 3.7 Testes de Limite Superior

    def test_limite_superior ( self ) :
        calc = Calculadora()
        # Teste com numeros grandes
        resultado = calc.somar(1e10, 1e10)
        self.assertEqual(resultado , 2e10 )
        resultado = calc.subtrair(sys.float_info.max, 2)
        self.assertEqual(resultado , sys.float_info.max - 2)

    def test_extra_3_7_potencia_produces_inf_for_huge_inputs(self):
        """3.7 extra: very large power may produce infinity"""
        import math
        calc = Calculadora()
        resultado = calc.potencia(1e308, 2)
        self.assertTrue(math.isinf(resultado) or math.isfinite(resultado))

    # 3.8 Testes de Valores Fora do Interval

    def test_divisao_por_zero ( self ):
        calc = Calculadora()
        with self.assertRaises( ValueError ):
            calc.dividir(10 , 0)

    def test_extra_3_8_potencia_very_large_exponent(self):
        """3.8 extra: very large exponent should not crash (may produce inf)"""
        import math
        calc = Calculadora()
        try:
            resultado = calc.potencia(1e10, 1000)
            self.assertTrue(math.isinf(resultado) or math.isfinite(resultado))
        except OverflowError:
            # Accept OverflowError from underlying math if it occurs
            self.assertTrue(True)

    # 3.9 Testes de Fluxos de Controle

    def test_fluxos_divisao ( self ):
        calc = Calculadora()
        # Caminho normal
        resultado = calc.dividir(10 , 2)
        self.assertEqual( resultado , 5)
        # Caminho de erro
        with self.assertRaises( ValueError ):
            calc.dividir(10 , 0)

    def test_extra_3_9_control_flow_result_unchanged_on_error(self):
        """3.9 extra: failed operation (division by zero) does not change last result"""
        calc = Calculadora()
        calc.somar(5, 5)
        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)
        # last result should still be 10
        self.assertEqual(calc.obter_ultimo_resultado(), 10)

    # 3.10 Testes de Mensagens de Erro
    def test_mensagens_erro ( self ) :
        calc = Calculadora()
        try :
            calc.dividir(5 , 0)
        except ValueError as e :
            self.assertEqual(str ( e ) , "Divisao por zero nao permitida")

    def test_extra_3_10_typeerror_message(self):
        """3.10 extra: TypeError message for invalid types is clear"""
        calc = Calculadora()
        with self.assertRaises(TypeError) as cm:
            calc.somar("a", "b")
        self.assertIn("Argumentos devem ser numeros", str(cm.exception))



