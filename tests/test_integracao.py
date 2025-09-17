import unittest
from src.calculadora import Calculadora

class Testes(unittest.TestCase):
    def test_operacoes_sequenciais ( self ):
        calc = Calculadora()
        # Sequencia : 2 + 3 = 5 , depois 5 * 4 = 20 , depois 20 / 2 = 10
        calc . somar (2 , 3)
        resultado1 = calc.obter_ultimo_resultado()
        calc.multiplicar( resultado1 , 4)
        resultado2 = calc.obter_ultimo_resultado()
        calc.dividir( resultado2 , 2)
        resultado_final = calc.obter_ultimo_resultado()
        self.assertEqual( resultado_final , 10)
        self.assertEqual( len ( calc . historico ) , 3)

    def test_integracao_historico_resultado ( self ):
        calc = Calculadora()
        calc.potencia(2 , 3) # 2^3 = 8
        calc.somar( calc . obter_ultimo_resultado () , 2) # 8 + 2 = 10
        self.assertEqual( calc . obter_ultimo_resultado () , 10)
        self.assertEqual( len ( calc . historico ) , 2)
        self.assertIn("2 ^ 3 = 8", calc . historico )
        self.assertIn("8 + 2 = 10", calc . historico )

    def test_operacoes_sequenciais_e_limpeza(self):
        """Testa sequência e comportamento de limpar_historico (aqui verificamos retorno do método; hoje retorna None - testará essa diferença)."""
        calc = Calculadora()
        calc.somar(2, 3)          # 5
        resultado1 = calc.obter_ultimo_resultado()
        calc.multiplicar(resultado1, 4)  # 20
        resultado2 = calc.obter_ultimo_resultado()
        calc.dividir(resultado2, 2)  # 10
        resultado_final = calc.obter_ultimo_resultado()
        self.assertEqual(resultado_final, 10)
        self.assertEqual(len(calc.historico), 3)
        # agora limpa e checa retorno (esperamos lista vazia — IMPLEMENTAÇÃO ATUAL RETORNA None -> VAI FALHAR)
        retorno = calc.limpar_historico()
        self.assertEqual(retorno, [])

    def test_integracao_potencia_dividir_resultado_complexo(self):
        """Executa potência que gera complex (com base negativa + expoente fracionário) e tenta dividir o resultado —
            dividir deve rejeitar complex e levantar TypeError (implementação atual de dividir checa isinstance e levantará TypeError)."""
        calc = Calculadora()
        calc.potencia(-1, 0.5)  # atualmente armazena um complex como resultado
        # tentar usar esse resultado em dividir deve levantar TypeError por causa da checagem de tipos em dividir
        with self.assertRaises(TypeError):
            calc.dividir(calc.obter_ultimo_resultado(), 1)

