# Script: operadores_logicos.py
# Autor: Exemplo
# Descrição: Este script demonstra operadores lógicos em Python.

# Definimos duas variáveis para comparar
a = True
b = False

print("Valores usados: a =", a, " e b =", b)
print("----------------------------------")

# Operador AND (e) → só é True se as duas condições forem verdadeiras
resultado_and = a and b
print("a AND b :", resultado_and)   # False, porque True e False dá False

# Operador OR (ou) → é True se pelo menos uma condição for verdadeira
resultado_or = a or b
print("a OR b  :", resultado_or)    # True, porque True ou False dá True

# Operador NOT (não) → inverte o valor lógico
resultado_not_a = not a
resultado_not_b = not b
print("NOT a   :", resultado_not_a) # False, porque a = True, e o NOT inverte
print("NOT b   :", resultado_not_b) # True, porque b = False, e o NOT inverte

print("----------------------------------")
# Exemplo combinado com números
x = 10
y = 5

# Verifica se x é maior que 0 E y é maior que 0
print("(x > 0) and (y > 0):", (x > 0) and (y > 0))  # True, porque 10 > 0 e 5 > 0

# Verifica se x é menor que 0 OU y é menor que 0
print("(x < 0) or (y < 0):", (x < 0) or (y < 0))    # False, porque nenhum é menor que 0

# Inverte o resultado da comparação
print("not (x > y):", not (x > y))  # False, porque x > y é True, mas o NOT inverte
