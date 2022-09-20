v =[int(x) for x in input().split()]
elem = int(input())

n = len(v)
esq = 0
dir = n - 1

while esq <= dir:
    meio = (esq+dir)//2
    if v[meio] == elem:
        break
    elif elem < v[meio]:
        dir = meio - 1
    else:
        esq = meio + 1

if v[meio] == elem:
    print(meio)
else:
    print(-1)