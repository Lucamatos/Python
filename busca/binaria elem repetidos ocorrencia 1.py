v =[int(x) for x in input().split()]
elem = int(input())

n = len(v)
esq = 0
dir = n - 1

while esq < dir:
    meio = esq + (esq + dir) // 2
    if elem > v[meio]:
        esq = meio + 1
    else:
        dir = meio 
    
if v[esq] == elem:
    print(esq)
else:
    print(-1)