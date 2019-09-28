def main():
    N = int(input())
    ans = 0

    for i in range(1, N+1):
        if i % 2 != 0:
            ans += 1

    print(ans/float(N))

    # for i in range(N):
    #     A = list(map(int, input().split()))


if __name__ == '__main__':
    main()
