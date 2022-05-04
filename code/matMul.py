#Implementacion de multiplicacion de matrices 
import random
n= 1300 
low,high = 0,100
cols,rows = n,n

r = [random.choices(range(low,high), k=cols) for _ in range(rows)]

def matMul (m1,m2):
    m =[]
    for i in range(rows):
        aux = []
        for j in range(cols):
            suma = 0
            for h in range(rows):
                suma += m1[i][h]*m2[h][j]
            aux.append(suma)
        m.append(aux)
    return m

matMul(r,r)
print("Finished")
