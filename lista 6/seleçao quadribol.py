#dado o tempo de cada candidato, imprimir os 8 primeiros em ordem crescente
#1°passo:entrada de N candidatos
N = int(input())

#2°passo: entrada do tempo de cada canditato
candidatos = [int(x) for x in input().split()]

#3°passo:coloca candidatos em ordem crescente utilizando bubble sort
n = len(candidatos)
for fim in range(n-1,0,-1):
    for i in range(0,fim):
        if candidatos[i] > candidatos[i+1]:
            candidatos[i],candidatos[i+1] = candidatos[i+1],candidatos[i]

#4°passo:imprime os 8 primeiros candidatos
for i in range(8):
    print(candidatos[i],end=" ")
