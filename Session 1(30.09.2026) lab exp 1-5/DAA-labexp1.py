arr = ["abc", "car", "ada", "racecar"]

for s in arr:
    if s == s[::-1]:
        print(s)
        break
else:
    print("No palindrome found")
