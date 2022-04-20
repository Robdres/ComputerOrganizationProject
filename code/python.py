#Implementacion de multiplicacion de matrices 
import random

low,high = 0,100
cols,rows = 1000,1000

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
