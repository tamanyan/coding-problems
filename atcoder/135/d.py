maps = input()
people = [0] * len(maps)

counter = 0
for i in range(len(maps)):
    if maps[i] == 'R':
        counter += 1
        if maps[i+1] == 'L':
            people[i] += (counter+1) // 2
            people[i+1] += counter // 2
    else:
        counter = 0

counter = 0
for i in range(len(maps) - 1, 0, -1):
    if maps[i] == 'L':
        counter += 1
        if maps[i-1] == 'R':
            people[i] += (counter+1) // 2
            people[i-1] += counter // 2
    else:
        counter = 0

print(*people)
