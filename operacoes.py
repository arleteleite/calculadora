class Calculadora:
    """
    Esta classe representa uma calculadora simples, capaz de realizar
    operações aritméticas básicas.
    """

    def __init__(self):
        """
        O construtor da classe Calculadora.
        """
        pass # 'pass' é usado quando você não quer fazer nada no corpo do método/função por enquanto

    def somar(self, num1, num2):
        """
        Realiza a operação de soma entre dois números.
        """
        return num1 + num2

    def subtrair(self, num1, num2):
        """
        Realiza a operação de subtração entre dois números.
        """
        return num1 - num2

    def multiplicar(self, num1, num2):
        """
        Realiza a operação de multiplicação entre dois números.
        """
        return num1 * num2

    def dividir(self, num1, num2):
        """
        Realiza a operação de divisão entre dois números.
         """
        if num2 == 0:
            return "Erro: Divisão por zero não é permitida."
        return num1 / num2

    def potenciacao(self, num1, num2):
        
        return num1 ** num2
    # Você pode adicionar mais métodos aqui conforme a calculadora evolui,
    # como potenciação, raiz quadrada, etc.