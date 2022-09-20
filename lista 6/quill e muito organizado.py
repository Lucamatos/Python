#1°:inserir qtd. planetas e vetor de p. visitados
N = int(input())
C = [int(x) for x in input().split()]

#2°:vetor de planetas a serem verificados
P = [int(x) for x in input().split()]

#3°:realizar verificação
for i in range(0,len(P)-1):

    n = len(C)
    esq = 0
    dir = n - 1

    while esq <= dir:
        meio = (esq+dir)//2
        if C[meio] == P[i]:
            break
        elif P[i] < C[meio]:
            dir = meio - 1
        else:
            esq = meio + 1

    if C[meio] == P[i]:
        print(meio)
    else:
        print('Nao foi visitado ainda.')