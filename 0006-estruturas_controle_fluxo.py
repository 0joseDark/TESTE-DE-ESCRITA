# Script: estruturas_controle_fluxo.py
# Autor: Exemplo
# Descrição: Demonstra as estruturas de controle de fluxo em Python.

# --------------------------
# ESTRUTURA CONDICIONAL IF / ELIF / ELSE
# --------------------------
numero = 7

print("Exemplo IF / ELIF / ELSE:")
if numero > 10:
    print("O número é maior que 10")
elif numero == 10:
    print("O número é exatamente 10")
else:
    print("O número é menor que 10")   # Vai imprimir isto porque 7 < 10

print("----------------------------------")

# --------------------------
# ESTRUTURA DE REPETIÇÃO FOR
# --------------------------
print("Exemplo FOR:")
for i in range(1, 6):  # repete de 1 até 5
    print("Contagem:", i)

print("----------------------------------")

# --------------------------
# ESTRUTURA DE REPETIÇÃO WHILE
# --------------------------
print("Exemplo WHILE:")
contador = 1
while contador <= 5:   # repete enquanto a condição for verdadeira
    print("Valor do contador:", contador)
    contador += 1      # incrementa o contador (senão fica em loop infinito)

print("----------------------------------")

# --------------------------
# USANDO BREAK
# --------------------------
print("Exemplo BREAK:")
for i in range(1, 10):
    if i == 5:
        print("Encontrei o número 5! Parando o loop.")
        break   # interrompe o laço imediatamente
    print("Número:", i)

print("----------------------------------")

# --------------------------
# USANDO CONTINUE
# --------------------------
print("Exemplo CONTINUE:")
for i in range(1, 6):
    if i == 3:
        print("Saltei o número 3")
        continue   # volta para o início do laço, sem executar o resto
    print("Número:", i)
