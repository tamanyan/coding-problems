A, B = list(map(int, input().split()))
out = 1
ans = 0

while out < B:
    out += A - 1
    ans += 1

print(ans)
