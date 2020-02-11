# Решето Эратосфена eratosthenes.py

def remove_duplicates(x): return list(dict.fromkeys(x))

# Функция возвращает список (sieve):
def eratosthenes(n): 
    sieve = list(range(n + 1))
    sieve[1] = 0 # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0

    return remove_duplicates(sieve)

print(eratosthenes(30))


# filter

n = 30

numbs = list(range(2, n + 1))

for numb in numbs:
    if numb != 0:
        for i in range(2 * numb, n+1, numb):
            numbs[i-2] = 0
# print(numbs)
print(list(filter(lambda x: x != 0, numbs)))

#  списковое включение
s = [x for x in range(2, n+1) if x not in [i for s in [list(range(2 * j, n+1, j)) for j in range(2, n // 2)] for i in s]]
print(s)
