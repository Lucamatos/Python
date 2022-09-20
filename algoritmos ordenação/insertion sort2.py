v = [int(x) for x in input().split()]
n = len(v)
for inicio in range(1,n):
    i = inicio
    while v[i] < v[i-1] and i >= 1:
        v[i],v[i-1] = v[i-1],v[i]
        i -= 1
print(*v)