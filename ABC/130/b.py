N, X = map(int, input().split())
L = list(map(int, input().split()))
H = 0
ans = 0

for i in range(N):
    H += L[i]
    if H <= X:
        ans += 1

print(ans+1)
