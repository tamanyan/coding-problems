N = int(input())
monsters = list(map(int, input().split()))
heros = list(map(int, input().split()))
nums = 0

for i in range(len(heros)):
    if monsters[i] <= heros[i]:
        heros[i] -= monsters[i]
        nums += monsters[i]
        monsters[i] = 0

        if monsters[i+1] <= heros[i]:
            heros[i] -= monsters[i+1]
            nums += monsters[i+1]
            monsters[i+1] = 0
        else:
            nums += heros[i]
            monsters[i+1] -= heros[i]
            heros[i] = 0
    else:
        nums += heros[i]
        monsters[i] -= heros[i]
        heros[i] = 0

print(nums)
