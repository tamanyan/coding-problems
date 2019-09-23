import heapq

N, M = list(map(int, input().split()))
# A = list(map(int, input().split()))

# N = 10**5
# A = [10 for i in range(10**5)]
# M = 10**5

A = []
for i in input().split():
    heapq.heappush(A, -int(i))

while M > 0:
    heapq.heappush(A, -((-heapq.heappop(A))//2))
    M -= 1

print(-sum(A))
