#dada uma matriz 7x7,se o ele. for 1 verificar se a pos. inversa possui 1, se sim, somar uma peça
#1°passo:definir dimensão da matriz
L = int(7)
C = int(7)
#2°passo:definir linhas e elementos da matriz
matriz = []
for linhas in range(L):
    e = [int(x) for x in input().split()]
    matriz.append(e)
#3°passo:contar qnt. de peças em jogo
peças = 0
peças_t = 0
for l in range(L):
    for c in range(C):
        if matriz[l][c] == 1:
            if matriz[l][c] == matriz[c][l]:
                peças += 1
            if l == c:
                peças += 1
peças_t = peças//2
print(peças_t)           