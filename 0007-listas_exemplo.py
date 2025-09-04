# Script: listas_exemplo.py
# Autor: Exemplo
# Descrição: Demonstra o uso de listas em Python.

# --------------------------
# CRIAR UMA LISTA
# --------------------------
frutas = ["maçã", "banana", "laranja", "uva"]
print("Lista de frutas:", frutas)

# --------------------------
# ACESSAR ELEMENTOS
# --------------------------
print("Primeira fruta:", frutas[0])   # índices começam em 0 → "maçã"
print("Última fruta:", frutas[-1])   # índice -1 acessa o último → "uva"

# --------------------------
# ALTERAR ELEMENTOS
# --------------------------
frutas[1] = "kiwi"   # troca "banana" por "kiwi"
print("Lista depois da alteração:", frutas)

# --------------------------
# ADICIONAR ELEMENTOS
# --------------------------
frutas.append("pera")   # adiciona no fim
print("Depois do append:", frutas)

frutas.insert(2, "abacaxi")  # insere na posição 2
print("Depois do insert:", frutas)

# --------------------------
# REMOVER ELEMENTOS
# --------------------------
frutas.remove("laranja")   # remove pelo valor
print("Depois do remove:", frutas)

elemento_removido = frutas.pop()   # remove o último e devolve
print("Elemento removido com pop():", elemento_removido)
print("Lista depois do pop:", frutas)

# --------------------------
# VERIFICAR TAMANHO
# --------------------------
print("Quantidade de frutas:", len(frutas))

# --------------------------
# PERCORRER LISTA COM FOR
# --------------------------
print("Percorrendo a lista:")
for fruta in frutas:
    print("-", fruta)

# --------------------------
# OUTROS MÉTODOS ÚTEIS
# --------------------------
numeros = [5, 2, 9, 1, 7]

print("Lista de números:", numeros)
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
print("Soma dos números:", sum(numeros))

numeros.sort()   # ordena em ordem crescente
print("Ordenada (crescente):", numeros)

numeros.reverse()  # inverte a lista
print("Lista invertida:", numeros)
