
def CortarVara(n: int, precios):
    val = []
    if n == 0:
        return 0
    elif n == 1:
        return precios[0]
    else:
        for i in range(1, n + 1):
            val.append(precios[i - 1] + CortarVara(n - i, precios))
        return max(val)

print(CortarVara(8, [1, 5, 8, 9, 10, 17, 17, 20]))
print(CortarVara(8, [3, 5, 8, 9, 10, 17, 17, 20]))
