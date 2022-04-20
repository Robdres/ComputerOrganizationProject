#Implementacion de multiplicacion de matrices 
import random 
low,high = 0,100
cols,rows = 10,10
r = [random.choices(range(low,high), k=cols) for _ in range(rows)]

def matMul (m1,m2): 
    m =[]
    for i in range(rows): 
        aux = []
        suma = 0 
        for j in range(cols): 
            suma += m1[i][j]+ m2[j][i]
            aux.append(suma)
        m.append(aux)
    return m

print(matMul(r,r))
