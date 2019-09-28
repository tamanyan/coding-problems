
import sys
input = sys.stdin.readline


def get_key(item):
    return item[1]

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []

    for (k, v) in enumerate(A):
        B.append((v, k))

    B = sorted(B)
    B = [i[1]+1 for i in B]

    print(*B)


if __name__ == '__main__':
    main()
