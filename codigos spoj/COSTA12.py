#objetivo:dado o mapa,determinar a extansão da costa(pontos de terra tocados por água)
#1°passo:definir dimensão da matriz
L,C = [int(x) for x in input().split()]
mapa = []
#2°passo:definir linhas e elementos da matriz
for i in range(L):
    e = [x for x in input().split()]
    mapa.append(e)
#3°passo:verificar os elementos que correspondem a costa e determinar sua extensão
costa = 0
for i in range (L):
    for j in range (C):
        #da esquerda para direita e de cima para baixo
        if i < (L-1):
            if mapa[i][j]== '#' and mapa[i+1][j] == '.':
                costa += 1
        if j < (C-1):
            if mapa[i][j]== '#' and mapa[i][j+1] == '.':
                costa += 1
        #da direita para esquerda e de baixo para cima
        if i > 0:
               if mapa[i][j]== '#' and mapa[i-1][j] == '.':
                costa += 1
        if j > 0:
            if mapa[i][j]== '#' and mapa[i][j-1] == '.':
                costa += 1
#4°passo:imprimir a extensão da costa
print(costa)
