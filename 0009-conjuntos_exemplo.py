# Script: conjuntos_exemplo.py
# Autor: Exemplo
# Descrição: Demonstra o uso de conjuntos (sets) em Python.

# --------------------------
# CRIAR UM CONJUNTO
# --------------------------
frutas = {"maçã", "banana", "laranja", "uva", "maçã"}  # "maçã" repetida será ignorada
print("Conjunto de frutas:", frutas)   # não mostra elementos repetidos

# --------------------------
# ADICIONAR ELEMENTOS
# --------------------------
frutas.add("pera")   # adiciona um elemento
print("Depois de adicionar 'pera':", frutas)

# --------------------------
# REMOVER ELEMENTOS
# --------------------------
frutas.remove("banana")   # remove "banana" (dá erro se não existir)
print("Depois de remover 'banana':", frutas)

frutas.discard("manga")   # descarta "manga" (não dá erro se não existir)
print("Depois de descartar 'manga':", frutas)

# --------------------------
# PERCORRER UM CONJUNTO COM FOR
# --------------------------
print("Percorrendo o conjunto de frutas:")
for fruta in frutas:
    print("-", fruta)

# --------------------------
# OPERAÇÕES DE CONJUNTOS
# --------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Conjunto A:", A)
print("Conjunto B:", B)

print("União (A | B):", A | B)             # junta todos sem repetir
print("Interseção (A & B):", A & B)       # apenas os comuns
print("Diferença (A - B):", A - B)        # apenas os de A que não estão em B
print("Diferença simétrica (A ^ B):", A ^ B)  # apenas os diferentes

# --------------------------
# VERIFICAR ELEMENTOS
# --------------------------
print("Existe 2 em A?", 2 in A)   # True
print("Existe 7 em A?", 7 in A)   # False

# --------------------------
# OUTRAS OPERAÇÕES ÚTEIS
# --------------------------
print("Tamanho do conjunto A:", len(A))  # quantidade de elementos
A.clear()   # limpa o conjunto
print("Depois de limpar A:", A)
