import math

class Calculadora:
    """
    Calculadora with basic arithmetic operations.
    
    Changes made to satisfy tests (documented here):
    - potencia: catches OverflowError when result is too large and normalizes it to float('inf').
      Some Python builds/platforms raise OverflowError on exponentiation that overflows float;
      tests expect the operation to return a numeric value (either finite or infinite) rather than crash.
    - All numeric inputs are validated; TypeError raised when non-number arguments are passed.
    """

    def __init__(self):
        self.historico = []
        self.resultado = 0

    def _validate_numbers(self, *args):
        for a in args:
            if not isinstance(a, (int, float)):
                raise TypeError("Argumentos devem ser numeros")

    def somar(self, a, b):
        self._validate_numbers(a, b)
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def subtrair(self, a, b):
        self._validate_numbers(a, b)
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def multiplicar(self, a, b):
        self._validate_numbers(a, b)
        resultado = a * b
        self.historico.append(f"{a} * {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def dividir(self, a, b):
        self._validate_numbers(a, b)
        if b == 0:
            raise ValueError("Divisao por zero nao permitida")
        resultado = a / b
        self.historico.append(f"{a} / {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def potencia(self, base, expoente):
        self._validate_numbers(base, expoente)
        try:
            resultado = base ** expoente
        except OverflowError:
            resultado = float('inf')
        self.historico.append(f"{base} ^ {expoente} = {resultado}")
        self.resultado = resultado
        return resultado

    def limpar_historico(self):
        self.historico.clear()

    def obter_ultimo_resultado(self):
        return self.resultado
