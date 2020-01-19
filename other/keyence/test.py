def cleanup_list(lists):
    ranges = []
    for l in lists:
        to_insert = True
        for i in ranges:
            r = range(i[0], i[1])
            # if l overlaps with i, but l does not contain i
            if l[0] in r or l[1] in r:
                if (l[1]-l[0]) < len(r):
                    ranges.remove(i)
                else:
                    to_insert = False
            # l contains i
            if l[0] < i[0] and l[1] > i[1]:
                to_insert = False
        if to_insert:
            ranges.append(l)
    return ranges

    N = I()
    XL = [None] * N
    ans = 0

    for i in range(N):
        X, L_ = MI()
        XL[i] = (X, L_, i)

    arr = [None] * N
    for i in range(N):
        arr[i] = (XL[i][0] - XL[i][1], XL[i][0] + XL[i][1])

    arr = sorted(arr, key=lambda a: a[1])
