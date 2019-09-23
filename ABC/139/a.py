S = input()
T = input()

counter = 0

for i in range(len(S)):
    if S[i] == T[i]:
        counter += 1

print(counter)
