elemets = []

with open("input.txt", "r") as file:
    data = file.read().split("\n")
    for el in data:
        split = el.split(" ")
        if len(split) >= 2:
            elemets.append([int(t) for t in split])


def check_decreasing(arr):
    for el1, el2 in zip(arr[:-1], arr[1:]):
        if el1 <= el2:  # beacuse theay also are not allowed to be equal
            return False
    return True


def check_increasing(arr):
    for el1, el2 in zip(arr[:-1], arr[1:]):
        if el1 >= el2:
            return False
    return True


def get_max_adjacent_levels(arr):
    level = 0
    for el1, el2 in zip(arr[:-1], arr[1:]):
        level = max(level, abs(el1 - el2))
    return level


sum = 0
for el in elemets:
    if check_decreasing(el) or check_increasing(el):
        level = get_max_adjacent_levels(el)
        if 1 <= level <= 3:
            sum += 1

print(sum)
