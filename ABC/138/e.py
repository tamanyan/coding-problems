
# import sys
# input = sys.stdin.readline
from collections import Counter


def main():
    s = input()
    t = input()
    ts = Counter(s)
    i = 0
    pos = 0

    while i < len(t):
        cur = pos % len(s)
        # print(len(t), i, cur, t[i], s[cur])

        if t[i] not in ts:
            pos = -1
            break

        if t[i] == s[cur]:
            i += 1
        # else:
        #     pos = -1
        #     break
        pos += 1

    print(pos)


if __name__ == '__main__':
    main()
