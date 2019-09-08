N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

s = 0
prev = -1

for i in range(N):
    t = A[i] - 1
    s += B[t]
    if prev != -1 and prev + 1 == t:
        s += C[prev]
    prev = t

print(s)
