import sys
import math

MOD = 10 ** 9 + 7


def main():
    S = input()

    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            print('Bad')
            return

    print('Good')


if __name__ == '__main__':
    main()
