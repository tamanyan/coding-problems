import math

# Check


def main():
    N = 5
    dishes = [0] * N
    m = 10 ** 9
    m_index = -1

    for i in range(N):
        dishes[i] = int(input())

    for i in range(len(dishes)):
        if m > dishes[i] % 10 and dishes[i] % 10 != 0:
            m = dishes[i] % 10
            m_index = i

    if m_index == -1:
        print(sum(dishes))
    else:
        print(sum([d // 10 * 10 + 10 if d % 10 != 0 else d for i, d in enumerate(dishes) if i != m_index]) + dishes[m_index])


if __name__ == '__main__':
    main()
