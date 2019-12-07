import sys
input = sys.stdin.readline


def main():
    N, A, B = map(int, input().split())
    print(min(N * A, B))


if __name__ == '__main__':
    main()
