def main():
    N = int(input())
    S = input()
    ans = ''

    for i in range(len(S)):
        a = ord(S[i]) - ord('A') + N
        a = a % 26
        ans += chr(a + ord('A'))

    print(ans)


if __name__ == '__main__':
    main()
