
a = None
p = None


def f(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    elif X <= 1 + a[N-1]:
        return f(N-1, X-1)
    else:
        return p[N-1] + 1 + f(N-1, X-2-a[N-1])


def main():
    N, X = list(map(int, input().split()))
    global a
    global p
    a = [1]
    p = [1]

    for i in range(N):
        a.append(a[i] * 2 + 3)
        p.append(p[i] * 2 + 1)

    print(f(N, X))


if __name__ == '__main__':
    main()
