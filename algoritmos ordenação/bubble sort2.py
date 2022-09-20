v = [int(x) for x in input().split()]
n = len(v)
for fim in range(n-1,0,-1):
    for i in range(0,fim):
        if v[i] > v[i+1]:
            v[i],v[i+1] = v[i+1],v[i] 
    #ao final do loop mais interno, o maior elemento estará na posição fim   
print(*v) 