'''
A criação de uma matriz em Python é muito simples.
Utilizando a estrutura de dados lista, é possível
criar as linhas e colunas com facilidade.

Ao criar uma lista dentro de outra lista, procedi-
mento chamado de aninhamento, é possível formar
uma matriz.

Abaixo uma matriz 3x3

Índices ⇨ 0   1   2
⇩       0 [2,  6, -4]
⇩       1 [4,  0,  2]
⇩       2 [8, 14, 17]
'''

matriz = [
    [2, 6, -4],
    [4,  0,  2],
    [8, 14, 17],
]

linhas = len(matriz)
colunas = len(matriz[0])

# Faz a soma de todos os itens da matriz
soma = 0
for linha in matriz:
    for item in linha:
        soma += item
# Existe um problema ao somar todos os números de
# uma matriz para verificar se ela é nula.

# Verifica se é uma matriz linha, coluna, quadra-
# da ou nula.
if linhas == 1:
    print("Matriz linha.")
if colunas == 1:
    print("Matriz coluna.")
if linhas == colunas:
    print("Matriz quadrada.")
if soma == 0:
    print("Matriz nula.")
