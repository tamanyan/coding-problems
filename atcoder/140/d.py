N, K = list(map(int, input().split()))
S = input()


def swap(s, l, r):
    sl = list(s)
    for i in range(l-1, l - 1 + ((r-l) // 2)):
        tmp = sl[i]
        sl[i] = 'R' if sl[r-i] == 'L' else 'L'
        sl[r-i] = 'R' if tmp == 'L' else 'L'
    return ''.join(sl)


ans = 0

for i in range(N):
    if S[i] == 'L' and i != 0 and S[i] == S[i-1]:
        ans += 1
    elif S[i] == 'R' and i != N - 1 and S[i] == S[i+1]:
        ans += 1

print(ans)

print(min(ans + 2 * K, N-1))
