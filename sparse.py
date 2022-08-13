from collections import defaultdict

def sparse_matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    else:
        assert len(matrix_a[0]) == len(matrix_b)

    mapJI = defaultdict(list) # map j to a list of i, where A[i][j] != 0
    mapJK = defaultdict(list) # map j to a list of k, where B[j][k] != 0

    for i,Row in enumerate(matrix_a):
        for j,n in enumerate(Row):
            if n!=0:
                mapJI[j].append( i )

    for j,Row in enumerate(matrix_b):
        for k,n in enumerate(Row):
            if n!=0:
                mapJK[j].append( k )

    ret = [ [0 for k in range(len(matrix_b[0]))] for i in range(len(matrix_a)) ]

    for j in range(len(matrix_b)):
        for i in mapJI[j]:
            for k in mapJK[j]:
                ret[i][k] += matrix_a[i][j] * matrix_b[j][k]

    return ret