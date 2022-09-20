lista = [int(x) for x in input().split()]

n = len(lista)
for j in range(n-1):
    min_index = j
    for i in range(j,n):
        if lista[i] < lista[min_index]:
            min_index = lista[i]
    j = 0
    if lista[j] > lista[min_index]:
        aux = lista[j]
        lista[j] = lista[min_index]
        lista[min_index] = aux

print(lista)
#19 27 46 2 1 98 23 32 63 54 29 17 13 26
