# Script: tuplos_exemplo.py
# Autor: Exemplo
# Descrição: Demonstra o uso de tuplos em Python.

# --------------------------
# CRIAR UM TUPLO
# --------------------------
cores = ("vermelho", "verde", "azul", "amarelo")
print("Tuplo de cores:", cores)

# --------------------------
# ACESSAR ELEMENTOS
# --------------------------
print("Primeira cor:", cores[0])   # índice 0 → "vermelho"
print("Última cor:", cores[-1])   # índice -1 → "amarelo"

# --------------------------
# TUPLO COM UM ÚNICO ELEMENTO
# --------------------------
um_elemento = ("laranja",)   # precisa da vírgula no fim
print("Tuplo com um elemento:", um_elemento)

# --------------------------
# PERCORRER UM TUPLO COM FOR
# --------------------------
print("Percorrendo o tuplo de cores:")
for cor in cores:
    print("-", cor)

# --------------------------
# VERIFICAR SE UM ELEMENTO EXISTE
# --------------------------
print("Existe 'verde' no tuplo?", "verde" in cores)   # True
print("Existe 'preto' no tuplo?", "preto" in cores)   # False

# --------------------------
# COMPRIMENTO DO TUPLO
# --------------------------
print("Quantidade de cores:", len(cores))

# --------------------------
# OPERAÇÕES COM TUPLOS
# --------------------------
numeros = (1, 2, 3, 4, 5)

print("Tuplo de números:", numeros)
print("Maior número:", max(numeros))   # 5
print("Menor número:", min(numeros))   # 1
print("Soma dos números:", sum(numeros))   # 15

# --------------------------
# CONCATENAR TUPLOS
# --------------------------
tuplo1 = (1, 2, 3)
tuplo2 = (4, 5, 6)
tuplo3 = tuplo1 + tuplo2   # cria um novo tuplo
print("Concatenação de tuplos:", tuplo3)

# --------------------------
# DESEMPACOTAR UM TUPLO
# --------------------------
pessoa = ("Ana", 25, "Portugal")
nome, idade, pais = pessoa   # atribui cada valor a uma variável
print("Nome:", nome)
print("Idade:", idade)
print("País:", pais)
