# parte relevante
    L1 = [1, 2, 3, 4, 5]
    L2 = [4, 5, 6, 7, 8]

    clean(L1, L2)

    for i in range(max(len(L1), len(L2))):
        a = getitem(L1, i, [])
        b = getitem(L2, i, [])
        diff = []

        for j in range(max(len(a), len(b))):
            if not getitem(a, j) == getitem(b, j):
                diff.append(j)

        print a, b, diff