
import sys
from collections import Counter
import string

# input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

def divisor(n):
    """
    n の約数をリストで返す
    :param int n:
    :rtype: list of int
    """
    ret = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return ret


def factorization(n):
    """
    素因数分解
    :param int n:
    :rtype: list of int
    """
    if n <= 1:
        return []

    ret = []
    while n > 2 and n % 2 == 0:
        ret.append(2)
        n //= 2
    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            ret.append(i)
            n //= i
        else:
            i += 2
    ret.append(n)
    return ret


def is_prime(n):
    """
    nの素数判定
    :param int n:
    :rtype: Bool
    """
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def coprime(a, b):
    return gcd(a, b) == 1


def main():
    S = input()
    ans = 0
    cur = 0
    stack_initial = 0
    stack_count = 0
    # arr = []

    for i in range(len(S)):
        if i == 0 and S[i] == '<':
            cur = 0
            ans = 0
            cur = 1
        elif i == 0 and S[i] == '>':
            stack_count = 1
        elif S[i-1] == '<' and S[i] == '<':
            ans += cur
            cur += 1
        elif S[i-1] == '<' and S[i] == '>':
            # ans += cur
            stack_initial = cur
            # print('stack_initial', i, stack_initial)
            stack_count = 1
            cur = 0
        elif S[i-1] == '>' and S[i] == '>':
            stack_count += 1
        elif S[i-1] == '>' and S[i] == '<':
            stack_count += 1
            # ans += (stack_count * (0 + (stack_count)) // 2)
            # print(i, stack_initial, stack_count)
            if stack_count > stack_initial:
                ans += (stack_count * (0 + (stack_count - 1)) // 2)
            else:
                ans += stack_initial + ((stack_count - 1) * (0 + ((stack_count - 1) - 1)) // 2)
            stack_initial = 0
            stack_count = 0
            cur = 1
        # print(i, ans)

    if S[len(S)-1] == '<':
        ans += cur
        # print(cur)
    elif S[len(S)-1] == '>':
        stack_count += 1
        #
        if stack_count > stack_initial:
            ans += (stack_count * (0 + (stack_count - 1)) // 2)
        else:
            ans += stack_initial + ((stack_count - 1) * (0 + ((stack_count - 1) - 1)) // 2)
        # print(stack_count, ans)
        stack_count = 0
    print(ans)


if __name__ == '__main__':
    main()
