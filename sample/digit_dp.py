MOD = 10**9+7
memo = None


def print_memo(memo):
    for k, v in enumerate(memo):
        print(k, 'False', str(v[0]))
        print(k, ' True', str(v[1]))


def rec(s, D, k, tight=True, d_sum=0, tried=[]):
    if k == len(s):
        memo[k][int(tight)][d_sum] = int(d_sum == D)
        # print('Save', tried, 'memo[{}][{}][{}]={}'.format(
        #     k, tight, d_sum, int(d_sum == D)))
        # print_memo(memo)
        return int(d_sum == D)

    if memo[k][int(tight)][d_sum] >= 0:
        # print('Return', tried, 'memo[{}][{}][{}]={}'.format(
        #     k, tight, d_sum, int(d_sum == D)))
        # print_memo(memo)
        return memo[k][tight][d_sum]

    x = int(s[k])
    r = x if tight else 9
    ret = 0

    for i in range(r+1):
        ret += rec(s, D, k+1, tight and i == r, d_sum + i, tried + [i])
        ret %= MOD

    # print('Save', tried + ['x'], 'memo[{}][{}][{}]={}'.format(
    #     k, tight, d_sum, int(d_sum == D)))
    memo[k][int(tight)][d_sum] = ret
    # print_memo(memo)

    return ret

S = input()
D = int(input())
L = len(S)+1
memo = [[[-1 for i in range(L*9)] for i in range(2)] for j in range(L)]
print(rec(S, D, 0))
