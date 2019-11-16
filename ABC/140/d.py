def main():
    N, K = list(map(int, input().split()))
    S = input()
    ans = 0

    for i in range(N):
        if S[i] == 'L' and i != 0 and S[i] == S[i-1]:
            ans += 1
        elif S[i] == 'R' and i != N-1 and S[i] == S[i+1]:
            ans += 1

    # print(ans)
    print(min(ans + (2 * K), N - 1))


if __name__ == '__main__':
    main()
