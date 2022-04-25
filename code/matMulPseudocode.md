# Pseudocode #

__function__ randomMatrix is 
    input:
    n -> rank of the square matrix
    output:
    r -> random square matrix of rank n

__implementation__:
    let r -> empty array
    for i in range n
        let aux = []
        for j in range n
            aux.append(randomNumber())
        end
        r.append(aux)
    end
    return r

__function__ matMul is
    input:
    n -> rank of the square matrix
    m1 -> matrix 1 factor
    m2 -> matrix 2 factor
    output:
    r -> result matrix

__implementation__:
    let r -> empty array
    for i in n
        let aux = []
        for j in n
            let sum = 0
            for k in n
                sum += m1[i][h]*m2[h][j]
            aux.append(sum)
        r.append(sum)
    return r
    


    
 
