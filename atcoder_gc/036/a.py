S = int(input())


for i in range(2, 10**9):
    if S % i == 0:
        print(i, S // i)
        break
