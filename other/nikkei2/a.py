import sys
input = sys.stdin.readline


def main():
    N = int(input())
    if N == 1 or N == 2:
        print(0)
        return

    print((N-1)//2)


if __name__ == '__main__':
    main()
