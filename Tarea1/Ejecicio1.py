# Dado dos enteros a y b, cacule la cantidad de n´umeros de fibonacci que hay entre a y b, inclusive. Por ejemplo,
# si a = 2 y b = 6, el resultado es 3 (0,1,1,2,3,5,8,13,...).
# Su implementaci´on debe considerar:
# Funci´on recursiva: FiboNumbers()
# Entrada: a,b.
# Salida: cantidad de n´umeros de la serie fibonacci entre a y b.
# - a: tomar´a valores entre 2 y 1000, inclusive.
# - b: tomar´a valores entre a y 1000, inclusive.

def FiboNumbers(n):
    if n == 0 or n == 1:
        return n
    return FiboNumbers(n - 1) + FiboNumbers(n - 2)

def num_fib(a, b):
    if a < 2 or b < a:
        print('Valores no validos')
    else:
        lista = [i for i in range(b)]
        remover = [i for i in range(a + 1)]
        for i in remover:
            lista.remove(i)
        add = []
        for i in lista:
            add.append(FiboNumbers(i))
        return len(add)


print(num_fib(2, 6))