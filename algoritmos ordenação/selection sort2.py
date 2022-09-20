v = [int(x) for x in input().split()]
n = len(v)
for fim in range(n-1,0,-1):
    #determina o indice do maior elemento(imaior)
    imaior = 0
    for i in range(1,fim+1):
        if v[i] > v[imaior]:
            imaior = i
    #permuta o maior com o ultimo
    v[imaior],v[fim] = v[fim],v[imaior]
print(*v)
