
import sys

input = sys.stdin.readline

# input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


def main():
    N = int(input())
    b = list(map(int, input().split()))
    ans = []

    for i in range(N):
        for j in range(len(b))[::-1]:
            if j+1 == b[j]:
                ans.append(b[j])
                b.remove(b[j])
                break
        else:
            print(-1)
            return

    ans = ans[::-1]
    for i in range(N):
        print(ans[i])


if __name__ == '__main__':
    main()
