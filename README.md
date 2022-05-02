## Integrantes:

- Juan Sánchez
- Mateo Ruiz
- Roberto Alvarado

## Objetivos:

- [] Realizar un análisis comparativo de las diferentes tecnologías para el manejo de memoria
- [] Implementar en diferentes lenguajes de programación un programa para la multiplicación de matrices
- [] Comparar el uso de memoria y la eficiencia entre lenguajes de programación 

## Metodología:

Para la realización de este proyecto se hará uso de las herramientas de cada
lenguaje de programación para la implementación de un algoritmo para crear una
matriz cuadrada de dimensión n aleatoria, seguidamente se realizará la
implementación de un algoritmo de multiplicación de matrices, se busco
generalizar cada paso y las librerías utilizadas de forma que la comparación
entre lenguajes no tenga variables no controladas. Por lo tanto se espera que
la única variable que se cambiará es el lenguaje en si mismo. 

Para cada lenguaje la implementación es diferente, pero para analizar como cada
algoritmo lo maneja, se correrá cada lenguaje con matrices que vayan de una
dimensión 300 a 1500 en saltos de 100. Para todo el análisis de memoria
y tiempo se harán usos de los recursos de la linea de comandos de Linux

- time [process] : Permite medir el tiempo que le toma realizar al
  computador computar el proceso _process_, este nos ayudará a ver el tiempo que le toma
  cada lenguaje realizar el proceso 

- top : Permite mostrar todos los procesos que están activos dentro de Linux,
  este también da especificaciones de la memoria utilizada

- grep : permite encontrar strings en un archivo 
 
A continuación se presenta el pseudocode que se utiliza como base del código 

### Pseudocode 

        function randomMatrix is 
            input:
            n -> rank of the square matrix
            output:
            r -> random square matrix of rank n

        implementation:
            let r -> empty array
            for i in range n
                let aux = []
                for j in range n
                    aux.append(randomNumber())
                end
                r.append(aux)
            end
            return r
        function matMul is
            input:
            n -> rank of the square matrix
            m1 -> matrix 1 factor
            m2 -> matrix 2 factor
            output:
            r -> result matrix

        implementation:
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


## Multiplicación de matrices en cada lenguaje

[Python](./subpages/python.md)\\
[Java](./subpages/java.md)\\
[JavaScript](./subpages/javaScript.md)\\
[C++](./subpages/cpp.md)\\
[Assembly](./subpages/assembly.md)

## Resultados 

## Conclusiones
esta son la conclusiones
