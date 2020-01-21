#  Транспозиция матрицы

def matrixTranspose( matrix ):
    if not matrix: return []
    return [ [ row[ i ] for row in matrix ] for i in range( len( matrix[ 0 ] ) ) ]

print(matrixTranspose(maxl))

res = [max(lst) for lst in matrixTranspose(maxl)]
print(res)
