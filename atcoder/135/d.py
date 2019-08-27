from collections import Counter

S = input()
MOD = 10**9 + 7

c = Counter(S)
n = c['?']

for i in range(2 ** n):
    total = 0
    print("pattern {}: ".format(i), end="")
    for j in range(n):
        if ((i >> j) & 1):
            print(j)
