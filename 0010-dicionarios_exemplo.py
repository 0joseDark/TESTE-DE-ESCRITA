# Script: dicionarios_exemplo.py
# Autor: Exemplo
# Descrição: Demonstra o uso de dicionários (dict) em Python.

# --------------------------
# CRIAR UM DICIONÁRIO
# --------------------------
pessoa = {
    "nome": "Ana",
    "idade": 25,
    "pais": "Portugal"
}
print("Dicionário pessoa:", pessoa)

# --------------------------
# ACESSAR VALORES
# --------------------------
print("Nome:", pessoa["nome"])         # acessa pelo nome da chave
print("Idade:", pessoa.get("idade"))   # método get (evita erro se chave não existir)

# --------------------------
# ALTERAR VALORES
# --------------------------
pessoa["idade"] = 26   # altera a idade
print("Depois de alterar a idade:", pessoa)

# --------------------------
# ADICIONAR NOVOS PARES
# --------------------------
pessoa["profissao"] = "Engenheira"
print("Depois de adicionar profissão:", pessoa)

# --------------------------
# REMOVER ELEMENTOS
# --------------------------
pessoa.pop("pais")   # remove chave "pais"
print("Depois do pop:", pessoa)

del pessoa["profissao"]   # remove chave "profissao"
print("Depois do del:", pessoa)

# --------------------------
# PERCORRER UM DICIONÁRIO
# --------------------------
print("Percorrendo chaves:")
for chave in pessoa.keys():
    print("-", chave)

print("Percorrendo valores:")
for valor in pessoa.values():
    print("-", valor)

print("Percorrendo pares chave-valor:")
for chave, valor in pessoa.items():
    print(chave, ":", valor)

# --------------------------
# VERIFICAR EXISTÊNCIA DE CHAVE
# --------------------------
print("Existe 'nome' no dicionário?", "nome" in pessoa)     # True
print("Existe 'pais' no dicionário?", "pais" in pessoa)     # False (foi removido)

# --------------------------
# TAMANHO DO DICIONÁRIO
# --------------------------
print("Quantidade de pares:", len(pessoa))

# --------------------------
# DICIONÁRIO ANINHADO
# --------------------------
alunos = {
    "aluno1": {"nome": "João", "nota": 15},
    "aluno2": {"nome": "Maria", "nota": 18}
}
print("Dicionário de alunos:", alunos)
print("Nota do aluno2:", alunos["aluno2"]["nota"])  # acesso em dicionário dentro de dicionário
