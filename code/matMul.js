let n = 600
//Function to generate random Matrix
function randomMatrix(n) {
    let a = []
    for (let i = 0; i < n ; i++) {
        let aux = []
        for (let j = 0; j < n ; j++) {
            aux.push(Math.floor(Math.random() * 10));   
        }
        a.push(aux)
    }
    return a;
}

//Function to multiplcate
function matMul(a,b,n) {
    let res = [];
    for (let i = 0, len = n; i < len; i++) {
        let aux = [];
        for (let j = 0, len = n; j < len; j++) {
            let sum = 0;
            for (let k = 0, len = n; k < len; k++) {
                sum += a[i][k]*b[k][j];
            } 
            aux.push(sum);
        }
        res.push(aux);
    }
    return res;
}

let r = randomMatrix(n)
let s = matMul(r,r,n)


