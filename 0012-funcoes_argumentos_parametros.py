# Script: funcoes_argumentos_parametros.py
# Autor: Exemplo
# Descrição: Demonstra funções com diferentes tipos de argumentos e parâmetros em Python.

# --------------------------
# FUNÇÃO COM PARÂMETROS NORMAIS
# --------------------------
def saudacao(nome, idade):
    """Recebe nome e idade (parâmetros) e imprime uma mensagem"""
    print(f"Olá {nome}, tens {idade} anos!")

# Chamando a função com ARGUMENTOS
saudacao("Ana", 25)
saudacao("João", 30)

print("----------------------------------")

# --------------------------
# PARÂMETROS COM VALOR POR DEFEITO
# --------------------------
def apresentar(nome, pais="Portugal"):
    """Se não passar o argumento 'pais', usa 'Portugal' por defeito"""
    print(f"{nome} é de {pais}")

apresentar("Maria")              # usa valor por defeito
apresentar("Carlos", "Brasil")   # sobrescreve o valor

print("----------------------------------")

# --------------------------
# *ARGS (NÚMERO VARIÁVEL DE ARGUMENTOS)
# --------------------------
def somar(*numeros):
    """Recebe vários argumentos e devolve a soma"""
    return sum(numeros)

print("Soma de 1,2,3 =", somar(1, 2, 3))
print("Soma de 10,20,30,40 =", somar(10, 20, 30, 40))

print("----------------------------------")

# --------------------------
# **KWARGS (ARGUMENTOS NOMEADOS VARIÁVEIS)
# --------------------------
def info_pessoa(**dados):
    """Recebe vários pares chave=valor como argumentos"""
    for chave, valor in dados.items():
        print(chave, ":", valor)

info_pessoa(nome="Ricardo", idade=28, cidade="Lisboa")

print("----------------------------------")

# --------------------------
# COMBINANDO PARÂMETROS
# --------------------------
def resumo(a, b=0, *args, **kwargs):
    """
    Exemplo com todos os tipos:
    - a, b → parâmetros normais (b tem valor por defeito)
    - *args → lista extra de argumentos
    - **kwargs → argumentos nomeados extra
    """
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

resumo(1, 2, 3, 4, 5, nome="Sofia", idade=22)
