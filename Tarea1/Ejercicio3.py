
def MaxTip(lista):
    candidates = lista
    s = []
    t = 0
    for _ in range(len(lista)):

        while candidates is not None:
            m = max(candidates)
            break
        if t > m:
            continue
        else:
            s.append(m - t)
        t += 1
        candidates.remove(m)
    return sum(s)

print(MaxTip([3, 3, 3, 3]))
print(MaxTip([3, 2, 3]))
print(MaxTip([7, 8, 6, 9, 10]))
print(MaxTip([1, 1, 1, 1, 2]))
print(MaxTip([1, 2, 3]))
