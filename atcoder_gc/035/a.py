N = int(input())
a = list(map(int, input().split()))
dic = {}

for i in range(N):
    if a[i] not in dic:
        dic[a[i]] = 1
    else:
        dic[a[i]] += 1

values = list(dic.values())
keys = list(dic.keys())

if len(dic.keys()) == 3 and values[0] == values[1] == values[2] and keys[0] ^ keys[1] ^ keys[2] == 0:
    print('Yes')
elif len(dic.keys()) == 2 and 0 in dic and dic[0] * 3 == N:
    print('Yes')
elif len(dic.keys()) == 1 and 0 in dic:
    print('Yes')
else:
    print('No')
