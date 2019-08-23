N = int(input())
towers = list(map(int, input().split()))


for i in reversed(range(len(towers))):
    if len(towers) <= i+1:
        continue

    if towers[i] > towers[i+1]:
        towers[i] -= 1

# print(towers)

for i in range(1, len(towers)):
    if towers[i-1] > towers[i]:
        print('No')
        exit()

print('Yes')
