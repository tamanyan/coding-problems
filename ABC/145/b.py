def main():
    N = int(input())
    S = input()

    if N % 2 == 1:
        print('No')
        return

    half = S[:N//2]
    half2 = S[N//2:]

    if half == half2:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
