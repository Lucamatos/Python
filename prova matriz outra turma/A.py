#dada a matriz, se possuir um vírus aniquilad, imprimir sua posição, se não, imprimir 0 0
#1°passo: definir dimensão da matriz
L,C = [int(x) for x in input().split()]
matriz = []
#2°passo:definir linhas eelementos da matriz
for linhas in range(L):
    e = [int(x) for x in input().split()]
    matriz.append(e)
#3°passo:verificar se tem virus eliminado e imprimir sua posição caso contrario imprimir 0 0
for l in range(L):
    for c in range(C):
        if l>0 and l<L and c>0 and c<C:
            if matriz[l][c] == 0:
                if matriz[l][c-1]==1 and matriz[l][c+1]==1 and matriz[l-1][c]==1 and matriz[l+1][c]==1:
                    print(l,c)
                else:
                    print('0 0')

 