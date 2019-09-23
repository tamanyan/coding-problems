N = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)

counter = 0
for i in range(len(numbers)):
    if numbers[i] != sorted_numbers[i]:
        counter += 1

if counter <= 2:
    print('YES')
else:
    print('NO')
