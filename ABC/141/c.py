N, K, Q = list(map(int, input().split()))
A = [0] * Q
P = [-Q] * N

for i in range(Q):
    A[i] = int(input())

# N, K, Q = (10**5, 10*4, 10**5)
# A = [0] * Q
# P = [K] * N

# for i in range(Q):
#     A[i] = int(1)

for i in range(Q):
    P[A[i]-1] += 1

# print(P)

for i in range(N):
    if P[i] > -K:
        print('Yes')
    else:
        print('No')
