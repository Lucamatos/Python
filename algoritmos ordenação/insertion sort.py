lista = [int(x) for x in input().split()]
lenght = len(lista)
for i in range(1,lenght):
    chave = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > chave:
        lista[j+1] = lista[j]
        j = j - 1
    lista[j+1] = chave
print(lista)