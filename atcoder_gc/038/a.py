H, W, A, B = list(map(int, input().split()))

if H == 1 and W == 1:
    print(0)
else:
    if A <= (W // 2) and B <= (H // 2):
        for i in range(H):
            b = ''
            if i < H - B:
                for j in range(W):
                    if j < A:
                        b += '1'
                    else:
                        b += '0'
            else:
                for j in range(W):
                    if j < A:
                        b += '0'
                    else:
                        b += '1'
            print(b)
    else:
        print('No')
