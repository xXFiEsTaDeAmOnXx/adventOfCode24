list_left = []
list_right = []
with open("input.txt", "r") as file:
    data = file.read().split("\n")
    for el in data:
        split = el.split("   ")
        if len(el) >= 2:
            list_left.append(int(split[0]))
            list_right.append(int(split[1]))


list_left.sort()
list_right.sort()
sum = 0
for left, right in zip(list_left, list_right):
    sum += abs(right - left)

print(sum)
