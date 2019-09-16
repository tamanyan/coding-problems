N = int(input())
A = list(map(int, input().split()))
B = [0] * N
dp = [0] * N
bc = 0

for _i in range(N):
    i = N-_i
    cur = i * 2
    sum_b = 0
    # print('i', i)

    if i == 0:
        break

    while cur <= N:
        # print(i-1, cur)
        sum_b += B[cur-1]
        cur += i

    b = (sum_b + A[i-1]) % 2

    # print(i, b)
    if b == 1:
        B[i-1] = b
        bc += 1

# print(B)
print(bc)
if bc > 0:
    print(' '.join([str(i+1) for i in range(N) if B[i] > 0]))
