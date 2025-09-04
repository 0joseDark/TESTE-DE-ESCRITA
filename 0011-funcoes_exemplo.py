# Script: funcoes_exemplo.py
# Autor: Exemplo
# Descrição: Demonstra a definição e utilização de funções em Python.

# --------------------------
# DEFINIR UMA FUNÇÃO SIMPLES
# --------------------------
def saudacao():
    """Exibe uma mensagem de boas-vindas"""
    print("Olá! Bem-vindo ao programa de funções.")

# Chamar a função
saudacao()

print("----------------------------------")

# --------------------------
# FUNÇÃO COM PARÂMETROS
# --------------------------
def cumprimentar(nome):
    """Recebe um nome e exibe uma saudação personalizada"""
    print("Olá,", nome, "! Prazer em conhecer-te.")

# Chamar a função passando um argumento
cumprimentar("Ana")
cumprimentar("João")

print("----------------------------------")

# --------------------------
# FUNÇÃO COM VÁRIOS PARÂMETROS
# --------------------------
def soma(a, b):
    """Recebe dois números e retorna a sua soma"""
    return a + b   # devolve o resultado

# Usar a função e guardar o resultado
resultado = soma(10, 5)
print("A soma de 10 + 5 é:", resultado)

print("----------------------------------")

# --------------------------
# FUNÇÃO COM VALOR POR DEFEITO
# --------------------------
def potencia(base, expoente=2):
    """Calcula a potência de um número (por defeito, ao quadrado)"""
    return base ** expoente

print("5² =", potencia(5))        # usa o expoente por defeito (2)
print("2³ =", potencia(2, 3))     # define expoente = 3

print("----------------------------------")

# --------------------------
# FUNÇÃO COM NÚMERO VARIÁVEL DE ARGUMENTOS
# --------------------------
def soma_varios(*numeros):
    """Soma vários números recebidos como parâmetros"""
    return sum(numeros)

print("Soma de 1, 2, 3 =", soma_varios(1, 2, 3))
print("Soma de 4, 5, 6, 7 =", soma_varios(4, 5, 6, 7))

print("----------------------------------")

# --------------------------
# FUNÇÃO ANINHADA (FUNÇÃO DENTRO DE OUTRA)
# --------------------------
def calcular_area_retangulo(largura, altura):
    """Calcula a área de um retângulo"""
    def multiplicar(x, y):   # função interna
        return x * y
    return multiplicar(largura, altura)

print("Área do retângulo 5x3 =", calcular_area_retangulo(5, 3))
