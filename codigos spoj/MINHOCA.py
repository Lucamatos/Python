#objetivo:dado o mapa das minhocas com a produtividade de cada célula,calcular o maximo de minhocas a serem colhidas
#1°entrada:N e M, dimensão das matrizes
#2°entrada:N linhas com M inteiros, representando a matriz do campo de produtividade das minhocas

#1°passo:definir dimensão da matriz
L,C = [int(x) for x in input().split()]
campo = []

#2°passo:definir linhas e elementos da matriz
for i in range(L):
    e = [int(x) for x in input().split()]
    campo.append(e)

#3°passo:contagem das minhocas colhidas
produtividade = []
#contagem das minhocas por linhas:
for l in range(L):
    wormsL = 0
    for c in range(C):
        wormsL += campo[l][c]
    produtividade.append(wormsL)
#contagem de minhocas por colunas:
for c in range(C):
    wormsC = 0
    for l in range(L):
        wormsC += campo[l][c]
    produtividade.append(wormsC)

#4°passo:imprimindo maior soma
maxx = int(max(produtividade))
print(maxx)