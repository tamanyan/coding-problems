import math

# Check


def main():
    N = int(input())
    capacity = []

    for i in range(5):
        capacity.append(int(input()))

    m = min(capacity)
    print(math.ceil(N/m) + 4)


if __name__ == '__main__':
    main()
