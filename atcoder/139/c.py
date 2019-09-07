N = int(input())
towers = list(map(int, input().split()))
max_c = 0
c = 0
prev = 0
prev = towers[0]

for i in range(1, N):
    # print(i, c, prev, towers[i])
    if prev >= towers[i]:
        c += 1
    else:
        max_c = max(c, max_c)
        c = 0
    prev = towers[i]

max_c = max(c, max_c)
print(max_c)
