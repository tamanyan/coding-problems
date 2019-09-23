# def main():
#     N, Q = list(map(int, input().split()))
#     parents = [[] for i in range(N+1)]
#     ans = [0] * (N+1)

#     for i in range(N-1):
#         a, b = list(map(int, input().split()))
#         parents[b].append(a)

#     for i in range(Q):
#         p, x = list(map(int, input().split()))
#         ans[p] += x

#     print(parents[1:])

#     for i in range(1, N+1):
#         for p in parents[i]:
#             ans[i] += ans[p]

#     print(*ans[1:])

import sys
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    tree = [[] for i in range(N+1)]
    ans = [0] * (N+1)
    visit = [False]*(N+1)

    for i in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    for i in range(Q):
        p, x = map(int, input().split())
        ans[p] += x

    visit[1] = True
    q = [1]

    while len(q) != 0:
        n = q.pop()
        # print(tree[n])
        for i in tree[n]:
            if visit[i] is False:
                ans[i] += ans[n]
                # print(i, '+=', n)
                visit[i] = True
                q.append(i)

    print(*ans[1:])


if __name__ == '__main__':
    main()
