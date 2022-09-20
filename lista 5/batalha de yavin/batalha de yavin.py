#objetivo:dada as coordenadas de cada nave inimiga e de cada teleporte de Luke,dizer o total de naves destruídas
#1°passo:dimensão matriz/teleportes:
N,M = [int(x) for x in input().split()]
#2°passo: posição das naves:
matriz = []
for l in range(N):
    campo = [int(x) for x in input().split()]
    matriz.append(campo)
#3°passo:inserindo coordenadas do tp e verificando se um noob morreu:
noobs = 0
noobs = int(noobs)
for i in range(M):
    linha_tp,coluna_tp = [int(x) for x in input().split()]
    for l in range(linha_tp-1,-1,-1):
        if matriz[l][coluna_tp]==1:
            noobs+=1
            matriz[l][coluna_tp]=0
            break
        else:
            continue        
#4°passo:imprimir numero de otarios:
print(noobs)