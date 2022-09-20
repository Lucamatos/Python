#dada uma matriz de dimensões 10x10, transformar em 'p' todos pontos 't' tocados por '*'.

#1°passo:inserção dos pontos do mapa
mapa = []
for i in range(10):
    pontos = list(input().split())
    mapa.append(pontos)
#2°passo:verificar na matriz os pontos 't' tocados por '*' e transformar em p
for i in range (10):
    for j in range (10):
        #da esquerda para direita e de cima para baixo
        if i < 9:
            if mapa[i][j]== 't' and mapa[i+1][j] == '*':
                mapa[i][j]= 'p'
        if j < 9:
            if mapa[i][j]== 't' and mapa[i][j+1] == '*':
                mapa[i][j]= 'p'
        #da direita para esquerda e de baixo para cima
        if i > 0:
               if mapa[i][j]== 't' and mapa[i-1][j] == '*':
                mapa[i][j]= 'p'
        if j > 0:
            if mapa[i][j]== 't' and mapa[i][j-1] == '*':
                mapa[i][j]= 'p'
#3°passo:imprimir o mapa corrigido:
for l in range(10):
    for c in range(10):
        print(mapa[l][c],end=" ")
    print()
