def main():
    S = input()
    a = S[:2]
    b = S[2:]

    if int(a) > 0 and int(a) < 13 and int(b) > 0 and int(b) < 13:
        print('AMBIGUOUS')
    elif int(a) > 0 and int(a) < 13:
        print('MMYY')
    elif int(b) > 0 and int(b) < 13:
        print('YYMM')
    else:
        print('NA')


if __name__ == '__main__':
    main()
