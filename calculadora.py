def soma(a, b):
    """
    Realiza a soma de dois números.
    
    Parâmetros:
    a (int/float): Primeiro número
    b (int/float): Segundo número
    
    Retorna:
    int/float: Resultado da soma
    """
    return a + b

if __name__ == "__main__":
    print("Teste da função soma:")
    print(f"2 + 3 = {soma(2, 3)}") 
    print(f"5.5 + 4.5 = {soma(5.5, 4.5)}") 
    print(f'6 + 2 = {soma(6,2)}')
    print(f'8 + 2 = {soma(8,2)}')

def subtracao(a, b):
    """
    Realiza a subtração de dois números.

    Parâmetros:
    a (int/float): Primeiro número
    b (int/float): Segundo número
    
    Retorna:
    int/float: Resultado da subtração
    """
    return a - b

if __name__ == "__main__":
    print("Teste da função subtracao:")
    print(f"5 - 3 = {subtracao(5, 3)}")
    print(f"10.5 - 4.5 = {subtracao(10.5, 4.5)}")
    print(f'8 - 2 = {subtracao(8,2)}')

def multiplicacao(a, b):
    """
    Realiza a multiplicação de dois números.
    Parâmetros:
    a (int/float): Primeiro número
    b (int/float): Segundo número

    Retorna:
    int/float: Resultado da multiplicação
    """
    return a * b

if __name__ == "__main__":
    print("Teste da função multiplicacao:")
    print(f"2 * 3 = {multiplicacao(2, 3)}")
    print(f"5.5 * 4.5 = {multiplicacao(5.5, 4.5)}")
    print(f'6 * 2 = {multiplicacao(6,2)}')
    print(f'8 * 2 = {multiplicacao(8,2)}')
