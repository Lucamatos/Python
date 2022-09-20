#1°:inserir n° de planetas
N = int(input())
#2°:inserir codigo dos planetas
planetas_G = [x for x in input().split()]
#3°:n° de planetas visitados
X = int(input())
#4°:planetas visitados
planetas_V = [x for x in input().split()]
#5°:matriz de distâncias
matriz = []
for l in range(N):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)
#6°:calculando distância(a partir do planeta 0)
aux = 0
distancia = 0
for i in range(X):
    n = N
    esq = 0
    dir = n - 1
    while esq <= dir:
        meio = esq + (dir - esq) // 2
        if planetas_G[meio] == planetas_V[i]:
            break
        elif planetas_V[i] < planetas_G[meio]:
            dir = meio - 1
        else:
            esq = meio + 1
    if planetas_G[meio] == planetas_V[i]:
        y = meio
    for linha in range(N):
        for coluna in range(N):
            x = aux
            distancia += matriz[x][y]
            aux = y
print(distancia)