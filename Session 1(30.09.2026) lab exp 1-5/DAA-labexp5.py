arr = [10, 20, 5, 30, 15]

max_element = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]

print(max_element)
