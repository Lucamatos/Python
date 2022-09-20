#1°:inserir dimensões da matriz
L,C = [int(x) for x in input().split()]
#2°:inserir elementos da matriz
matriz = []
for l in range(L):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)
#3°:n° de consultas
Cons = int(input())
H = [int(x) for x in input().split()]
#4°:verificar partes inundadas
for i in range(Cons):
    inun = 0
    for l in range(L):
        for c in range(C):
            if matriz[l][c] <= H[i]:
                inun +=1
    print(inun)