MOD = 10 ** 9 + 7


# def dfs(graph, start):
#     options = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     W = len(graph)
#     H = len(graph[0])
#     ans = 0

#     for x in range(len(graph)):
#         for y in range(len(graph[x])):
#             if graph[x][y] == '#':
#                 continue

#             val = 1
#             path = []
#             stack = [(x, y, options)]
#             # print(x, y)

#             while stack != []:
#                 v = stack.pop()

#                 if v not in path:
#                     path.append(v)

#                 for op in v[2]:
#                     n = (v[0] + op[0], v[1] + op[1], [op])

#                     if n[0] >= 0 and n[0] < W and n[1] >= 0 and n[1] < H:
#                         f = graph[n[0]][n[1]]
#                         if n not in path and f == '.':
#                             stack.append(n)
#                             val += 1

#             ans = max(ans, val)
#             # print(ans)

#             if ans == 3999:
#                 return ans

#     return ans


def main():
    H, W = map(int, input().split())
    S = [None] * H
    w_score = [[0 for i in range(W)] for i in range(H)]
    h_score = [[0 for i in range(W)] for i in range(H)]
    stack = []

    for i in range(H):
        S[i] = list(input())

    for x in range(H):
        v = 0
        stack = []
        for y in range(W+1):
            if x >= 0 and x < H and y >= 0 and y < W and S[x][y] == '.':
                v += 1
                stack.append((x, y))
            else:
                if len(stack) == 0:
                    # w_score[x][y] = 0
                    stack = []
                elif len(stack) == 1:
                    first = stack.pop(0)
                    w_score[x][first[1]] = v
                    stack = []
                    v = 0
                else:
                    first = stack.pop(0)
                    last = stack.pop()
                    for y in range(first[1], last[1]+1):
                        w_score[x][y] = v
                    stack = []
                    v = 0

    for y in range(W):
        v = 0
        stack = []
        for x in range(H+1):
            if x >= 0 and x < H and y >= 0 and y < W and S[x][y] == '.':
                v += 1
                stack.append((x, y))
            else:
                if len(stack) == 0:
                    # w_score[x][y] = 0
                    stack = []
                elif len(stack) == 1:
                    first = stack.pop(0)
                    h_score[first[0]][y] = v
                    stack = []
                    v = 0
                else:
                    first = stack.pop(0)
                    last = stack.pop()
                    for x in range(first[0], last[0]+1):
                        h_score[x][y] = v
                    stack = []
                    v = 0

    ans = 0
    for x in range(H):
        for y in range(W):
            ans = max(ans, w_score[x][y] + h_score[x][y])

    print(ans-1)
    # print(w_score)
    # print(h_score)
    # print(dfs(S, S[0][0]))


if __name__ == '__main__':
    main()
