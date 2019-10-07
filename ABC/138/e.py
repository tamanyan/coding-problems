
# import sys
# input = sys.stdin.readline
import bisect


def ch_to_int(c):
    return ord(c) - 96


def main():
    s = input()
    t = input()
    pos = 0
    count = 0
    ch = [[] for i in range(27)]

    for i in range(len(s)):
        ch[ch_to_int(s[i])].append(i)

    for i in range(len(t)):
        c = ch_to_int(t[i])
        li = ch[c]

        if len(li) == 0:
            pos = -1
            count = 0
            break

        next_index = bisect.bisect_left(li, pos)
        # print(next_index, pos, li)
        if next_index >= len(li):
            next_pos = li[0]
            count += 1
            pos = next_pos + 1
        else:
            if pos == li[next_index]:
                pos += 1
            else:
                pos = li[next_index] + 1
        # print(li, next_index, pos, count)

    print(pos + count * len(s))


if __name__ == '__main__':
    main()
