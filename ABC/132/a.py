import sys
import math

MOD = 10 ** 9 + 7


def main():
    S = input()
    dic = {}

    for i in range(len(S)):
        if S[i] not in dic:
            dic[S[i]] = 1
        else:
            dic[S[i]] += 1

    if len(dic.keys()) == 2 and len([i for i in dic.values() if i == 2]):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
