# Relatório de Testes (PT-BR)

## 1) Resumo
Todos os testes unitários e de integração foram executados e passaram neste ambiente. O projeto agora inclui **um teste extra por item** (3.1 → 3.10). A implementação (`src/calculadora.py`) foi ajustada para tratar overflow em potenciação e para corresponder à mensagem de erro de divisão por zero usada pelos testes. As mudanças estão documentadas na docstring do código-fonte.

---

## 2) Resultado completo dos testes (unittest discover)
```
test_cadeia_sub_mul (test_integracao.Testes.test_cadeia_sub_mul) ... ok
test_integracao_historico_resultado (test_integracao.Testes.test_integracao_historico_resultado) ... ok
test_operacoes_sequenciais (test_integracao.Testes.test_operacoes_sequenciais) ... ok
test_consistencia_historico (test_unidade.Testes.test_consistencia_historico) ... ok
test_divisao_por_zero (test_unidade.Testes.test_divisao_por_zero) ... ok
test_entrada_saida_div (test_unidade.Testes.test_entrada_saida_div) ... ok
test_entrada_saida_exp (test_unidade.Testes.test_entrada_saida_exp) ... ok
test_entrada_saida_mult (test_unidade.Testes.test_entrada_saida_mult) ... ok
test_entrada_saida_soma (test_unidade.Testes.test_entrada_saida_soma) ... ok
test_entrada_saida_sub (test_unidade.Testes.test_entrada_saida_sub) ... ok
test_extra_3_10_typeerror_message (test_unidade.Testes.test_extra_3_10_typeerror_message)
3.10 extra: TypeError message for invalid types is clear ... ok
test_extra_3_1_input_output_floats (test_unidade.Testes.test_extra_3_1_input_output_floats)
3.1 extra: operations with floats ... ok
test_extra_3_2_typing_list_raises (test_unidade.Testes.test_extra_3_2_typing_list_raises)
3.2 extra: passing a list must raise TypeError ... ok
test_extra_3_3_history_contains_potencia (test_unidade.Testes.test_extra_3_3_history_contains_potencia)
3.3 extra: history records power operation ... ok
test_extra_3_4_initialization_independent_instances (test_unidade.Testes.test_extra_3_4_initialization_independent_instances)
3.4 extra: two instances have independent state ... ok
test_extra_3_5_clear_history_idempotent (test_unidade.Testes.test_extra_3_5_clear_history_idempotent)
3.5 extra: clearing history twice stays empty and no exception ... ok
test_extra_3_6_multiplicar_by_zero (test_unidade.Testes.test_extra_3_6_multiplicar_by_zero)
3.6 extra: multiplying by zero yields zero ... ok
test_extra_3_7_potencia_produces_inf_for_huge_inputs (test_unidade.Testes.test_extra_3_7_potencia_produces_inf_for_huge_inputs)
3.7 extra: very large power may produce infinity ... ok
test_extra_3_8_potencia_very_large_exponent (test_unidade.Testes.test_extra_3_8_potencia_very_large_exponent)
3.8 extra: very large exponent should not crash (may produce inf) ... ok
test_extra_3_9_control_flow_result_unchanged_on_error (test_unidade.Testes.test_extra_3_9_control_flow_result_unchanged_on_error)
3.9 extra: failed operation (division by zero) does not change last result ... ok
test_fluxos_divisao (test_unidade.Testes.test_fluxos_divisao) ... ok
test_inicializacao (test_unidade.Testes.test_inicializacao) ... ok
test_limite_inferior (test_unidade.Testes.test_limite_inferior) ... ok
test_limite_superior (test_unidade.Testes.test_limite_superior) ... ok
test_mensagens_erro (test_unidade.Testes.test_mensagens_erro) ... ok
test_modificacao_historico (test_unidade.Testes.test_modificacao_historico) ... ok
test_tipagem_invalida_dividir (test_unidade.Testes.test_tipagem_invalida_dividir) ... ok
test_tipagem_invalida_multiplicar (test_unidade.Testes.test_tipagem_invalida_multiplicar) ... ok
test_tipagem_invalida_potencia (test_unidade.Testes.test_tipagem_invalida_potencia) ... ok
test_tipagem_invalida_soma (test_unidade.Testes.test_tipagem_invalida_soma) ... ok
test_tipagem_invalida_subtrair (test_unidade.Testes.test_tipagem_invalida_subtrair) ... ok

----------------------------------------------------------------------
Ran 31 tests in 0.004s

OK
```

## 3) Relatório de coverage
```
Name                       Stmts   Miss  Cover
----------------------------------------------
src/calculadora.py            48      0   100%
tests/test_integracao.py      28      0   100%
tests/test_unidade.py        151      2    99%
----------------------------------------------
TOTAL                        227      2    99%
```

## 4) Arquivos alterados / adicionados
- **Modificado** `src/calculadora.py`  
  - Centralizou a validação de tipos em `_validate_numbers`.
  - `potencia`: agora captura `OverflowError` e normaliza o resultado para `float('inf')` em caso de overflow, evitando falhas em plataformas onde `**` lança erro.
  - Docstring adicionada com a documentação das correções.
- **Modificado** `tests/test_unidade.py`  
  - Adicionou o teste de potencia para 3.1.
  - Adicionou **10 testes extras** (um por item 3.1..3.10), com nomes `test_extra_3_1_*` … `test_extra_3_10_*`.

---

## 5) Correções aplicadas (detalhado)
1. **_validate_numbers**  
   - Garante que funções aritméticas levantem `TypeError("Argumentos devem ser numeros")` quando recebam tipos inválidos.

2. **potencia**  
   - Problema: `base ** expoente` pode lançar `OverflowError` para entradas muito grandes em algumas plataformas.
   - Correção: envolveu a operação em `try/except` e, em caso de `OverflowError`, retorna `float('inf')`. Isso mantém comportamento numérico e evita que os testes falhem por exceção.

4. **Documentação**  
   - Todas as correções foram documentadas na docstring da classe `Calculadora` e no próprio `relatorio.md`.
