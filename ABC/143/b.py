def main():
    N = int(input())
    d = list(map(int, input().split()))
    ans = 0

    for xi in range(len(d)):
        for yi in range(xi+1, len(d)):
            if xi != yi:
                ans += d[xi] * d[yi]

    print(ans)


if __name__ == '__main__':
    main()
