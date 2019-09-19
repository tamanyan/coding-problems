N, A, B, C, D = list(map(int, input().split()))
S = input()

A -= 1
B -= 1
C -= 1
D -= 1


def moveA(A, dest=True):
    if A == C:
        return A, True
    elif dest is True and A+1 == C and B != A+1:
        A += 1
    elif dest is True and A+2 == C and B != A+2:
        A += 2
    elif A+1 < N and S[A+1] == "." and B != A+1:
        A += 1
    elif A+2 < N and S[A+2] == "." and B != A+2:
        A += 2
    else:
        return A, True

    return A, False


def moveB(B, dest=True):
    if B == D:
        return B, True
    elif dest is True and B+1 == D and A != B+1:
        B += 1
    elif dest is True and B+2 == D and A != B+2:
        B += 2
    elif B+1 < N and S[B+1] == "." and A != B+1:
        B += 1
    elif B+2 < N and S[B+2] == "." and A != B+2:
        B += 2
    else:
        return B, True

    return B, False


if C < D:
    while B != D:
        B, stop = moveB(B)
        if stop:
            break
        # print(A, '=', C, ',', B, '=', D)

    while A != C:
        A, stop = moveA(A)
        if stop:
            break
        # print(A, '=', C, ',', B, '=', D)
else:
    while A < B and A != C:
        A, stop = moveA(A, dest=False)
        if stop:
            B, stop = moveB(B, dest=False)
            if stop:
                # for i in range(-3 + A, 4 + A):
                #     if i == A:
                #         print('A', end='')
                #     elif i == B:
                #         print('B', end='')
                #     else:
                #         print(S[i], end='')
                # print()
                # print(A, B, C, D)
                # print(A+2 < N and S[A+2] == "." and B != A+2)
                # print(S[A+2] == ".")
                # print(B != A+2)
                break
        # print(1, A, '=', C, ',', B, '=', D)

    while A != C:
        A, stop = moveA(A)
        if stop:
            # print('A', S[A-4:A+3], A, '=', C, ',', B, '=', D)
            break
        # print(2, A, '=', C, ',', B, '=', D)

    while B != D:
        B, stop = moveB(B)
        if stop:
            # print('B', S[B-4:B+3], A, '=', C, ',', B, '=', D)
            break
        # print(3, A, '=', C, ',', B, '=', D)

if A == C and B == D:
    print('Yes')
else:
    print('No')
