S = input()
ans = []
cur = ''


for i in range(len(S)):
    cur += S[i]

    if len(ans) == 0:
        ans.append(cur)
        cur = ''
    else:
        if ans[len(ans)-1] != cur:
            ans.append(cur)
            cur = ''

print(len(ans))
