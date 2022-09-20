A = int(input())
x = A - 1986
y = x%76 #anos que sobraram
z = 76 - y #anos que faltaram
prox_obs = A + z
print(prox_obs)