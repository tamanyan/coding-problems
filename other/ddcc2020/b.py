from itertools import accumulate

INF = float("inf")
IINF = 10 ** 18
MOD = 998244353

def main():
    N = int(input())
    A = list(map(int, input().split()))

    lengths = list(accumulate([0] + A))

    # length = sum(A)
    # half = len(A) // 2
    half = lengths[-1] // 2

    # print(lengths, half)

    if N == 2:
        print(abs(A[0] - A[1]))
    else:
        a1 = 0
        b1 = 0
        a2 = 0
        b2 = 0
        for i in range(1, N):
            if lengths[i] >= half:
                a1 = lengths[i]
                b1 = lengths[N] - lengths[i]
                a2 = lengths[i-1]
                b2 = lengths[N] - lengths[i-1]
                break

        # print(b2, a2)
        # print(b1, a1)
        print(min(abs(b2 - a2), abs(b1 - a1)))


if __name__ == '__main__':
    main()
