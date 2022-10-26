n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
data1 = data[n-1]
data2 = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += data1
        m -= 1
    if m == 0:
        break
    result += data2
    m -= 1

print(result)
