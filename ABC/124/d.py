import math
from itertools import accumulate

INF = float("inf")


def main():
    N, K = map(int, input().split())
    S = input()
    zero_list = []
    A = []
    one = 0
    zero = 0

    for i in range(N):
        if S[i] == '1':
            one += 1
            if zero != 0:
                A.append(zero)
                zero_list.append(zero)
                zero = 0
        else:
            zero += 1
            if one != 0:
                A.append(one)
                one = 0

    if one != 0:
        A.append(one)
    elif zero != 0:
        A.append(zero)
        zero_list.append(zero)

    if len(zero_list) <= K:
        print(N)
        return

    section = 0
    if S[0] == '1':
        section = 3 + (K-1) * 2
    else:
        section = 2 + (K-1) * 2

    B = list(accumulate([0] + A))
    # print(B)
    if S[0] == '1':
        # print(*A, section)
        m = 0
        i = 0
        while True:
            if i % 2 == 0:
                section = 3 + (K-1) * 2
                end = min(i+section, len(B) - 1)
                # print(B[end] - B[i])
                # print(end)
                m = max(m, B[end] - B[i])
                if len(B) - 1 <= end:
                    break
            else:
                section = 2 + (K-1) * 2
                end = min(i+section, len(B) - 1)
                # print(B[end] - B[i])
                # print(end)
                m = max(m, B[end] - B[i])
                if len(B) - 1 <= end:
                    break
            i += 1
        print(m)
    else:
        m = 0
        i = 0
        while True:
            if i % 2 == 0:
                section = 2 + (K-1) * 2
                end = min(i+section, len(B) - 1)
                # print(B[end] - B[i])
                # print(end, len(B) <= end - 1)
                m = max(m, B[end] - B[i])
                if len(B) - 1 <= end:
                    break
            else:
                section = 3 + (K-1) * 2
                end = min(i+section, len(B) - 1)
                # print(B[end] - B[i])
                # print(end, len(B) <= end - 1)
                m = max(m, B[end] - B[i])
                if len(B) - 1 <= end:
                    break
            i += 1
        print(m)


if __name__ == '__main__':
    main()
