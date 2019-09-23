import math
from itertools import accumulate


N, Q = list(map(int, input().split()))
S = input()

ans = []

for i in range(len(S) - 1):
    if S[i:i+2] == 'AC':
        ans.append(1)
    else:
        ans.append(0)

# print(ans)

L = [0] * Q
R = [0] * Q
for i in range(Q):
    L[i], R[i] = list(map(int, input().split()))

ans = list(accumulate([0] + ans))
# print(ans)
for i in range(Q):
    # print(i, R[i], L[i])
    print(ans[R[i] - 1] - ans[L[i] - 1])