#1°:insere n° de datas
N = int(input())

#2°:insere cada data
datas = []
for i in range(N):
    data = [int(x) for x in input()]
    datas.append(data)

#3°:ordena as datas em ordem crescente
n = len(datas)
for fim in range(n-1,0,-1):
    #determina o indice do maior elemento(imaior)
    imaior = 0
    for i in range(1,fim+1):
        if datas[i] > datas[imaior]:
            imaior = i
    #permuta o maior com o ultimo
    datas[imaior],datas[fim] = datas[fim],datas[imaior]

#4°:imprimir datas em ordem crescente
for i in range(N):
    print(*datas[i],sep='')

