import fractions

# N個の最大公約数
# ユークリッド互除法

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = A[0]
    for i in range(1, N):
        ans = fractions.gcd(A[1], ans)
    print(ans)
    # A = sorted(A)

    # while True:
    #     v = A[0]
    #     tmp = [v]
    #     for i in range(len(A)):
    #         if A[i] % v == 1:
    #             print(1)
    #             return
    #         if A[i] % v == 0:
    #             pass
    #         else:
    #             tmp.append(A[i] % v)

    #     if len(A) == 1:
    #         print(A[0])
    #         return

    #     A = sorted(tmp)
    #     # print(A)


if __name__ == '__main__':
    main()