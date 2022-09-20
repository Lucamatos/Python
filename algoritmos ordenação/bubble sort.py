#depende do tamanho da lista e da disposição dos elementos
lista = [int(x) for x in input().split()]
lenght = len(lista)
for j in range(lenght-1):
    for i in range(lenght-1):
        if lista[i] > lista[i+1]:
            #troca de elementos nas pos. i e i+1
            lista[i],lista[i+1] = lista[i+1],lista[i]
print(lista)

