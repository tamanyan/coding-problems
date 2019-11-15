import sys
import math
import heapq
import bisect
input = sys.stdin.readline

MOD = 10 ** 9 + 7


def my_sol(N, M):
    _A = {}
    A = []

    for i in map(int, input().split()):
        if i in _A:
            _A[i] += 1
        else:
            _A[i] = 1

    for (num, c) in _A.items():
        heapq.heappush(A, (num, c))
    # B = [0] * N
    # C = [0] * N
    # print(A)

    B = [0] * M
    C = [0] * M
    T = [None] * M
    for i in range(M):
        b, c = map(int, input().split())
        T[i] = (c, b)

    T = sorted(T, reverse=True)

    finish = False
    for i in range(M):
        C, B = T[i]

        while B > 0:
            item = heapq.heappop(A)

            if item[0] < C:
                replace = min(item[1], B)
                B -= replace
                remain = item[1] - replace

                heapq.heappush(A, (C, replace))

                if remain > 0:
                    heapq.heappush(A, (item[0], remain))

                # print("")
                # print(A, B, replace)
            else:
                heapq.heappush(A, item)
                finish = True
                break

        if finish is True:
            break

    ans = 0
    for a in A:
        ans += a[0] * a[1]
    print(ans)


def main():
    N, M = map(int, input().split())
    D = {}
    E = []

    for i in map(int, input().split()):
        if i in D:
            D[i] += 1
        else:
            D[i] = 1

    for i in range(M):
        B, C = map(int, input().split())
        if C in D:
            D[C] += B
        else:
            D[C] = B

    # print(D)
    for (num, c) in D.items():
        heapq.heappush(E, (-num, c))

    total = 0
    ans = 0

    while total < N:
        item = heapq.heappop(E)
        num = -item[0]
        c = item[1]
        ans += num * min(N-total, c)
        total += min(N-total, c)

    print(ans)
    # my_sol(N, M)


if __name__ == '__main__':
    main()
