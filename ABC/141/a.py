S = input()

t = {
    1: ['L', 'U', 'D'],
    0: ['R', 'U', 'D'],
}

ans = 0

for i in range(len(S)):
    if S[i] in t[i % 2]:
        ans += 1

if ans == len(S):
    print('Yes')
else:
    print('No')
