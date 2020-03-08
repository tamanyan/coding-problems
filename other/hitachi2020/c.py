from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
import sys
import bisect
import string
import math
import time


def I(): return int(input())


def S(): return input()


def MI(): return map(int, input().split())


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat)


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def lowestCommonAncestor(graph, root, p, q):
    pass
        # node_parent = {}  # key: node, value: node's parent
        # queue = deque([root])
        # # traverse all nodes by BST and construct node_parent map
        # while queue:
        #     edge = queue.popleft()
        #     nxt = graph[edge]
        #     if node.left:
        #         node_parent[node.left] = node
        #         queue.append(node.left)
        #     if node.right:
        #         node_parent[node.right] = node
        #         queue.append(node.right)

        # constcurt node existence on paths of p
        # In python, we can use set instead of dictionary
        # because it also takes O(1) to check value existence
        # pParents = set()
        # current = p
        # while current in node_parent:
        #     pParents.add(current)
        #     current = node_parent[current]
        # else:
        #     pParents.add(current)

        # # find first common node on paths of p and q
        # current = q
        # while current not in pParents:
        #     current = node_parent[current]
        # return current


def bfs(graph, initial, N):
    n = len(graph) - 1
    dist = [-1] * (n + 1)
    q = deque([initial])
    visited = [False] * (n + 1)
    visited[initial] = True
    dist[initial] = 0
    levels = [[] for i in range(N)]
    levels[0].append(initial)
    node_parent = {}

    while len(q) != 0:
        edge = q.popleft()
        nxt = graph[edge]

        for i, e in enumerate(nxt):
            if visited[e] is False:
                q.append(e)
                dist[e] = dist[edge] + 1
                levels[dist[e]].append(e)
                node_parent[e] = edge
                visited[e] = True

    return levels, node_parent


def main():
    N = I()
    # n = Segtree(10**5, )
    graph = [[] for i in range(N+1)]
    children = [[] for i in range(N+1)]
    # parents = [[] for i in range(N+1)]

    for i in range(N-1):
        x, y = MI()
        graph[x].append(y)
        graph[y].append(x)

    children = [set(i) for i in graph]

    levels, node_parent = bfs(graph, 1, N)
    # print(levels)
    # print(node_parent)
    # print(children)
    pairs = [[] for i in range(N+1)]

    for i in range(N-1):
        if i < N - 3:
            nodes = levels[i+3]
            for j in range(len(nodes)):
                pairs[i+1].append(nodes[j])

    for i in range(2, N):
        parent = node_parent[i]
        d_2 = children[parent]
        # print(i, parent)
        for node in d_2:
            if parent in node_parent and node == node_parent[parent]:
                continue

            if node == parent or node == i:
                continue

            for d_3 in children[node]:
                if d_3 != parent and d_3 != i:
                    # pairs.append((i, d_3))
                    pairs[i].append(d_3)
                # print(node, children[node])

        # if i > 0:
        #     parents = levels[i]
        #     for parent in parents:
                # nodes = levels[i+1]
                # for j in range(len(nodes)):
                #     if nodes[j] not in children[parent]:
                #         pairs.append((parent, nodes[j]))

    # print(pairs)
    m = [False] * (N+1)
    p = [0] * N
    cur = 1
    for p1 in range(1, N):
        if m[p1-1] is False:
            p[p1-1] = cur
            m[p1-1] = True
        for i in range(len(pairs[p1])):
            # print(target, p2)
            p2 = pairs[p1][i]
            if m[p2-1] is False:
                target = p[p1-1] + 3 * (i+1)
                p[p2-1] = target
                m[p2-1] = True
            else:
                if p[p1-1] + p[p2-1] % 3 == 0 or p[p1-1] * p[p2-1] % 3 == 0:
                    continue
                else:
                    print(-1)
                    return
        cur += 1

    print(*p)
    # for p1, p2 in pairs:
        # if m[cur] is False:
        #     m[cur] = True
        #     p[p1-1] = cur
        #     cur + 3



if __name__ == '__main__':
    main()

# 11
# 1 2
# 1 3
# 1 4
# 2 5
# 2 6
# 3 7
# 3 8
# 4 9
# 5 11
# 9 10
