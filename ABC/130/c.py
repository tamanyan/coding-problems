import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7


def main():
    W, H, x, y = map(int, input().split())

    # if (W % 2 == 0 and x == W // 2 and y != H and y != 0) or (H % 2 == 0 and y == H // 2 and x != W and x != 0):
    if (W % 2 == 0 and x == W // 2) and (H % 2 == 0 and y == H // 2):
        print(W*H/2, 1)
    else:
        print(W*H/2, 0)


if __name__ == '__main__':
    main()
