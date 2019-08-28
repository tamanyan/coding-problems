MOD = 10**9 + 7
memo = None


def rec(S, k, total):
    if k == len(S)//3:
        # print(total)
        fixed_total = total + 5 if k % 2 == 0 else total - 5
        # fixed_total = abs(total) + 5
        memo[k][total % 13] = int((fixed_total) % 13 == 0)
        return int((fixed_total) % 13 == 0)

    if memo[k][total % 13] is not None:
        return memo[k][total % 13]

    s = S[k*3:k*3+3]
    d1 = [str(i) for i in range(10)] if s[0] == '?' else [s[0]]
    d2 = [str(i) for i in range(10)] if s[1] == '?' else [s[1]]
    d3 = [str(i) for i in range(10)] if s[2] == '?' else [s[2]]
    ret = 0

    for i1 in d1:
        for i2 in d2:
            for i3 in d3:
                num = int(i1 + i2 + i3)
                if k % 2 == 0:
                    ret += rec(S, k+1, total + num)
                else:
                    ret += rec(S, k+1, total - num)

    memo[k][total % 13] = ret
    return ret

S = input()

if len(S) % 3 == 1:
    S = '00' + S
elif len(S) % 3 == 2:
    S = '0' + S

L = (len(S) // 3) + 1
memo = [[None for i in range(14)] for j in range(L)]
# print(rec(S, 0, 0) % MOD)
# print(memo)

for k in range(L//3):
    for m in range(13):
        s = S[k*3:k*3+3]
        d1 = [str(i) for i in range(10)] if s[0] == '?' else [s[0]]
        d2 = [str(i) for i in range(10)] if s[1] == '?' else [s[1]]
        d3 = [str(i) for i in range(10)] if s[2] == '?' else [s[2]]

        for i1 in d1:
            for i2 in d2:
                for i3 in d3:
                    num = int(i1 + i2 + i3)
                    if k % 2 == 0:
                        ret += rec(S, k+1, total + num)
                        ret %= MOD
                    else:
                        ret += rec(S, k+1, total - num)
                        ret %= MOD
