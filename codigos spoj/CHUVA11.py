#objetivo:dada a quantidade de chuva acumulada em cada periodo para cada região, calcular quantidade total de chuva acumulada nos dois periodos para cada uma das regiões
#1°entrada:N(inteiro)=dimensão dos dois mapas que devem ser lidos
#Prox. N*2 linhas:é dado os 2 mapas, cada um com N linhas e N elementos, sendo cada elemento a quantidade de chuva acumulada,no periodo,em 1 regiao
#saida:N linhas com N inteiros, indicando a quantidade de chuva acumulada em cada regiao após os 2 periodos
####################################################
#1°passo:entrada da dimensão dos mapas
N = int(input())

#2°passo:entrada dos mapas com quantidade de chuva acumulada em cada região
mapaP1 = []
mapaP2 = []
for i in range(N):
    linhaP1 = [int(x) for x in input().split()]
    mapaP1.append(linhaP1)
for i in range(N):
    linhaP2 = [int(x) for x in input().split()]
    mapaP2.append(linhaP2)

#3°passo:somando quantidade de chuva de cada região dos dois periodos
chuva_total = []
for l in range(N):
    chuva = []
    for c in range(N):
        chuva.append(mapaP1[l][c]+mapaP2[l][c])
    chuva_total.append(chuva)

#4°passo:imprimindo quantidade total de chuva acumulada para cada região
for l in range(N):
    for c in range(N):
        print(chuva_total[l][c],end=" ")
    print()
