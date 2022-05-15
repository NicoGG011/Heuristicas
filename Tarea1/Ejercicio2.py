
def conjuntos(lista):
    return ConjuntoPotencia([], lista)


def ConjuntoPotencia(inicial, lista):
    if lista:
        return ConjuntoPotencia(inicial, lista[1:]) + ConjuntoPotencia(inicial + [lista[0]], lista[1:])
    return [inicial]


lista = [1, 2, 3]
print(conjuntos(lista))
