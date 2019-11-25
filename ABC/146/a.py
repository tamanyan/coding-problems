import math


def main():
    S = input()
    arr = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT',
           'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    ans = 0
    flag = False

    if S == 'SUN':
        print(7)
        return

    for i in range(len(arr)):
        if arr[i] == S:
            flag = True

        if flag and arr[i] == 'SUN':
            break

        if flag:
            ans += 1

    print(ans)



if __name__ == '__main__':
    main()
