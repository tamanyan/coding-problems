from itertools import accumulate


while True:
    N, K = list(map(int, input().split()))

    if N == 0 and K == 0:
        break

    A = [int(input()) for _ in range(N)]
    B = list(accumulate([0] + A))
    ans = []

    for i in range(N - K + 1):
        ans.append(B[i+K] - B[i])
    
    print(max(ans))