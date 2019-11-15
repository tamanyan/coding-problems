def main():
    A, B = list(map(int, input().split()))
    print(max(A - 2 * B, 0))


if __name__ == '__main__':
    main()
