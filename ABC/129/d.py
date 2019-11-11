MOD = 10 ** 9 + 7


def dfs(graph, start):
    path = []
    stack = [start]

    while stack != []:
        v = stack.pop()
        if v not in path:
            path.append(v)
        for w in reversed(graph[v]):
            if w not in path:
                stack.append(w)

    return path


def main():
    H, W = map(int, input().split())
    S = [""] * H

    for i in range(H):
        S[i] = str(input())

    print(S)


if __name__ == '__main__':
    main()
