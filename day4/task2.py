import re

elemets = []

with open("input.txt", "r") as file:
    data = file.read().split("\n")[:-1]
    for el in data:
        elemets.append(el)


padded_array = []


boarder_size = 2
for i in range(boarder_size):  # add top padding
    stri = ""
    for j in range(len(elemets[0]) + boarder_size * 2):
        stri += "."
    padded_array.append(stri)

for row in elemets:
    stri = ""
    for j in range(boarder_size):  # boader in front
        stri += "."
    stri += row
    for j in range(boarder_size):  # boader in back
        stri += "."
    padded_array.append(stri)

boarder_size = 2
for i in range(boarder_size):  # add bottom padding
    stri = ""
    for j in range(len(elemets[0]) + boarder_size * 2):
        stri += "."
    padded_array.append(stri)


res_array = padded_array.copy()
# search x-mas
sum = 0
for i in range(len(elemets)):
    for j in range(len(elemets[i])):
        # check in 3x3 kernel
        first_dia = ""
        second_dia = ""
        for k in range(3):
            first_dia += padded_array[i + k - 1 + boarder_size][
                j + k - 1 + boarder_size
            ]  # get diagonal top right to left botom
            second_dia += padded_array[i - k + 1 + boarder_size][
                j + k - 1 + boarder_size
            ]  # get diagonal bootom right to right bottom

        res1 = re.findall(r"(MAS)", first_dia)  # find mas forward
        res2 = re.findall(r"(MAS)", first_dia[::-1])  # find mas backwards

        res3 = re.findall(r"(MAS)", second_dia)  # find mas forward
        res4 = re.findall(r"(MAS)", second_dia[::-1])  # find mas backwards

        if (len(res1) > 0 or len(res2) > 0) and (
            len(res3) > 0 or len(res4) > 0
        ):  # only conut if we saw x
            sum += 1
print(sum)
