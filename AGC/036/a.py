S = int(input())

X = 0
Y = 0

MAX = 10**9

x1, y1, x2, y2, x3, y3 = (0, 0, MAX, 1, 0, 0)

# S = x2 * y3 - x3 * y2
# S = 10**9 * y3 - x3 * 1

x3 = (MAX - S) % MAX
y3 = (S - 1) // MAX + 1

print("{} {} {} {} {} {}".format(x1, y1, x2, y2, x3, y3))
