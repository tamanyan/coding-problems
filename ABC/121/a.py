def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H * W - (W * h + (H - h) * w))


if __name__ == '__main__':
    main()
