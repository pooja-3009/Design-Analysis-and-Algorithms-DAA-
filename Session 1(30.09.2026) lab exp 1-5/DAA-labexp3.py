arr = [1, 2, 1]
total = 0

for i in range(len(arr)):
    s = set()
    for j in range(i, len(arr)):
        s.add(arr[j])
        total += len(s) ** 2

print(total)
