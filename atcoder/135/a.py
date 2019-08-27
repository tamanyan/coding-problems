A, B = list(map(int, input().split()))
diff = abs(A - B)

if diff % 2 == 0:
    print(int(abs(diff / 2 + min(A, B))))
else:
    print('IMPOSSIBLE')
