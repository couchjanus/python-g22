#  Транспозиция матрицы

def matrixTranspose( matrix ):
    if not matrix: return []
    return [ [ row[ i ] for row in matrix ] for i in range( len( matrix[ 0 ] ) ) ]

maxl = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(maxl)
print(matrixTranspose(maxl))

# Creates a list containing 3 lists, each of 3 items, all set to 0
w, h = 3, 3;
for z in (0,1,3):
    Matrix = [[x+y+1 for x in range(w)] for y in range(z)]

print(Matrix)

def make_matrix(n):
    x = range(9)
    return [[x[j] if i!=j else 0 for i in range(n)] for j in range(n)]
print(make_matrix(3))
print(matrixTranspose(make_matrix(3)))
