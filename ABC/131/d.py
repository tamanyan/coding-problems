import sys
import heapq
input = sys.stdin.readline

MOD = 10 ** 9 + 7


def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    h = []

    for i in range(N):
        A, B = map(int, input().split())
        # deadline, effort
        heapq.heappush(h, (B, A))

    days = 0
    for i in range(N):
        work = heapq.heappop(h)
        days += work[1]
        # print(days, work)
        if days > work[0]:
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    main()
