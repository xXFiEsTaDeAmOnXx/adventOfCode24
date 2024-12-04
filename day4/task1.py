import re

elemets = []

with open("input.txt", "r") as file:
    data = file.read().split("\n")[:-1]
    for el in data:
        elemets.append(el)


def get_horizontal_occurings(array):
    sum = 0
    for row in array:
        res1 = re.findall(r"(XMAS)", row)  # find xmas forward
        res2 = re.findall(r"(XMAS)", row[::-1])  # find xmas backwards
        sum += len(res1) + len(res2)
    return sum


def get_vertical_occurings(array):
    sum = 0
    for i in range(len(array[0])):  # for all colums
        stri = ""
        for j in range(len(array)):
            stri += array[j][i]
        res1 = re.findall(r"(XMAS)", stri)  # find xmas forward
        res2 = re.findall(r"(XMAS)", stri[::-1])  # find xmas backwards
        sum += len(res1) + len(res2)
    return sum


def find_diagonal_occurings(array):
    sum = 0
    nrow = len(array)
    ncol = len(array[0])
    for i in range(ncol):  # going down diagnoals starting at top edge
        l = ncol - 1 - i
        k = 0
        stri = ""
        while l < ncol and k < nrow:  # forward diagonal
            stri += array[k][l]
            l += 1
            k += 1
        res1 = re.findall(r"(XMAS)", stri)  # find xmas forward
        res2 = re.findall(r"(XMAS)", stri[::-1])  # find xmas backwards
        sum += len(res1) + len(res2)

    for i in range(1, nrow):  # goign down diagonals starting at left edge
        l = 0
        k = i
        stri = ""
        while l < ncol and k < nrow:  # forward diagonal
            stri += array[k][l]
            l += 1
            k += 1
        res1 = re.findall(r"(XMAS)", stri)  # find xmas forward
        res2 = re.findall(r"(XMAS)", stri[::-1])  # find xmas backwards
        sum += len(res1) + len(res2)

    for i in range(ncol):  #  going up diagonals starting at left edge
        l = i
        k = nrow - 1
        stri = ""
        while l < ncol and k >= 0:  # forward diagonal
            stri += array[k][l]
            l += 1
            k -= 1
        res1 = re.findall(r"(XMAS)", stri)  # find xmas forward
        res2 = re.findall(r"(XMAS)", stri[::-1])  # find xmas backwards
        sum += len(res1) + len(res2)

    for i in range(1, nrow):  # going up diagonals starting at left edge
        l = 0
        k = nrow - 1 - i
        stri = ""
        while l < ncol and k >= 0:  # forward diagonal
            stri += array[k][l]
            l += 1
            k -= 1
        res1 = re.findall(r"(XMAS)", stri)  # find xmas forward
        res2 = re.findall(r"(XMAS)", stri[::-1])  # find xmas backwards
        sum += len(res1) + len(res2)
    return sum


sum = (
    get_horizontal_occurings(elemets)
    + get_vertical_occurings(elemets)
    + find_diagonal_occurings(elemets)
)
print(sum)
