list_left = []
list_right = []
with open("input.txt", "r") as file:
    data = file.read().split("\n")
    for el in data:
        split = el.split("   ")
        if len(el) >= 2:
            list_left.append(int(split[0]))
            list_right.append(int(split[1]))


def count_number(a, num):
    sum = 0
    for el in a:
        if el == num:
            sum += 1
    return sum


sum = 0

for val in list_left:
    res = val * count_number(list_right, val)
    sum += res

print(sum)
