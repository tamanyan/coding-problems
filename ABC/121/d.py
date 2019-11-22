import math


def bits(n, max_bits):
    return [int(x) for x in format(n, '0{}b'.format(max_bits))]


def my(A, B):
    max_bits = len(bin(B)[2:])
    c = [0] * max_bits
    ans = -1

    # for n in range(A, B+1):
    #     a = bits(n, max_bits)
    #     for i in range(max_bits):
    #         if a[i] == 1:
    #             c[i] += 1

    #     if ans == -1:
    #         ans = n
    #     else:
    #         ans ^= n

    # print(ans)
    # print(*c)

    # print(*bits(A, max_bits))
    # print(*bits(B, max_bits))
    # print(int(math.ceil((B - A) / 2)))
    pair = []
    for C in [A-1, B]:
        cur = 1
        bit_list = []
        for i in range(0, max_bits):
            a = C // (cur * 2)
            b = C % (cur * 2)
            # print(a, b, (a * cur), (b - cur) + 1)
            bit_list.append((a * cur) + max((b - cur) + 1, 0))
            # print(C, i, a, b, (a * cur) + max((b - cur) + 1, 0))
            cur *= 2
        # print(bit_list)
        pair.append(bit_list)

    pair[0] = pair[0][::-1]
    pair[1] = pair[1][::-1]
    for i in range(max_bits):
        c[i] = pair[1][i] - pair[0][i]

    ans = ''
    for i in range(max_bits):
        if c[i] % 2 == 0:
            ans += '0'
        else:
            ans += '1'

    print(int(ans, 2))
    # print(*c)


def f(n):
    if n % 2 == 1 and n % 4 == 3:
        return 0
    elif n % 2 == 1 and n % 4 == 1:
        return 1
    elif n % 2 == 0 and n % 4 == 0:
        return 0 ^ n
    else:
        return 1 ^ n


def main():
    A, B = map(int, input().split())

    print(f(B) ^ f(A-1))


if __name__ == '__main__':
    main()
