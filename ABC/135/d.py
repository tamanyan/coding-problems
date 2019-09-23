# memo = None

# def rec(S, k, total):
#     if k == len(S)//3:
#         # print(total)
#         fixed_total = total + 5 if k % 2 == 0 else total - 5
#         # fixed_total = abs(total) + 5
#         memo[k][total % 13] = int((fixed_total) % 13 == 0)
#         return int((fixed_total) % 13 == 0)

#     if memo[k][total % 13] is not None:
#         return memo[k][total % 13]

#     s = S[k*3:k*3+3]
#     d1 = [str(i) for i in range(10)] if s[0] == '?' else [s[0]]
#     d2 = [str(i) for i in range(10)] if s[1] == '?' else [s[1]]
#     d3 = [str(i) for i in range(10)] if s[2] == '?' else [s[2]]
#     ret = 0

#     for i1 in d1:
#         for i2 in d2:
#             for i3 in d3:
#                 num = int(i1 + i2 + i3)
#                 if k % 2 == 0:
#                     ret += rec(S, k+1, total + num)
#                 else:
#                     ret += rec(S, k+1, total - num)

#     memo[k][total % 13] = ret
#     return ret

# MOD = 10**9 + 7
# S = input()

# if len(S) % 3 == 1:
#     S = '00' + S
# elif len(S) % 3 == 2:
#     S = '0' + S

# L = (len(S) // 3)
# dp = [[0 for i in range(14)] for j in range(L + 1)]
# # print(rec(S, 0, 0) % MOD)
# # print(memo)

# dp[0][0] = 1

# for k in range(L):
#     for m in range(13):
#         s = S[k*3:k*3+3]
#         d1 = [i for i in range(10)] if s[0] == '?' else [int(s[0])]
#         d2 = [i for i in range(10)] if s[1] == '?' else [int(s[1])]
#         d3 = [i for i in range(10)] if s[2] == '?' else [int(s[2])]

#         for i1 in d1:
#             for i2 in d2:
#                 for i3 in d3:
#                     num = 100 * i1 + 10 * i2 + i3
#                     dp[k + 1][(13 + num - m) % 13] += dp[k][m]

#         for i in range(13):
#             dp[k+1][i] %= MOD

# print(dp[L][5])

MOD = 10**9 + 7

S = input()
S = '?' * 10 ** 5
L = len(S)
memo = [[0 for i in range(14)] for j in range(L + 1)]
dp = [[0 for i in range(14)] for j in range(L + 1)]

dp[0][0] = 1
mul = 1

for k in range(L):
    for m in range(13):
        # print('S[-(k+1)]', S[-(k+1)], 'm', m)
        # if S[-(k+1)] == '?':
        #     for i in range(10):
        #         dp[k+1][(m + (mul * i) % 13) % 13] += dp[k][m]
        #         # print('dp[k+1][(m + (10 ** k + i) % 13) % 13]', dp[k+1][(m + (10 ** k + i) % 13) % 13])
        # else:
        #     dp[k+1][(m + (mul * int(S[-(k+1)])) % 13) % 13] += dp[k][m]
        #     # print('dp[k+1][(m + (10 ** k + int(S[-(k+1)])) % 13) % 13', dp[k+1][(m + (10 ** k + int(S[-(k+1)])) % 13) % 13])

        # for i in range(13):
        #     dp[k+1][i] %= MOD
        if S[k] == '?':
            for i in range(10):
                dp[k + 1][(m * 10 + i) % 13] += dp[k][m]
        else:
            dp[k + 1][(m * 10 + int(S[k])) % 13] += dp[k][m]

        for i in range(13):
            dp[k+1][i] %= MOD
    mul *= 10

print(dp[L][5])
