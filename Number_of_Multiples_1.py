n, x, y = map(int, input().split())
list = []
for i in range(1, n+1):
    if i % x == 0 or i % y == 0:
        list.append(i)
print(len(list))