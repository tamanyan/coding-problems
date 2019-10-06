
# import sys
# input = sys.stdin.readline
from collections import Counter
import string


def main():
    S = input()
    K = int(input())
    S_MAP = Counter(S)

    count_1st = 0
    S1 = list(S * 1)
    for i in range(len(S) - 1):
        if S1[i] == S1[i+1]:
            count_1st += 1
            S1[i+1] = '_'
            # for c in string.ascii_lowercase:
            #     if i == 0:
            #         if c != S1[i+1]:
            #             count_1st += 1
            #             S1[i+1] = c
            #             break
            #     else:
            #         if c != S1[i-1] and c != S1[i+1]:
            #             count_1st += 1
            #             S1[i+1] = c
            #             break

    count_2nd = 0
    S2 = list(S * 2)
    for i in range(len(S) * 2 - 1):
        if S2[i] == S2[i+1]:
            count_2nd += 1
            S2[i+1] = '_'

    count_3rd = 0
    S3 = list(S * 3)
    for i in range(len(S) * 3 - 1):
        if S3[i] == S3[i+1]:
            count_3rd += 1
            S3[i+1] = '_'

    count_4th = 0
    S4 = list(S * 4)
    for i in range(len(S) * 4 - 1):
        if S4[i] == S4[i+1]:
            count_4th += 1
            S4[i+1] = '_'

    # count_k = 0
    # SK = list(S * K)
    # for i in range(len(S) * K - 1):
    #     if SK[i] == SK[i+1]:
    #         for c in string.ascii_lowercase:
    #             if i == 0:
    #                 if c != SK[i+1]:
    #                     count_k += 1
    #                     SK[i+1] = c
    #                     break
    #             else:
    #                 if c != SK[i-1] and c != SK[i+1]:
    #                     count_k += 1
    #                     SK[i+1] = c
    #                     break

    # if K <= 4:
    #     if K == 1:
    #         print(count_1st)
    #     elif K == 2:
    #         print(count_2nd)
    #     elif K == 3:
    #         print(count_3rd)
    #     elif K == 4:
    #         print(count_4th)
    # print(len(S_MAP))
    if len(S_MAP) == 1 and len(S) % 2 == 1:
        d1 = count_2nd - count_1st
        d2 = count_3rd - count_2nd
        # print(d1)
        # print(d2)
        print(d1 * K//2 + d2 * K//2)
    # elif len(S)
    else:
        d = count_3rd - count_2nd
        # last_d = count_4th - count_3rd
        print(count_1st + d * (K-1))
        # print(*S1)
        # print(*S2)
        # print(*S3)
        # print(*S4)
        # print(d * K)
    # # print(K, d, count_1st)
    # # print(count_1st, count_2nd, count_3rd)
    # # print(count_k)
    # # print(*SK)


if __name__ == '__main__':
    main()
