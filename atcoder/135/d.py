def rec(S, k):
    if k == len(S):
        return 1

    ret = 0

    if S[k] == '?':
        for i in range(10):
            ret += rec(S, k+1)
    else:
        ret += rec(S, k+1)

    return ret


S = input()
MOD = 10**9 + 7

print(rec(S, 0))
